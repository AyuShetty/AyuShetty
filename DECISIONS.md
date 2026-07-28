# DECISIONS.md

# AYU.OS Architectural Decisions

---

## Decision 001

**Date:** 2026-07-27

**Context:**
Build system needed a way to generate README and validate SVGs without introducing external dependencies.

**Decision:**
Use Python standard library only for all generators and build orchestration.

**Reasoning:**
- No unnecessary framework overhead
- Reproducible across environments
- Aligns with engineering principle: simplicity wins
- Future contributors only need Python runtime

**Alternatives:**
- Node.js-based build system
- Make + shell scripts
- Third-party static site generators

---

## Decision 002

**Date:** 2026-07-27

**Context:**
AYU.UI components needed a consistent coordinate system and viewport.

**Decision:**
Use `1000 x 500` as the standard viewBox for all panel and layout components. Use `64 x 64` for icons.

**Reasoning:**
- 1000x500 provides a 2:1 aspect ratio ideal for dashboard modules
- Matches existing design tokens and SVG specification
- Icons remain legible at small sizes with 64x64

**Alternatives:**
- 1200x800 for higher resolution
- Dynamic viewBox per component
- Single unified viewBox for everything

---

## Decision 003

**Date:** 2026-07-27

**Context:**
Templates needed a rendering strategy that remained maintainable.

**Decision:**
Use simple `{{placeholder}}` string replacement instead of introducing a templating engine.

**Reasoning:**
- Zero dependencies
- Transparent to future contributors
- Sufficient for current README generation complexity
- Easy to debug

**Alternatives:**
- Jinja2
- Mustache
- Python f-strings with template classes

---

## Decision 004

**Date:** 2026-07-27

**Context:**
Existing `assets/ui/` files were empty while `ayu-ui/` was designated as the canonical component library.

**Decision:**
Populate `assets/ui/` as direct copies of `ayu-ui/` primitives. Treat `assets/icons/` as the deployed icon set.

**Reasoning:**
- `assets/` serves as the runtime asset root for README and GitHub
- `ayu-ui/` remains the single source of truth for component design
- Copying keeps both directories synchronized for build and preview

**Alternatives:**
- Symlinks
- Build-time copy only
- Single shared directory

---

## Decision 005

**Date:** 2026-07-28

**Context:**
The original repository had a cyberpunk/space aesthetic (`cyber_hud.svg`, `ayu_os_v7_core.svg`) that contradicted the documented design language ("Not a cyberpunk poster", "Calm. Minimal. Purposeful.").

**Decision:**
Remove cyberpunk assets entirely. Adopt the clean engineering aesthetic defined in `DESIGN_LANGUAGE.md` and implemented in `ayu-ui/` components.

**Reasoning:**
- Design language explicitly rejects cyberpunk clichés
- Two conflicting visual languages created cognitive dissonance
- Clean engineering aesthetic aligns with Apple HIG, Nothing OS, Linear, NASA Mission Control inspirations
- Component system already embodied the correct aesthetic

**Alternatives:**
- Keep both aesthetics with a theme switcher
- Gradually migrate cyberpunk elements
- Hybrid approach

---

## Decision 006

**Date:** 2026-07-28

**Context:**
Content was scattered across inline README, empty templates, and hardcoded scripts. No single source of truth.

**Decision:**
Centralize ALL content in `data/*.json` files. Templates contain only structure. Scripts contain only logic.

**Reasoning:**
- Single source of truth for all profile content
- Content changes don't require code changes
- Data files are reviewable in PRs
- Enables future CMS or headless integration
- Aligns with "Components Before Screens" principle

**Alternatives:**
- Keep content in templates
- Use Markdown frontmatter
- Database-backed CMS

---

## Decision 007

**Date:** 2026-07-28

**Context:**
Component library was flat (`ayu-ui/*.svg`) with mixed primitive, layout, and feature components.

**Decision:**
Reorganize into three-layer hierarchy: `components/primitives/`, `components/layouts/`, `components/features/`.

**Reasoning:**
- Enforces component composition rules (primitives → layouts → features)
- Clear ownership and reuse boundaries
- Matches atomic design methodology
- Easier navigation and discovery

**Alternatives:**
- Flat structure with naming conventions
- Two-layer (atoms + molecules)
- Feature-based folders

---

## Decision 008

**Date:** 2026-07-28

**Context:**
Design tokens were only in `TOKENS.md` (markdown), not machine-readable.

**Decision:**
Create `tokens/*.json` files for all token categories (colors, spacing, radius, strokes, typography, animation, shadows) plus `index.json` as manifest.

