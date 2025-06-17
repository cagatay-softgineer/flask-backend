# models.py
from pydantic import BaseModel, EmailStr, constr


class RegisterRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=6)  # type: ignore


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserIdRequest(BaseModel):
    user_id: str

class UserEmailRequest(BaseModel):
    user_email: EmailStr