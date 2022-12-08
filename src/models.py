import uuid
from datetime import time

from sqlmodel import Field, SQLModel


class Restaurant(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=False, primary_key=True, index=True)
    name: str = Field(..., nullable=False)
    weekday: int = Field(..., nullable=False)
    open: time = Field(..., nullable=False)
    close: time = Field(..., nullable=False)
