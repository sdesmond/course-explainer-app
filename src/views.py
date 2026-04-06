from flask import render_template, abort
from models import courses

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    try:
        course = courses[int(course_id) - 1]
    except (IndexError, ValueError):
        abort(404)
    return render_template('course.html', course=course)