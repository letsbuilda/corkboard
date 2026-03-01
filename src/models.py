from pydantic import BaseModel
from datetime import datetime

class UploadedImage(BaseModel):
    id: str
    filename: str
    content_type: str
    size_bytes: int
    width: int
    height: int
    created_at: datetime
    deletion_token: str
