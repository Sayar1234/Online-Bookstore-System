from fastapi import FastAPI

app = FastAPI(title = "Online BookStore API")

@app.get("/")
def root():
    return {"message": "Bookstore API is functioning"}