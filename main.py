from fastapi import FastAPI

app= FastAPI()
@app.get("/")
async def root():
    return 'hola FastApi'

@app.get("/Url")
async def root():
    return {"url_curso":"https://www.google.com"}