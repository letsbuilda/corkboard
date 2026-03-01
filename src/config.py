from pathlib import Path
from pydantic import BaseModel, Field

class UploadConfiguration(BaseModel):
    max_size: int
    allowed_types: set[str] # this is for MIME types, i'm planning to add support to the sacred gifs later

class StorageConfiguration(BaseModel):
    img_path: Path
    db_path: Path

class MainConfiguration(BaseModel):
    host: str
    port: int = Field(ge=1, le=65535)
    upload: UploadConfiguration
    storage: StorageConfiguration
