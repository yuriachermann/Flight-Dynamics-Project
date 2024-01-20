import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def healthcheck():
    return {"CHECK": "Uvicorn server running"}


@app.get('/healthcheck')
def healthcheck():
    return {"Cho Cho": "Welcome to your FastAPI app 🚅"}


@app.get('/route')
def route():

    return ()


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
