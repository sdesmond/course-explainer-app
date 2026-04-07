---
name: Course Explainer App Structure
description: Key architectural facts about the Flask app that inform design decisions — nav pattern, CSS approach, route registration style
type: project
---

The app is a plain CSS Flask app (no Bootstrap, no Tailwind). Styles live in `src/static/css/styles.css`. The color palette is dark slate header (`#37474f`/`#35424a`), white content cards, light grey page background (`#f4f5f6`).

The base template is `src/templates/layout.html`. All pages extend it via Jinja2 `{% extends %}`. Nav links are hand-authored `<li>` items inside `.main-nav` in `layout.html`.

Routes are registered in `src/app.py` via `app.add_url_rule()`. View functions live in `src/views.py`. There is no database — data is hardcoded in `src/models.py`.

The `.container` class gives pages a `max-width: 1000px`, centered, white, with a subtle box shadow.

**Why:** Knowing the CSS approach avoids recommending Bootstrap classes or icon font CDN links that conflict with the plain-CSS stack.

**How to apply:** All new pages extend `layout.html`, add a nav `<li>` in that file, register a route in `app.py`, and add a view function in `views.py`. New styles go into the existing `styles.css` following the same flat-class naming convention.
