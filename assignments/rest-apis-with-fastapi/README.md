# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. In this assignment, you will learn how to create API endpoints, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI project and implement endpoints for a small task manager API. Your API should support reading data and adding new tasks.

#### Requirements
Completed program should:

- Create a FastAPI app that runs locally.
- Add a `GET /` endpoint that returns a welcome JSON message.
- Add a `GET /tasks` endpoint that returns a list of tasks.
- Add a `POST /tasks` endpoint that accepts task data and adds it to memory.
- Return responses in valid JSON format.


### 🛠️	Validate Input and Handle Errors

#### Description
Improve your API by validating user input and returning clear error messages when invalid data is sent.

#### Requirements
Completed program should:

- Use a Pydantic model to validate incoming task data.
- Require each task to include a title.
- Return an appropriate HTTP error when required fields are missing.
- Return status codes that match the operation outcome (for example, `200` for success and `400` or `422` for invalid input).
- Keep the API behavior predictable and easy to test.
