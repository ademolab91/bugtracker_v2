from pydantic import BaseModel, EmailStr

"""  Pydantic schemas for authentication  """


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int


class TokenData(BaseModel):
    email: EmailStr
    scopes: list[str] = []


class User(BaseModel):
    email: EmailStr
    name: str
    disabled: bool | None = None
    role: str = None


class UserInDB(User):
    hashed_password: str
