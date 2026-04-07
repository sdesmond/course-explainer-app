from flask import render_template, abort, request, redirect, url_for
from models import courses

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    try:
        course = courses[int(course_id) - 1]
    except (IndexError, ValueError):
        abort(404)
    return render_template('course.html', course=course)

def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        if name and email and message:
            return redirect(url_for('contact', success=1))
        return render_template('contact.html', success=False, error=True,
                               name=name, email=email, message=message)
    success = request.args.get('success') == '1'
    return render_template('contact.html', success=success, error=False,
                           name='', email='', message='')