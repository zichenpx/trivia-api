import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category



class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.database_path = "postgres://{}:{}@{}/{}".format('USER', 'PASSWORD', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
          'question': 'The capital of Taiwan(ROC)',
          'answer': 'Taipei',
          'difficulty': 1,
          'category': '3'
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
        # get response and load data
        response = self.client().get("/questions")
        data = json.loads(response.data)

        # check status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)

        # check that total_questions and questions return data
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_404_request_beyond_vaid_page(self):
        response = self.client().get('/questions?page=100')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_categories(self):
        response = self.client().get("/categories")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_questions_by_category(self):
        response = self.client().get("/categories/2/questions")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        self.assertEqual(data['current_category'], 'Art')

    def test_400_if_questions_by_category_fails(self):
        response = self.client().get('/categories/10000/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_create_question(self):
        questions_before = Question.query.all()

        # create new question without json data, then load response data
        response = self.client().post('/questions', json=self.new_question)
        data = json.loads(response.data)
        

        questions_after = Question.query.all()

        # check if the question has been created
        question = Question.query.filter_by(id=data['created']).one_or_none()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)

        self.assertTrue(len(questions_after) - len(questions_before) == 1)
        self.assertIsNotNone(question)

    # def test_422_if_question_creation_fails(self):
    #     questions_before = Question.query.all()

    #     # create new question without json data, then load response data
    #     response = self.client().post('/questions', json={})
    #     data = json.loads(response.data)

    #     questions_after = Question.query.all()

    #     self.assertEqual(response.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertTrue(len(questions_after) == len(questions_before))
    #     self.assertEqual(data['message'], 'unprocessable')

    # def test_delete_question(self):
    #     question = Question(question=self.new_question['question'], answer=self.new_question['answer'], category=self.new_question['category'], difficulty=self.new_question['difficulty'])
    #     question.insert()

    #     q_id = question.id
    #     questions_before = Question.query.all()
    #     response = self.client().delete('/questions/{}'.format(q_id))
    #     data = json.loads(response.data)
    #     questions_after = Question.query.all()
    #     question = Question.query.filter(Question.id == 1).one_or_none()

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)

    #     self.assertEqual(data['deleted'], q_id)
    #     self.assertTrue(len(questions_before) - len(questions_after) == 1)
    #     self.assertEqual(question, None)

    # def test_search_questions(self):

    #     response = self.client().post("/questions", json={"searchTerm": "1990"})

    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)

    #     self.assertEqual(len(data["questions"]), 1)
    #     self.assertEqual(data["questions"][0]["id"], 6)

    # def test_404_if_search_questions_fails(self):
    #     response = self.client().post('/questions', json={'searchTerm': 'a5b6c7d8e9f0'})

    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_play_quiz_game(self):
    #     response = self.client().post(
    #         "/quizzes",
    #         json={
    #             "previous_questions": [10],
    #             "quiz_category": {"type": "Sport", "id": "6"},
    #         },
    #     )
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data["question"])

    #     # check the question returns correctly
    #     self.assertEqual(data['question']['category'], 6)
    #     self.assertNotEqual(data['question']['id'], 10)

    # def test_play_quiz_fails(self):
    #     # send post request without json data
    #     response = self.client().post('/quizzes', json={})
    #     data = json.loads(response.data)

    #     # check response status code and message
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'bad request')       

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()