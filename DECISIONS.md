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
