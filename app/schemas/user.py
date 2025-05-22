from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    """用户基础模式"""
    username: str = Field(min_length=2, max_length=50)
    email: str





class UserResponse(UserCreate):
    """用户响应模式"""
    model_config = {
        "from_attributes": True
    } 