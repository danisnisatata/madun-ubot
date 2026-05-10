from PyroUbot.core.database import mongo_client

# Pastikan nama database lu sesuai (biasanya "ubot_database")
db = mongo_client["ubot_database"]
served_users_db = db["served_users"]

async def add_served_user(user_id: int):
    user = await served_users_db.find_one({"user_id": user_id})
    if user:
        return
    return await served_users_db.insert_one({"user_id": user_id})

async def get_served_users():
    users_list = []
    async for user in served_users_db.find():
        users_list.append(user)
    return users_list
    