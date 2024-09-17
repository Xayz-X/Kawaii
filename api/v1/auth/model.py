from pydantic import BaseModel


class AuthCredential(BaseModel):
    name: str
    email: str
    
