from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Meeting, User
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        title = request.form.get("meeting")
        topic = request.form.get("topic")
        attendees = request.form.get("absentees")
        raised_by = request.form.get("raised_by")
        actions_required = request.form.get("actions_required")
        actioned_by = request.form.get("actioned_by")
        subsequent_information = request.form.get("subsequent_information")
        end_time = request.form.get("end_time")

        if len(title) < 1:
            flash("Please enter a title.", category="error")
        elif len(topic) < 1:
            flash("Please enter a topic.", category="error")
        elif len(attendees) < 1:
            flash("Please enter the attendees.", category="error")
        elif len(raised_by) < 1:
            flash("You cannot leave the raised by field empty.", category="error")
        elif len(actions_required) < 1:
            flash("Please enter the actions required.", category="error")
        elif len(actioned_by) < 1:
            flash("Please enter the actioned by.", category="error")
        elif len(subsequent_information) < 1:
            flash("Please enter any subsequent information.", category="error")
        elif len(end_time) < 1:
            flash("Please specify the date of completion.", category="error")
        else:
            # add to database
            new_meeting = Meeting(
                title=title,
                topic=topic,
                attendees=attendees,
                raised_by=raised_by,
                actions_required=actions_required,
                actioned_by=actioned_by,
                subsequent_information=subsequent_information,
                end_time=end_time,
                user_id=current_user.id,
            )
            db.session.add(new_meeting)
            db.session.commit()
            flash("Meeting added successfully.", category="success")
    return render_template("home.html", user=current_user)


# function for delete modal
@views.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete_meeting(id):
    meeting = Meeting.query.get_or_404(id)
    db.session.delete(meeting)
    db.session.commit()
    return render_template("minutes.html", user=current_user)


# @views.route("/delete-note", methods=["POST"])
# def delete_note():
#    note = json.loads(request.data)
#    noteId = note["noteId"]
#    note = Note.query.get(noteId)
#    if note:
#       if note.user_id == current_user.id:
#           db.session.delete(note)
#            db.session.commit()
#    return jsonify({})
