from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome_mess():
    return {
        "welcome": "hello mohamed"
    }
