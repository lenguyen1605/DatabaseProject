from typing import List, Optional

from pydantic import BaseModel


class Cat(BaseModel):
    id: int = 0
    link: str = None

    class Config:
        orm_mode = True
