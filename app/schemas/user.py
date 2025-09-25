from pydantic import BaseModel, EmailStr, field_validator

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    confirm_password: str

    @field_validator("confirm_password")
    def passwords_match(cls, v, values):
        if "password" in values.data and v != values.data["password"]:
            raise ValueError("Passwords do not match")
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True



