from pydantic import BaseModel
from pydantic import ConfigDict


class UserBase(BaseModel):
    username: str
    foo: str
    bar: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int