from fastapi import FastAPI
from .translations.routes import router as translations_router

app = FastAPI()
app.title = "LinguaFlow API"
app.description = "API for LinguaFlow, a Machine Learning based Translator."
app.version = "0.1.0"
app.license_info = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT",
}
app.include_router(translations_router, prefix="/translations", tags=["translations"])

@app.get("/")
async def root():
    return {"message": "Hello World"}