# Full Stack Travi API Project

## Full Stack Trivia

This project is web application allows users can share their knowledge and play a game about it by answering trivia questions. The task for the project was to createan API and test suite for implementing the following functionality:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

## Full Stack Trivia

### Installing Dependencies

#### Frontend Dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

#### Backend Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Working within a virtual environment is recommended.

Follow instructions to set up virtual enviornment in https://flask.palletsprojects.com/en/2.0.x/installation/

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages in the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql trivia < trivia.sql
```

## Running the Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## Running the server

From within the `backend` directory

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Testing

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.sql
python test_flaskr.py
```

## API Reference

### Getting Started

- Backend Base URL: `http://127.0.0.1:5000/`
- Frontend Base URL: `http://127.0.0.1:3000/`
- Authentication: Authentication or API keys are not used in the project yet.

### Error Handling

Errors are returned as JSON in the following format:<br>

    {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }

The API will return four types of errors:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
- 500 - An error has occured, please try again

### Endpoints

#### GET /

- General: Returns a list categories.
- Sample: `curl http://127.0.0.1:5000/`<br>

		{
			"success": true
		}	
			

#### GET /categories

- General: Returns a list categories.
- Sample: `curl http://127.0.0.1:5000/categories`<br>

		{
			"categories": {
				"1": "Science",
				"2": "Art",
				"3": "Geography",
				"4": "History",
				"5": "Entertainment",
				"6": "Sports",
				"7": "Food",
				"8": "Cosmetics"
			},
			"success": true
		}
		
#### POST /categories

- General: Returns a new created category.
- Sample: `curl --location --request POST 'http://127.0.0.1:5000/categories' \
--header 'Content-Type: application/json' \
--data-raw '{
    "type": "Books"
}'`<br>

        {
			"categories": {
				"1": "Science",
				"2": "Art",
				"3": "Geography",
				"4": "History",
				"5": "Entertainment",
				"6": "Sports",
				"7": "Food",
				"8": "Cosmetics",
				"9": "Books"
			},
			"message": "New category: 'Books' created.",
			"success": true
		}

#### DELETE /categories

- General: Returns a new created category.
- Sample: `curl -X DELETE http://127.0.0.1:5000/categories/9`<br>
		{
			"deleted": 9,
			"message": "Category No.9 Books was successfully deleted",
			"success": true
		}

#### GET /questions

- General:
  - Returns a list questions.
  - Results are paginated in groups of 10.
  - Also returns list of categories and total number of questions.
- Sample: `curl http://127.0.0.1:5000/questions`<br>

        {
			"current_category": {
				"1": "Science",
				"2": "Art",
				"3": "Geography",
				"4": "History",
				"5": "Entertainment",
				"6": "Sports",
				"7": "Food",
				"8": "Cosmetics"
			},
			"questions": [
				{
					"answer": "Taipei",
					"category": 3,
					"creator": "Amy",
					"difficulty": 2,
					"id": 24,
					"question": "The capital of Taiwan(ROC)"
				},
				{
					"answer": "Scarab",
					"category": 4,
					"creator": "Max",
					"difficulty": 4,
					"id": 23,
					"question": "Which dung beetle was worshipped by the ancient Egyptians?"
				},
				{
					"answer": "Blood",
					"category": 1,
					"creator": "Argy",
					"difficulty": 4,
					"id": 22,
					"question": "Hematology is a branch of medicine involving the study of what?"
				},
				{
					"answer": "Alexander Fleming",
					"category": 1,
					"creator": "Argy",
					"difficulty": 3,
					"id": 21,
					"question": "Who discovered penicillin?"
				},
				{
					"answer": "The Liver",
					"category": 1,
					"creator": "Argy",
					"difficulty": 4,
					"id": 20,
					"question": "What is the heaviest organ in the human body?"
				},
				{
					"answer": "Jackson Pollock",
					"category": 2,
					"creator": "Argy",
					"difficulty": 2,
					"id": 19,
					"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
				},
				{
					"answer": "One",
					"category": 2,
					"creator": "Max",
					"difficulty": 4,
					"id": 18,
					"question": "How many paintings did Van Gogh sell in his lifetime?"
				},
				{
					"answer": "Mona Lisa",
					"category": 2,
					"creator": "Argy",
					"difficulty": 3,
					"id": 17,
					"question": "La Giaconda is better known as what?"
				},
				{
					"answer": "Escher",
					"category": 2,
					"creator": "Sylvia",
					"difficulty": 1,
					"id": 16,
					"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
				},
				{
					"answer": "Agra",
					"category": 3,
					"creator": "Emily",
					"difficulty": 2,
					"id": 15,
					"question": "The Taj Mahal is located in which Indian city?"
				}
			],
			"success": true,
			"total_questions": 21
		}

#### DELETE /questions/\<int:id\>

- General:
  - Deletes a question by id using url parameters.
  - Returns id of deleted question upon success.
