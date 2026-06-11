from flask import Blueprint, render_template, request, redirect

from flask_login import login_required, current_user

from extensions import db
from models.note import Note


notes = Blueprint("notes", __name__)


# 📌 показать и создать заметки
@notes.route("/notes", methods=["GET", "POST"])
@login_required
def notes_page():

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        new_note = Note(
            title=title,
            content=content,
            user_id=current_user.id
        )

        db.session.add(new_note)
        db.session.commit()

        return redirect("/notes")

    user_notes = Note.query.filter_by(user_id=current_user.id).all()

    return render_template("notes.html", notes=user_notes)


# 🗑 удалить заметку
@notes.route("/notes/delete/<int:note_id>")
@login_required
def delete_note(note_id):

    note = Note.query.get(note_id)

    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()

    return redirect("/notes")