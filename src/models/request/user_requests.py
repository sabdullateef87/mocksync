from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator

class CreateUser(BaseModel):
    username : str = Field(min_length=10, max_length=20)
    email : EmailStr
    password : str = Field(min_length=8, max_length=50)
    confirmPassword : str = Field(min_length=8, max_length=50)
    
    
    
    @field_validator('username')
    @classmethod
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValidationError('Username must be alphanumeric')
        return value
        
    @field_validator('confirmPassword')
    @classmethod
    def validate_password(cls, value, values):
        
        print("Debugging -> ", value, values.data.get("password"))
        
        if values.data.get('password') != None:
            password = values.data.get('password')
            if value != password:
                raise ValueError('Passwords do not match')
        return value