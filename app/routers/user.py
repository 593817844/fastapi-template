from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.core.redis import redis_client
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", response_model=UserResponse)
async def create_user(user: UserCreate):
    """创建用户"""
    # 检查用户名是否已存在
    if await User.filter(username=user.username).exists():
        raise HTTPException(status_code=500, detail="Username already exists")
    
    # 检查邮箱是否已存在
    if await User.filter(email=user.email).exists():
        raise HTTPException(status_code=500, detail="Email already exists")
    
    # 创建用户并保存到 MySQL
    user_obj = await User.create(
        username=user.username,
        email=user.email
    )
    return UserResponse.model_validate(user_obj)


@router.get("/{username}", response_model=UserResponse)
async def get_user(username: str):
    """获取用户信息"""
    # 1. 先查 Redis
    redis = await redis_client.get_client()
    cached_user = await redis.get(f"user:{username}")
    
    if cached_user:
        return UserResponse.model_validate_json(cached_user)
    
    # 2. Redis 没有，查 MySQL
    user = await User.get_or_none(username=username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 3. 存入 Redis
    user_data = UserResponse.model_validate(user)
    await redis.set(f"user:{username}", user_data.model_dump_json(), ex=300)
    
    return user_data
