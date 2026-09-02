from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"response": "Hello, Welcome to Adomic Arts samin"}

@app.get("/will")
def read_will():
    return {"response": "Hello World"}

@app.get("/ready")
def read_ready():
    return {"response": " Great!, It works!"}
