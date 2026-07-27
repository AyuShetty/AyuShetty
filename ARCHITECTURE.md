# ARCHITECTURE.md

# AYU.OS Architecture

**Version:** 1.0.0

---

# Purpose

This document describes the current architecture of the repository.

Unlike `PROJECT.md`, this file should only describe what currently exists.

Future ideas belong in `TODO.md`.

Architectural decisions belong in `DECISIONS.md`.

---

# Repository Layout

```
AyuShetty/
│
├── README.md
├── PROJECT.md
├── ARCHITECTURE.md
├── TODO.md
├── DECISIONS.md
│
├── assets/
├── ayu-ui/
├── docs/
├── templates/
├── scripts/
├── generated/
└── .github/
```

---

# Repository Components

## README.md

Public-facing GitHub profile.

Acts as the primary interface visitors see.

Currently maintained manually.

Future versions may be generated automatically.

---

## PROJECT.md

Defines repository philosophy.

Contains AI instructions.

Acts as the engineering constitution.

---

## ARCHITECTURE.md

Documents the current repository architecture.

Should always reflect reality.

---

## TODO.md

Tracks planned features and future milestones.

---

## DECISIONS.md

Stores architectural decisions and the reasoning behind them.

---

# assets/

Stores static visual assets.

Examples:

- illustrations
- backgrounds
- exported graphics

These assets are not reusable UI components.

---

# ayu-ui/

Contains reusable SVG primitives.

Every component should be generic enough to be reused across multiple modules.

Examples:

- panels
- grids
- dividers
- windows
- chips
- icons

This folder represents the design system of AYU.OS.

---

# docs/

Contains engineering documentation.

Examples include:

- design language
- SVG standards
- component specifications
- implementation guides

---

# templates/

Contains reusable Markdown templates.

Examples:

- section templates
- card templates
- module templates

Templates should not contain project-specific content.

---

# scripts/

Contains build automation.

Typical responsibilities include:

- README generation
- SVG optimization
- validation
- asset generation

Scripts should remain independent where possible.

---

# generated/

Contains generated files.

Nothing inside this directory should be edited manually.

Generated content should always be reproducible.

---

# Build Process

Current State:

Manual.

Future State:

Repository generation through Python scripts.

---

# Design System

AYU.OS follows a component-first architecture.

Every interface should be assembled from reusable SVG components.

Screens are compositions.

Components are primitives.

---

# Current Technology Stack

Markdown

SVG

Python

GitHub Actions (planned)

No unnecessary frameworks should be introduced unless they provide clear architectural value.

---

# Design Principles

The repository prioritizes:

- modularity
- readability
- maintainability
- scalability
- consistency

Every file should have a clearly defined responsibility.

---

# Current Status

Repository Foundation

Status: Complete

Reusable Component Library

Status: In Progress

Documentation

Status: In Progress

Automation

Status: Planned

README Generation

Status: Planned

---

# Future Expansion

Future modules should extend the existing architecture rather than replace it.

New features should integrate naturally into the existing design system.

Avoid architectural rewrites whenever possible.