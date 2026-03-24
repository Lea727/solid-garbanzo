from fastapi import FastAPI

app = FastAPI()



@app.get("/helloword")
async def root():
    return {"Hello": "World"}


@app.get("/funçaoteste")
async def funcaoteste():
    return {"O teste": "deu certo"}
