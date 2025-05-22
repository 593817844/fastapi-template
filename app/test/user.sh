# 创建用户
curl -X POST http://localhost:8000/users/create \
     -H "Content-Type: application/json" \
     -d '{"username": "test2", "email": "test1@example.com"}'

# 获取用户
curl http://localhost:8000/users/test2
