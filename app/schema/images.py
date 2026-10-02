from pydantic import BaseModel


class ImageUploadRequest(BaseModel):
    filename: str
    content_type: str = "image/jpeg"
