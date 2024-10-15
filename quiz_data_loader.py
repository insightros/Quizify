#!/usr/bin/env python3
"""Import Quiz from JSON file"""

import json
from App import app
from App.quiz_models import db, Quiz, Question, Option

def import_quiz_data():
    with app.app_context():
        with open("quizzes.json", "r") as file:
            quizzes = json.load(file)

            for quiz_data in quizzes:
                quiz = Quiz(title=quiz_data["title"])
                db.session.add(quiz)
                db.session.commit()  # Commit after adding quiz to ensure it has an ID

                for question_data in quiz_data["questions"]:
                    question = Question(content=question_data["content"], quiz_id=quiz.id)
                    db.session.add(question)
                    db.session.commit()  # Commit after adding question

                    for option_data in question_data["options"]:
                        option = Option(
                            content=option_data["content"],
                            is_correct=option_data["is_correct"],
                            question_id=question.id,
                        )
                        db.session.add(option)
                    db.session.commit()  # Commit after adding all options for the question

if __name__ == "__main__":
    import_quiz_data()
