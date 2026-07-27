# COMPONENT_SPEC.md

# AYU.UI Component Specification

Version: 1.0.0

---

# Purpose

This document defines the engineering standards for every reusable SVG component in AYU.OS.

Every component inside `ayu-ui/` must comply with these rules.

No exceptions.

---

# Philosophy

AYU.UI is a component library.

Not an asset folder.

Every component should be reusable.

Every component should solve one problem.

Every component should remain independent.

---

# Component Hierarchy

Primitive Components

↓

Layout Components

↓

Feature Components

↓

README Interface

Never skip a layer.

---

# Primitive Components

Primitive components are the smallest reusable building blocks.

Examples:

- panel
- divider
- grid
- corner
- chip
- icon
- badge
- status-dot

Primitive components should never depend on another component.

---

# Layout Components

Built from primitives.

Examples:

- terminal
- dashboard
- navigation
- sidebar
- window

Layout components should remain content agnostic.

---

# Feature Components

Built from layouts.

Examples:

- Mission Control
- Kernel
- Experience
- Projects
- Timeline

---

# SVG Standards

Every SVG must:

- validate successfully
- contain no syntax errors
- contain title
- contain desc
- contain XML comments
- contain grouped sections
- use meaningful IDs

Never leave unused elements.

Never leave hidden layers.

---

# SVG Header

Every SVG should begin with:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="..."
    role="img"
>
```

---

# Accessibility

Required:

```
<title>

<desc>
```

Optional:

```
aria-labelledby
```

Every SVG should be understandable by screen readers.

---

# Group Structure

Every component should use groups.

Example:

```xml
<g id="background">

<g id="panel">

<g id="border">

<g id="content">

<g id="decorations">
```

Avoid deeply nested groups.

---

# IDs

Good

```
panel

panel-border

panel-shadow

corner-top-left

grid-major

grid-minor
```

Bad

```
Layer 1

Rectangle 25

Path123

Group17
```

---

# Coordinate System

Always design around a predictable viewBox.

Preferred viewBoxes:

Panels

```
1000 x 500
```

Icons

```
64 x 64
```

Badges

```
200 x 60
```

Windows

```
1200 x 700
```

Avoid arbitrary dimensions.

---

# Border Specification

Stroke:

1.5px

Rounded joins.

Rounded caps.

No glow.

No gradients.

Borders should communicate structure.

---

# Corner Specification

Corner length:

24px

Corner thickness:

same as border

Corners should:

- align perfectly
- mirror each other
- never overlap borders

---

# Radius

Panels

12px

Cards

10px

Badges

8px

Buttons

8px

Keep radius consistent.

---

# Grid Specification

Grid spacing:

8px base unit

Major grid:

32px

Minor grid:

8px

Every layout should snap to the grid.

---

# Padding

Internal panel padding

32px

Section spacing

48px

Component spacing

24px

Small spacing

16px

Micro spacing

8px

Never invent spacing values.

---

# Color Tokens

Rather than hardcoding colors, define reusable tokens.

Background

```
--surface
```

Border

```
--border
```

Primary Text

```
--text-primary
```

Secondary Text

```
--text-secondary
```

Success

```
--success
```

Warning

```
--warning
```

Critical

```
--critical
```

Future generators may replace these with actual values.

---

# Decorations

Decorations should be subtle.

Examples:

- corner accents
- alignment markers
- grid lines

Never dominate the interface.

---

# Animation

SVGs should remain static.

Animations should be added externally.

Never embed animation directly into reusable components.

---

# File Naming

Good

```
panel.svg

divider.svg

grid.svg

terminal.svg

window.svg

status-card.svg
```

Bad

```
panel2.svg

new.svg

copy.svg

updated.svg

test.svg
```

---

# Documentation

Every component should begin with XML comments.

Example

```xml
<!--
Component:

Panel

Purpose:

Reusable container for dashboard modules.

Version:

1.0
-->
```

---

# Reusability Test

Before approving a component ask:

Can this be used in three different places?

If the answer is no,

it probably isn't reusable enough.

---

# Performance

Avoid:

- unnecessary paths
- duplicated shapes
- deeply nested groups
- repeated definitions

Prefer:

- simple geometry
- reusable defs
- minimal XML

---

# Quality Checklist

Every component should satisfy:

- Valid SVG
- Accessible
- Reusable
- Modular
- Documented
- Clean IDs
- Consistent spacing
- Consistent radius
- Consistent borders
- No unnecessary complexity

Only then should the component become part of AYU.UI.