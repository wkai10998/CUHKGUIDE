# ToCU Whole-Site Redesign Design

Date: 2026-04-12
Project: ToCU Flask web app
Source of visual truth: `DESIGN.md`

## 1. Intent

Redesign the entire ToCU website into a unified information platform for CUHK taught master's applicants.

The site should feel like an editorial application guide with light companionship, not a generic tool dashboard. It should help users understand what ToCU is, where to start, and how to move through the application process without anxiety.

## 2. Product Framing

### Target user

Applicants who are specifically preparing for CUHK master's applications.

### Core promise

ToCU explains CUHK master's application timelines, materials, steps, and common blockers in one calm, coherent place.

### Tone

Hybrid tone:
- Primary: editorial, trustworthy, quiet, refined
- Secondary: lightly supportive and companion-like

### Success criteria

- The home page clearly communicates what ToCU is in one screen.
- Navigation is simplified to four primary destinations.
- Visual style is consistent across all major pages.
- The application timeline is no longer a detached visual gimmick on the home page.
- The guide area becomes the primary place where users understand the six-stage process.
- Existing functional behavior remains available: program lookup, guide details, comments, progress state, assistant, login/profile.

## 3. Non-Goals

- No new standalone timeline page.
- No heavy dashboard experience.
- No major account-system expansion.
- No FAQ in primary navigation.
- No dark-mode chapter treatment for the assistant page.

## 4. Information Architecture

Primary navigation will be reduced to:

- Home
- Programs
- Guides
- Assistant

Secondary navigation and footer may reference:

- FAQ
- Login / Register
- Profile actions

### Destination responsibilities

#### Home

Acts as a cover page for the product.

Its job is to:
- explain what ToCU is
- state the product promise and slogan
- provide immediate access to the three main functional areas
- show login or user-state controls in the header

It should not carry the full timeline or six-stage overview.

#### Programs

Acts as a calm, searchable directory for program comparison.

Its job is to:
- help applicants compare programs, schools, language requirements, and deadlines
- feel more like a refined directory than a stack of promotional cards

#### Guides

Acts as the primary place for understanding the application process.

Its default state should:
- show all six stages as the main overview
- let the user choose the stage they are currently in
- optionally offer a “continue where you left off” entry based on the existing `last_stage` cookie

#### Assistant

Acts as the fastest route for solving a concrete question.

Its job is to:
- stay visually aligned with the rest of the site
- feel focused and quiet
- not visually overpower the information architecture

#### FAQ

Remains accessible but outside the primary navigation. It should behave as secondary/supporting content.

## 5. Visual Direction

All visual decisions should follow `DESIGN.md`.

### Design language

- Warm parchment page background
- Ivory panels and card surfaces
- Warm neutrals only
- Serif headlines, sans-serif interface text
- Terracotta used sparingly for primary emphasis
- Ring-style borders and restrained elevation
- Generous spacing and editorial pacing

### Primary tokens to emphasize

- Background: `#f5f4ed`
- Elevated light surfaces: `#faf9f5`
- Primary text: `#141413`
- Secondary text: `#5e5d59`
- Borders: `#f0eee6` and `#e8e6dc`
- Brand accent: `#c96442`

### Global behavioral rules

- Avoid purple-heavy branding currently present in the site.
- Reduce decorative gradients and glassy card treatment.
- Prefer thin warm borders, ring shadows, and restrained layering.
- Preserve approachability with soft radii and generous whitespace.
- Keep the visual system consistent across all primary pages.

## 6. Shared Layout System

### Header

The header should be redesigned as a refined, sticky editorial nav.

Requirements:
- brand mark / wordmark on the left
- four primary nav items in the center/right
- login button when logged out
- compact user avatar/profile entry when logged in
- homepage must visibly include login or user-state controls

Mobile:
- retain access to the same four primary destinations
- keep account entry visible and usable

### Main container behavior

Use wider, more editorial content widths rather than the current mixed open-layout vs boxed-layout split. Pages can still vary in width by content type, but they should clearly feel part of the same system.

### Footer

Footer remains secondary and quiet.

Requirements:
- remove “main product destination” feeling
- keep supporting links only
- keep FAQ accessible here if not promoted elsewhere

## 7. Home Page

### Goal

The home page should become minimal, premium, and immediately legible.

### Chosen direction

Use the approved “A1” direction: cover-style home page.

### Required content

- Product name: `ToCU`
- Clear product description for CUHK master's applicants
- A concise slogan
- Primary entry points to:
  - Programs
  - Guides
  - Assistant
- Login or user-state UI in the header

### Structure

1. Refined global header
2. Large hero / cover section
3. Minimal supporting copy
4. Three functional entry actions or cards

### Explicit exclusions

- No full timeline graphic
- No six-stage overview
- No dense information stack
- No dashboard widgets

### Emotional target

The page should feel like the cover of an application guidebook rather than a control panel.

