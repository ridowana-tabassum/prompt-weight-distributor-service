from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import sqlite3

app = FastAPI()


def distribute_weights(prompt, prompt_seed):
    for seed in prompt_seed:
        seed_parts = seed.split(':')
        if len(seed_parts) == 2 and seed_parts[1].startswith('(') and seed_parts[1].endswith(')'):
            word = seed_parts[0]
            weight = seed_parts[1][1:-1]
            prompt = prompt.replace(word, f"({word}:{weight})")
        elif seed.startswith('(') and seed.endswith(')'):
            seed = seed[1:-1]
            prompt = prompt.replace(seed.split(':')[0], seed)
    return prompt


@app.post("/weight-me")
def weight_me(request_data: dict):
    print(request_data)
    if request_data is None or "prompt" not in request_data or "prompt_seed" not in request_data:
        raise HTTPException(status_code=400, detail="Invalid request format")

    prompt = request_data["prompt"]
    prompt_seed = request_data["prompt_seed"]

    # Validate request data
    if not isinstance(prompt, str) or not isinstance(prompt_seed, list):
        raise HTTPException(status_code=400, detail="Invalid request data format")

    # Distribute weights
    weighted_prompt = distribute_weights(prompt, prompt_seed)

    return JSONResponse(content={"result": weighted_prompt})


@app.get("/")
def index():
    return {"message": "Welcome to the Prompt Weight Distributor Service!"}


if __name__ == "__main__":
    # Initialize SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create table for prompts if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT,
            prompt_seed TEXT
        )
    ''')
    conn.commit()

    # Start the FastAPI server
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
