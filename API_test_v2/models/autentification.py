from pydantic import Field
from API_test_v2.settings import base_settings
from base_model import BaseModel


class AuthUser(BaseModel):
    email: str = Field(default=base_settings.user.email)
    password: str = Field(default=base_settings.user.password)


class Authentication(BaseModel):
    auth_token: str | None
    user: AuthUser | None = AuthUser()

if __name__ == "__main__":
    print(Settings().dict())