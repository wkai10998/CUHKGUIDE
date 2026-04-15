# Assistant Chat Window Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the assistant page into a two-state chat experience with a centered empty canvas state that transitions into a standard dialogue window after the first message.

**Architecture:** Keep the existing Flask route and assistant API intact, but refactor the assistant template into one unified shell that owns the empty state, chat log, and fixed composer. Use CSS state classes and a small JS state machine to switch from empty state to chat mode on first interaction while preserving current message rendering and source display.

**Tech Stack:** Flask/Jinja templates, vanilla JavaScript, shared site CSS, unittest page rendering tests

---

### Task 1: Lock the new assistant page contract in tests

**Files:**
- Modify: `tests/test_pages.py`

- [ ] Add assertions for the new empty-state heading, unified assistant shell markers, and fixed composer wrapper.
- [ ] Run `python3 -m unittest tests.test_pages -v` or `.venv/bin/python -m unittest tests.test_pages -v` and confirm the new assertions fail before implementation.

### Task 2: Refactor the assistant template into a unified two-state shell

**Files:**
- Modify: `templates/assistant.html`

- [ ] Replace the split intro/chat structure with one assistant shell containing the empty-state hero, suggested question chips, chat log, and fixed composer.
- [ ] Add stable data/class hooks for JS state transitions and test coverage.

### Task 3: Implement the assistant empty-state and chat-state visual system

**Files:**
- Modify: `static/css/app.css`
- Modify: `templates/base.html` (only if a page-level assistant class is needed for header toning)

- [ ] Add desktop and mobile styles for the centered empty canvas state, the chat-state layout, and the fixed bottom composer.
- [ ] Reduce header weight on the assistant page without breaking the shared site shell.
- [ ] Keep message bubbles, chips, and composer accessible and responsive.

### Task 4: Add first-message state switching logic

**Files:**
- Modify: `static/js/assistant_chat.js`

- [ ] Introduce a small state toggle that switches the assistant shell from empty state to chat mode on first user action.
- [ ] Ensure the initial assistant greeting appears in chat mode without showing as a separate block in the default empty state.
- [ ] Preserve existing submit, loading, error, and source-link behavior.

### Task 5: Verify the redesign end-to-end

**Files:**
- Modify as needed from tasks above

- [ ] Run `.venv/bin/python -m unittest tests.test_pages -v`.
- [ ] Run `.venv/bin/python -m unittest discover -s tests -v`.
- [ ] Review the assistant page in the browser for both empty state and active chat state before claiming completion.
