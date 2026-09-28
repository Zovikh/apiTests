from fastapi import FastAPI
import uvicorn



app = FastAPI()

@app.get("/", summary="Root endpoint", description="Returns a welcome message.")
def root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run("main:app")