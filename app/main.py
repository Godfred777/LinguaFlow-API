from fastapi import FastAPI

app = FastAPI()
app.title = "LinguaFlow API"
app.description = "API for LinguaFlow, a Machine Learning based Translator."
app.version = "0.1.0"
app.license_info = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT",
}
app.include_router()

@app.get("/")
async def root():
    return {"message": "Hello World"}