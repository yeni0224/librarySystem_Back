from pydantic import BaseModel

class LibBase(BaseModel):
    title : str
    author : str
    publisher : str
class LibCreate(LibBase):
    pass
class LibUpdate(LibBase):
    pass
class LibOut(LibBase):
    isbn : int
    class Config:
        orm_mode = True