You are orchestrating the implementation of a UI user story in this project. Follow these three phases in order and report where you are in the process as you go, and which agent is being used where applicable.

## User Story

$ARGUMENTS

---

## Phase 1 — Design

Use the `ux-design-planner` sub-agent to produce a full UI/UX design specification for the user story above. Pass the story verbatim as the prompt. Wait for the agent to return its spec before proceeding.

## Phase 2 — Implementation

Using the design spec returned in Phase 1:

1. Identify which files need to change (`models.py`, `views.py`, `templates/`, `static/css/styles.css`, etc.).
2. Implement the feature — models first, then view logic, then templates/CSS.
3. Add or update unit tests in `tests/` and run them with `python -m unittest discover -s tests`. All tests must pass before continuing.

## Phase 3 — Visual Verification

Use the `flask-feature-verifier` sub-agent to:
1. Start the Flask app (if not already running).
2. Navigate to the new feature with Playwright.
3. Interact with it to confirm it works end-to-end.
4. Take a screenshot and save it to `test-output/` with a descriptive filename.

Report back with a summary of what was built and the path to the saved screenshot.
