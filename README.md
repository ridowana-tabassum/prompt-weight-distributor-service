# Prompt Weight Distributor Service

The Prompt Weight Distributor Service is a web application built using FastAPI and SQLite. It provides an API endpoint that accepts a JSON payload containing a prompt string and a prompt seed array. The service distributes weights in the prompt string based on the specified prompt seed values and returns the weighted prompt as a JSON response.

## Features

- Accepts POST requests to `/weight-me` endpoint with a JSON payload.
- Distributes weights in the prompt string based on the provided prompt seed values.
- Validates the request data and returns an appropriate response for invalid requests.
- Returns the weighted prompt as a JSON response.

## Requirements

- Python 3.6 or higher
- FastAPI
- SQLite


## Usage

1. Start the FastAPI server:


2. Once the server is running, you can access the API endpoints:

- **POST `/weight-me`**: Send a POST request to this endpoint with a JSON payload containing the prompt and prompt seed. The server will distribute weights in the prompt string and return the weighted prompt as a JSON response.

- **GET `/`**: Accessing this endpoint will return a JSON response with a welcome message.

## Example

**Request:**

```json
POST /weight-me
Content-Type: application/json

{
"prompt": "A woman with red lipstick and blue jeans walking down a city street",
"prompt_seed": ["(red lipstick:1.2)", "city", "(blue jeans:0.9)"]
}

HTTP/1.1 200 OK
Content-Type: application/json

{
  "result": "A woman with (red lipstick:1.2) and (blue jeans:0.9) walking down a city street"
}



