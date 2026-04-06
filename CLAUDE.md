# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (use a virtual environment)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run the app
python src/app.py

# Run tests
python -m unittest discover -s tests
```

## Architecture

Flask app with a simple MVC-like structure under `src/`:

- **app.py** — creates the Flask instance and registers routes via `add_url_rule()`
- **views.py** — route handler functions (`index`, `course`)
- **models.py** — `Course` dataclass with hardcoded static data (no database)
- **templates/** — Jinja2 templates; `layout.html` is the base, others extend/include it
- **static/css/styles.css** — app styling

Routes: `/` (index) and `/course/<course_id>` (course detail).

The `course.html` template references `course.topics`, but the `Course` model and `course()` view don't provide this — any feature work on the course detail page should account for this gap.

## Add unit tests
- When you add any code changes, you must also add unit test changes, run them, and ensure that all unit tests pass.

### Verify Changes with Playwright (MANDATORY)

**After implementing any new feature, you MUST:**
1. Start the Flask application (if not already running - `python src/app.py`)
1. Use the Playwright MCP tool to connect to the application at `http://127.0.0.1:5000`
1. Navigate to and interact with the new feature to verify it works correctly
1. Take a screenshot of the working feature
1. Save the screenshot in the `test-output/` folder with a descriptive filename (e.g. `feature-name-verification-YYY-MM-DD.png`)

This step ensures that all features are visually verified and provides documentation of the working state of the application.