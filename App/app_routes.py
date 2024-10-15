#!/usr/bin/env python3

from App.app_forms import RegistrationForm, LoginForm
from App.app_utils import hash_password
from App import app, login_manager
from App.quiz_models import db, Quiz, Question, Option, User
from flask_login import current_user, login_user, login_required, logout_user
from flask import redirect, url_for, request, jsonify, render_template

@app.route("/", strict_slashes=False)
def index():
    # Show quizzes if logged in, otherwise redirect to login page
    if current_user.is_authenticated:
        quizzes = Quiz.query.all()
        return render_template("index.html", quizzes=quizzes)
    return redirect(url_for("login"))

@app.route("/quiz", strict_slashes=False)
@login_required
def quiz():
    # Display all available quizzes
    quizzes = Quiz.query.all()
    return render_template("quiz_home.html", quizzes=quizzes)

@app.route("/quiz/<int:quiz_id>", strict_slashes=False)
@login_required
def display_quiz(quiz_id):
    # Fetch a quiz by its ID and prepare it for the template
    quiz = Quiz.query.get_or_404(quiz_id)
    quiz_dict = {
        "title": quiz.title,
        "questions": [
            {
                "content": question.content,
                "options": [option.content for option in question.options],
                "answer": [option.content for option in question.options if option.is_correct],
            }
            for question in quiz.questions
        ],
    }
    return render_template("start_quiz.html", quiz=quiz_dict)

@app.route("/quiz/<int:quiz_id>/delete", methods=["POST"], strict_slashes=False)
@login_required
def delete_quiz(quiz_id):
    # Delete a quiz and its related questions
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    for question in questions:
        db.session.delete(question)
    
    db.session.delete(quiz)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"], strict_slashes=False)
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data

        # Check if the username is taken
        if User.query.filter_by(username=username).first():
            return render_template("signup.html", form=form, error="Username already exists")
        
        # Add new user to the database
        new_user = User(username=username, password=hash_password(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("signup.html", form=form)

@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        # Check credentials and log user in
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("index"))
        return jsonify({"error": "Invalid credentials"}), 401

    return render_template("signin.html", form=form)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))

@app.route("/users", strict_slashes=False)
@login_required
def user():
    # Display all users as JSON
    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username, "created_at": user.created_at, "updated_at": user.updated_at} for user in users]
    return jsonify(users_list)

@app.route("/user/dashboard", methods=["GET"])
@login_required
def user_dashboard():
    user = current_user
    return render_template("dashboard.html", user=user, attempts=user.attempts)

@app.route("/forgot-password", strict_slashes=False)
def forgot_password():
    return jsonify({"message": "Forgot password", "status": "not implemented"})

@app.route("/logout", strict_slashes=False)
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
