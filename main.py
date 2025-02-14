from fastapi import FastAPI

app = FastAPI()  # ✅ This line must be present!

@app.get("/")
def home():
    return {"message": "API is running"}