**Reasoning:**
- Enables tooling (validation, theming, code generation)
- Single source of truth for both docs and code
- JSON is universally parseable
- Future: TypeScript definitions, CSS custom properties, Figma tokens

**Alternatives:**
- Keep markdown only
- YAML format
- CSS custom properties only

---

## Decision 009

**Date:** 2026-07-28

**Context:**
GitHub profile stats were hardcoded/empty in generators.

**Decision:**
Implement `fetch_github_stats.py` using GitHub GraphQL API, triggered by scheduled workflow. Store results in `data/stats.json` (gitignored).

**Reasoning:**
- Real data > fake data
- GraphQL provides precise data in single query
- Daily refresh keeps profile current
- GitHub Actions provides free token with `contents:write` permission

**Alternatives:**
- GitHub REST API (multiple calls needed)
- Third-party stats services (shields.io, etc.)
- Static badges only

---

## Decision 010

**Date:** 2026-07-28

**Context:**
SVG validation was basic (title, desc, style only).

**Decision:**
Enhance validator to check: viewBox, role="img", meaningful IDs, accessibility compliance. Run on every PR and build.

**Reasoning:**
- GitHub renders SVGs as images — must be accessible
- Meaningful IDs enable CSS targeting and debugging
- Validation prevents regressions
- CI enforcement ensures quality

**Alternatives:**
- Manual review only
- External SVG linter (svgo, svg-lint)
- Browser-based testing

---

## Decision 011

**Date:** 2026-07-28

**Context:**
Assets needed to be available at runtime for GitHub README rendering.

**Decision:**
Copy built assets from `dist/assets/` to root `assets/` during build. Both directories tracked in git.

**Reasoning:**
- GitHub README renders relative to repo root
- `assets/` at root serves as CDN for SVG components
- `dist/` is build output (ephemeral, gitignored in future)
- Simpler than configuring raw.githubusercontent.com URLs

**Alternatives:**
- Use raw.githubusercontent.com URLs in README
- GitHub Pages for asset hosting
- Data URIs in markdown

---

## Decision 012

**Date:** 2026-07-28

**Context:**
Boot sequence SVG used CSS animations (`@keyframes`) that GitHub strips from inline SVGs.

**Decision:**
Keep CSS animations in SVG for local viewing/documentation. Accept that GitHub will render static version. Document this limitation.

**Reasoning:**
- Animations work in browser, documentation, portfolio
- Static fallback is still informative
- Adding JS/fallback complexity violates simplicity principle
- Progressive enhancement: animation is bonus, not requirement

**Alternatives:**
- Remove all animations
- Use GIF/APNG for animated sections
- JavaScript-based animation (not possible in GitHub README)

---

## Decision 013

**Date:** 2026-07-28

**Context:**
README sections had duplicated inline SVG headers (7 nearly identical SVGs in original README).

**Decision:**
Create reusable `section-header.svg` component template parameterized by title and subtitle.

**Reasoning:**
- DRY principle — single component for all section headers
- Consistent visual hierarchy
- Easy to update design globally
- Reduces README size significantly

**Alternatives:**
- Keep inline SVGs with copy-paste
- Markdown headers only (no visual distinction)
- HTML `<details>` for collapsible sections

---

## Decision 014

**Date:** 2026-07-28

**Context:**
Project had accumulated duplicate/empty directories (`assets/ui/`, `assets/icons/ai/`, `assets/icons/backgrounds/`, etc.)

**Decision:**
Remove all empty placeholder directories. Consolidate assets into `components/` hierarchy. Delete cyberpunk assets.

**Reasoning:**
- Reduces cognitive load
- Eliminates sync burden
- Cleaner repository structure
- Matches actual architecture

**Alternatives:**
- Keep as documentation of intended structure
- Fill with placeholder content
- Archive instead of delete

---

## Decision 015

**Date:** 2026-07-28

**Context:**
Original `PROJECT.md`, `ARCHITECTURE.md`, `TODO.md` described a v1.0 that was already "complete" but had significant gaps.

**Decision:**
Update all constitution documents to reflect v2.0 reality: data-driven, component-hierarchy, automated, validated. Mark v1.0 items as complete, add v2.0 items.

**Reasoning:**
- Documentation must reflect reality
- Future contributors need accurate map
- Decision log captures why v2.0 differs from v1.0

**Alternatives:**
- Archive v1.0 docs, start fresh
- Add v2.0 as appendix
- Keep v1.0 as-is with disclaimer