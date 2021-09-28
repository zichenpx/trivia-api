import os
from flask import Flask, request, abort, jsonify
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from sqlalchemy.sql.expression import desc

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, questions):
  page = request.args.get("page", 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in questions]
  current_questions = questions[start:end]
  return current_questions


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  """
  @TODO: Set up CORS. Allow "*" for origins. Delete the sample route after completing the TODOs
  """
  cors = CORS(app, resources={r"/":{"origins": "*"}})


  """
  @TODO: Use the after_request decorator to set Access-Control-Allow
  """
  @app.after_request
  def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,true")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


  """
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  """
  @app.route("/categories")
  def get_categories():
    categories = Category.query.order_by(Category.id.asc()).all()
    categories_dict = {}

    for category in categories:
      # print(categories_dict)
      categories_dict[category.id] = category.type
      # print(categories_dict)
      # print(categories_dict[category.id])

    if (len(categories) == 0):
      return jsonify({
      "success": False,
      "categories": "no categorie were found" 
    }), 404

    result = {
      "success": True,
      "categories": categories_dict
    }

    return jsonify(result), 200




  """
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  """
  @app.route("/questions")
  def get_question():
    error = False
    questions = Question.query.order_by(Question.id.desc()).all()
    total_questions = len(questions)
    current_questions = paginate_questions(request, questions)

    categories = Category.query.order_by(Category.id).all()
    categories_dict = {}
    for category in categories:
      categories_dict[category.id] = category.type

    if (len(current_questions) == 0):
      error = True

    if (error):
      abort(404)

    result = {
      "success": True,
      "total_questions": total_questions,
      "category": categories_dict,
      "questions": current_questions
    }

    return jsonify(result), 200


  """
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  """
  @app.route("/questions/<int:q_id>", methods=["DELETE"])
  def delete_question(q_id):
    question = Question.query.filter(Question.id == q_id).one_or_none()
    if question is None:
      abort(404)
    try:
      question.delete()
    except:
      db.session.rollback()
      abort(422)
    finally:
      db.session.close()
      result = {
        "success": True,
        "id": q_id,
        "deleted": q_id,
        "message": "Question " + str(q_id) + " was successfully deleted"
      }
      return jsonify(result), 201
      
  """
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  """
  """
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  """
  @app.route("/questions", methods=["POST"])
  def create_question():
    data = request.get_json()
    # search for question
    if "searchTerm" in data:
      search_term = data["searchTerm"]
      search = Question.query.filter(Question.question.ilike(f"%{search_term}%")).all()
      total_results = len(search)
      if (len(search) !=0):
        current_results = paginate_questions(request, search)
        result = {
          "success": True,
          "results": current_results,
          "total_results": total_results,
        }
        return jsonify(result), 200
      else:
        abort(404)

    # create a new question
    else:
      # if data["question"] is None:
      #   abort(422)
      if (("question" not in data) or ("answer" not in data) or ("difficulty" not in data) or ("category" not in data) or ("creator" not in data)):
        abort(422)

      question = data.get("question", "")
      answer = data.get("answer", "")
      difficulty = data.get("difficulty", "")
      category = data.get("category", "")
      creator =data.get("creator", "")

      if ((question == "") or (answer == "") or (difficulty == "") or (category == "") or (creator == "")):
        abort(422)

      try: 
        new_question = Question(
          question = question,
          answer = answer,
          difficulty = difficulty,
          category = category,
          creator = creator,
        )
        new_question.insert()
      except Exception:
        db.session.rollback()
        # print(exc.info())
        abort(500)
      finally:
        db.session.close()
        result = {
          "success": True,
          "message": "New question: " + question + " created."
        }
        return jsonify(result), 201


  """
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  """
  @app.route("/categories/<int:c_id>/questions", methods=["GET"])
  def get_question_by_categories(c_id):
    category = Category.query.filter(Category.id == c_id).one_or_none()

    if category is None:
      abort(400)

    questions = Question.query.filter(Question.category == c_id).all()
    current_questions = paginate_questions(request, questions)
    total_questions = len(questions)
    result = {
      "success": True,
      "questions": current_questions,
      "total_questions": total_questions,
      "current_category": category.type,
    }
    return jsonify(result), 200


  """
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  """
  @app.route("/quizzes", methods=["POST"])
  def play_quiz():
    data = request.get_json(force=True)
    # print("print data: ")
    # print(data)
    # print("print data type: ")
    # print(type(data))

    if "previous_questions" not in data \
        or "quiz_category" not in data \
        or "id" not in data["quiz_category"]:
      abort(404)
    # test_404_play_quizzes 出現 TypeError: "NoneType" object is not subscriptable, 
    # 將傳遞的值(data)先經判斷是否存在後，再儲存至變數之中。
    previous_questions = data.get("previous_questions")
    quiz_category = data.get("quiz_category")
    quiz_category_id = quiz_category["id"]

    try:
      questions_rest = Question.query.filter(Question.id.notin_(previous_questions))

      if quiz_category_id:
        questions = questions_rest.filter_by(category=quiz_category_id).all()
      else:
        abort(404)
        
      next_question = random.choice(questions).format()

      result = {
        "success": True,
        "question": next_question,
      }
      return jsonify(result), 200
    
    except:
      abort(500)

  """
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  """
  @app.errorhandler(404)
  def not_found(error):
    return (
        jsonify({"success": False, "error": 404, "message": "resource not found"}),
        404,
    )

  @app.errorhandler(422)
  def unprocessable(error):
    return (
        jsonify({"success": False, "error": 422, "message": "unprocessable"}),
        422,
    )

  @app.errorhandler(500)
  def unprocessable(error):
    return (
        jsonify({"success": False, "error": 500, "message": "An error has occured, please try again"}),
        500,
    )

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({"success": False, "error": 400, "message": "bad request"}), 400
  
  return app