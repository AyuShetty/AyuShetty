#!/usr/bin/env python3
"""
AYU.OS GitHub Stats Fetcher
Fetches GitHub statistics via GraphQL API and writes to data/stats.json
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib import request, error

GRAPHQL_URL = "https://api.github.com/graphql"

QUERY = """
query($login: String!) {
  user(login: $login) {
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
      totalCount
      nodes {
        stargazerCount
        forkCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges {
            size
            node { name }
          }
        }
      }
    }
    followers { totalCount }
    following { totalCount }
    contributionsCollection {
      totalCommitContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
          }
        }
      }
    }
  }
}
"""

def fetch_stats(token: str, login: str) -> dict | None:
    """Fetch stats from GitHub GraphQL API."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "AYU.OS-Profile/1.0"
    }
    
    payload = {
        "query": QUERY,
        "variables": {"login": login}
    }
    
    req = request.Request(
        GRAPHQL_URL,
        data=json.dumps(payload).encode(),
        headers=headers,
        method="POST"
    )
    
    try:
        with request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            
            if "errors" in data:
                print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
                return None
            
            return data.get("data", {}).get("user")
    except error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.read().decode()}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error fetching stats: {e}", file=sys.stderr)
        return None

def process_stats(user_data: dict) -> dict:
    """Process raw GraphQL response into stats dict."""
    if not user_data:
        return {}
    
    repos = user_data.get("repositories", {})
    repo_nodes = repos.get("nodes", [])
    
    # Language stats
    lang_bytes = {}
    for repo in repo_nodes:
        for edge in repo.get("languages", {}).get("edges", []):
            lang = edge["node"]["name"]
            size = edge["size"]
            lang_bytes[lang] = lang_bytes.get(lang, 0) + size
    
    total_bytes = sum(lang_bytes.values())
    top_languages = [
        {"language": lang, "bytes": size, "percentage": round(size / total_bytes * 100, 1)}
        for lang, size in sorted(lang_bytes.items(), key=lambda x: -x[1])[:10]
    ] if total_bytes > 0 else []
    
    # Streak calculation
    calendar = user_data.get("contributionsCollection", {}).get("contributionCalendar", {})
    streak_current = 0
    streak_longest = 0
    current_streak = 0
    
    for week in calendar.get("weeks", []):
        for day in week.get("contributionDays", []):
            if day.get("contributionCount", 0) > 0:
                current_streak += 1
                streak_longest = max(streak_longest, current_streak)
            else:
                current_streak = 0
    
    # Current streak from end
    today = datetime.now(timezone.utc).date()
    for week in reversed(calendar.get("weeks", [])):
        for day in reversed(week.get("contributionDays", [])):
            day_date = datetime.fromisoformat(day["date"]).date()
            if day_date > today:
                continue
            if day.get("contributionCount", 0) > 0:
                streak_current += 1
            else:
                break
        else:
            continue
        break
    
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "public_repos": repos.get("totalCount", 0),
        "total_stars": sum(r.get("stargazerCount", 0) for r in repo_nodes),
        "total_forks": sum(r.get("forkCount", 0) for r in repo_nodes),
        "total_commits_1y": user_data.get("contributionsCollection", {}).get("totalCommitContributions", 0),
        "followers": user_data.get("followers", {}).get("totalCount", 0),
        "following": user_data.get("following", {}).get("totalCount", 0),
        "top_languages": top_languages,
        "streak_current": streak_current,
        "streak_longest": streak_longest,
    }

def main():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    login = os.environ.get("GITHUB_ACTOR", "AyuShetty")
    
    if not token:
        print("GH_TOKEN or GITHUB_TOKEN environment variable required", file=sys.stderr)
        sys.exit(1)
    
    print(f"Fetching stats for {login}...")
    user_data = fetch_stats(token, login)
    
    if not user_data:
        print("Failed to fetch stats", file=sys.stderr)
        sys.exit(1)
    
    stats = process_stats(user_data)
    
    output_path = Path("data/stats.json")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(stats, indent=2))
    
    print(f"✅ Stats written to {output_path}")
    print(f"   Repos: {stats.get('public_repos')}")
    print(f"   Stars: {stats.get('total_stars')}")
    print(f"   Followers: {stats.get('followers')}")

if __name__ == "__main__":
    main()