## 8. Programs Page

### Goal

Turn the page into a refined lookup directory for CUHK programs.

### Structure

1. Editorial page heading
2. Search/filter strip
3. Calm card or list-based result grid

### Page behavior

- Keep the existing search/filter behavior
- Preserve current content fields
- Improve hierarchy so name, school, requirements, and deadline are easier to scan

### Visual rules

- Avoid loud gradient cards
- Prefer lighter, more uniform containers
- Make results feel like well-typeset records, not marketing blocks

## 9. Guides Overview Page

### Goal

This becomes the default home for the timeline/process understanding.

### Structure

1. Editorial heading
2. Optional “resume where you left off” panel when `last_stage` exists
3. Six-stage overview grid

### Six-stage overview

Use the existing six stages from `content/stages.json`:

1. `prep`
2. `docs`
3. `apply`
4. `fill`
5. `submit`
6. `wait`

Each stage card should surface:
- stage number
- stage title
- stage date range
- concise description
- stage entry CTA

### Importance

This page is now the primary place where the process is visualized. It replaces the need to do timeline-heavy storytelling on the home page.

## 10. Guide Detail Page

### Goal

Make the detail page feel like a readable guide chapter rather than a busy admin/workflow screen.

### Keep

- stage navigation
- current step detail
- completion toggle
- image
- tutorial content
- notes
- materials
- comments

### Change

- reduce the “utility dashboard” feeling
- improve reading rhythm and spacing
- make the central reading column feel like the main narrative surface
- treat side panels as supporting annotations rather than equal-weight tool blocks

### Layout

Retain a three-zone structure:
- left: stage/step navigation
- center: main reading content
- right: materials and reminders

But visually rebalance it to make the center dominant and calmer.

## 11. Assistant Page

### Goal

Keep the assistant useful, but visually consistent with the main product system.

### Requirements

- Do not redesign it as a dark chapter
- Keep it on the same warm, light visual system as the rest of the site
- Preserve suggested questions and the current chat flow
- Make the page feel focused and editorial, not flashy or overly “chat app”

### Visual direction

- quiet light containers
- refined message contrast
- restrained controls
- strong spacing around intro copy and composer

## 12. FAQ Treatment

FAQ remains part of the product but outside the primary navigation.

Recommended placement:
- footer link
- optional supporting link from assistant or guides

The FAQ page should inherit the same global visual system rather than appearing as a separate mini-brand.

## 13. Authentication Surfaces

Login, register, and profile surfaces should be visually brought into the same system.

### Requirements

- The home page header must show login when logged out
- The home page header must show user state when logged in
- Login page and login modal should visually match the redesigned header and surface system
- Profile dropdown should look intentional and editorial, not like a utility popover pasted on top

## 14. Responsive Behavior

Follow `DESIGN.md` responsive guidance.

### Mobile priorities

- Home hero remains elegant and clear, not cramped
- Header still exposes the four primary destinations
- Programs filters stack cleanly
- Guides overview becomes a single-column six-stage flow
- Guide detail collapses into a readable top-down flow
- Assistant remains easy to use without losing composition quality

## 15. Content and Data Constraints

Use existing data and routing wherever practical.

Current content/data sources to preserve:
- `content/stages.json`
- `content/guide_steps.json`
- `content/programs.json`
- `content/faq.json`
- existing assistant endpoints
- existing login/profile/session logic
- existing progress cookie/session behavior

This redesign is primarily structural and visual, with only light behavior additions around navigation clarity and “resume where you left off.”

## 16. Accessibility and Interaction Rules

- Preserve visible focus states
- Maintain strong text contrast on warm surfaces
- Keep tap targets large enough on mobile
- Use semantic headings and preserve template accessibility affordances
- Avoid decorative motion that competes with reading

## 17. Implementation Boundaries

The redesign should be implemented through the existing Flask/Jinja structure, mainly by updating:

- `templates/base.html`
- `templates/header.html`
- `templates/footer.html`
- `templates/index.html`
- `templates/programs.html`
- `templates/guide_list.html`
- `templates/guide.html`
- `templates/assistant.html`
- `templates/faq.html`
- `templates/login.html`
- `templates/login_modal.html`
- `static/css/app.css`

JavaScript changes should stay light and only support layout/navigation needs, not invent new application logic unless necessary.

## 18. Final Design Decisions Locked

- Whole-site redesign, not homepage-only
- `DESIGN.md` is the UI source of truth
- Home page uses the approved minimal “A1” cover direction
- Timeline is not a standalone tab
- Home page does not carry the process visualization
- Primary navigation is only: Home, Programs, Guides, Assistant
- Guides overview page becomes the six-stage process overview
- Guide overview may include a “continue where you left off” entry
- Programs page becomes a calmer directory
- Guide detail becomes a reading-first chapter page
- Assistant remains light, not dark
- FAQ stays out of the primary nav
- Home page must visibly include login or user-state UI
