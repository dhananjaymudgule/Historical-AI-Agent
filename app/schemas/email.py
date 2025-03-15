from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    email: EmailStr

class OTPRequest(BaseModel):
    email: EmailStr
    otp: str

class EmailResponse(BaseModel):
    message: str
