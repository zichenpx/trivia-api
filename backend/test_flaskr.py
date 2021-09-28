import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category



class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format("", "", "localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        # self.new_question = {
        #   "question": "The capital of Taiwan(ROC)",
        #   "answer": "Taipei",
        #   "difficulty": 1,
        #   "category": 3
        # }

        self.test_quizz = {
            "previous_questions": [2],
            "quiz_category": {
                "id": 3
            }
        }

        self.new_question = {
          "question": "Two Famous French Food",
          "answer": "Cheese, Wine",
          "difficulty": 1,
          "category": 3,
          "creator": "Amy"
        }

        self.new_question_missing_data = {
          "question": "Two Famous French Food",
          "answer": "Cheese, Wine",
          "difficulty": 1,
          "creator": "Lily"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginated_questions(self):
        response = self.client().get("/questions")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_404_request_beyond_vaid_page(self):
        response = self.client().get("/questions?page=1000")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_get_categories(self):
        response = self.client().get("/categories")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_questions_by_category(self):
        response = self.client().get("/categories/2/questions")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)

        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        self.assertEqual(data["current_category"], "Art")

    def test_400_if_questions_by_category_fails(self):
        response = self.client().get("/categories/10000/questions")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_create_question(self):
        questions_before = Question.query.all()

        response = self.client().post("/questions", json=self.new_question)
        data = json.loads(response.data)
        questions_after = Question.query.all()

        # check whether the question was created
        # question = Question.query.filter_by(id=data["created"]).one_or_none()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["success"], True)

        self.assertTrue(len(questions_after) - len(questions_before) == 1)
        # check exist
        # self.assertIsNotNone(question)

    def test_422_create_question_with_no_data(self):
        questions_before = Question.query.all()

        response = self.client().post("/questions", json=self.new_question_missing_data)
        data = json.loads(response.data)

        questions_after = Question.query.all()

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(len(questions_after) == len(questions_before))
        self.assertEqual(data["message"], "unprocessable")

    def test_422_create_question_with_no_data(self):
        questions_before = Question.query.all()

        response = self.client().post("/questions", json={})
        data = json.loads(response.data)

        questions_after = Question.query.all()

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(len(questions_after) == len(questions_before))
        self.assertEqual(data["message"], "unprocessable")

    def test_delete_question(self):
        questions_before = Question.query.all()
        q_id = 4

        response = self.client().delete("/questions/{}".format(q_id))
        data = json.loads(response.data)
        questions_after = Question.query.all()
        question = Question.query.filter(Question.id == 1).one_or_none()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], q_id)
        self.assertTrue(len(questions_before) - len(questions_after) == 1)
        self.assertEqual(question, None)

    def test_404_delete_question_fail(self):
        response = self.client().delete("/questions/1912")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertIn("success", data)
        self.assertFalse(data["success"], True)

    def test_search_questions(self):
        response = self.client().post("/questions", json={"searchTerm": "1990"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        
    def test_404_if_search_questions_fails(self):
        response = self.client().post("/questions", json={"searchTerm": "a5b6c7d8e9f0"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_play_quizzes(self):
        response = self.client().post("/quizzes", json=self.test_quizz)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("question", data)
        self.assertEqual((data["question"]["category"]), self.test_quizz["quiz_category"]["id"])
        self.assertTrue(data["question"], True)

    def test_404_play_quizzes(self):
        response = self.client().post("/quizzes", json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertIn("success", data)
        self.assertFalse(data["success"], True)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()