from pydantic import BaseModel, Field
import datetime


class Translation(BaseModel):
    id: int = Field(..., description="Unique identifier for the translation")
    text: str = Field(..., description="The translated text")
    source_language: str = Field(..., description="The source language of the text")
    target_language: str = Field(..., description="The target language of the translation")
    created_at: datetime = Field(..., description="The timestamp when the translation was created")
