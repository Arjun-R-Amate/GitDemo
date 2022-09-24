from fastapi import FastAPI
app = FastAPI()


@app.get('/api/students')
def index():
    return {"hello":"world"}