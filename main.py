from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Bulk Certificate generator API is running!"}