- Sample: `curl http://127.0.0.1:5000/questions/4 -X DELETE`<br>

        {
			"deleted": 4,
			"id": 4,
			"message": "Question No.4 What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat? was successfully deleted",
			"success": true
		}

#### POST /questions

This endpoint either creates a new question or returns search results.

1. If <strong>no</strong> search term is included in request:

- General:
  - Creates a new question using JSON request parameters.
  - Returns JSON object with newly created question, as well as paginated questions.
- Sample: `curl --location --request POST 'http://127.0.0.1:5000/questions' \
--header 'Content-Type: application/json' \
--data-raw '{
          "question": "Total Harry Potter Novels",
          "answer": "7",
          "difficulty": 1,
          "category": 5,
          "creator": "Trivis"
        }'`<br>

		{
			"message": "New question: Total Harry Potter Novels created.",
			"questions": [
				{
					"answer": "7",
					"category": 5,
					"creator": "Trivis",
					"difficulty": 1,
					"id": 137,
					"question": "Total Harry Potter Novels"
				},
				{
					"answer": "Taipei",
					"category": 3,
					"creator": "Amy",
					"difficulty": 2,
					"id": 24,
					"question": "The capital of Taiwan(ROC)"
				},
				{
					"answer": "Scarab",
					"category": 4,
					"creator": "Max",
					"difficulty": 4,
					"id": 23,
					"question": "Which dung beetle was worshipped by the ancient Egyptians?"
				},
				{
					"answer": "Blood",
					"category": 1,
					"creator": "Argy",
					"difficulty": 4,
					"id": 22,
					"question": "Hematology is a branch of medicine involving the study of what?"
				},
				{
					"answer": "Alexander Fleming",
					"category": 1,
					"creator": "Argy",
					"difficulty": 3,
					"id": 21,
					"question": "Who discovered penicillin?"
				},
				{
					"answer": "The Liver",
					"category": 1,
					"creator": "Argy",
					"difficulty": 4,
					"id": 20,
					"question": "What is the heaviest organ in the human body?"
				},
				{
					"answer": "Jackson Pollock",
					"category": 2,
					"creator": "Argy",
					"difficulty": 2,
					"id": 19,
					"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
				},
				{
					"answer": "One",
					"category": 2,
					"creator": "Max",
					"difficulty": 4,
					"id": 18,
					"question": "How many paintings did Van Gogh sell in his lifetime?"
				},
				{
					"answer": "Mona Lisa",
					"category": 2,
					"creator": "Argy",
					"difficulty": 3,
					"id": 17,
					"question": "La Giaconda is better known as what?"
				},
				{
					"answer": "Escher",
					"category": 2,
					"creator": "Sylvia",
					"difficulty": 1,
					"id": 16,
					"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
				}
			],
			"success": true,
			"total_questions": 22
		}

2. If search term <strong>is</strong> included in request:

- General:
  - Searches for questions using search term in JSON request parameters.
  - Returns JSON object with paginated matching questions.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "1990"}'`<br>

        {
			"questions": [
				{
					"answer": "Edward Scissorhands",
					"category": 5,
					"creator": "Sylvia",
					"difficulty": 3,
					"id": 6,
					"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
				}
			],
			"success": true,
			"total_questions": 1
		}

#### GET /categories/\<int:id\>/questions

- General:
  - Gets questions by category id using url parameters.
  - Returns JSON object with paginated matching questions.
- Sample: `curl http://127.0.0.1:5000/categories/1/questions`<br>

        {
			"current_category": "Science",
			"questions": [
				{
					"answer": "Skin",
					"category": 1,
					"creator": "Max",
					"difficulty": 3,
					"id": 1,
					"question": "Biggest organ in human body?"
				},
				{
					"answer": "The Liver",
					"category": 1,
					"creator": "Argy",
					"difficulty": 4,
					"id": 20,
					"question": "What is the heaviest organ in the human body?"
				},
				{
					"answer": "Alexander Fleming",
					"category": 1,
					"creator": "Argy",
					"difficulty": 3,
					"id": 21,
					"question": "Who discovered penicillin?"
				},
				{
					"answer": "Blood",
					"category": 1,
					"creator": "Argy",
					"difficulty": 4,
					"id": 22,
					"question": "Hematology is a branch of medicine involving the study of what?"
				}
			],
			"success": true,
			"total_questions": 4
		}

#### POST /quizzes

- General:
  - Allows users to play the quiz game.
  - Uses JSON request parameters of category and previous questions.
  - Returns JSON object with random question not among previous questions.
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}'`<br>

        {
            "question": {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            },
            "success": true
        }

## Authors

Sylvia Yue authored the API (`__init__.py`), test suite (`test_flaskr.py`), parts of (`FormCView.js`) and this README.<br>
All other project files, including the models and frontend, were created by [Udacity](https://www.udacity.com/) as a project template for the [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).
