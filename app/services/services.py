from app.models.models import User

async def create_user(session, user):
    new_user = User(user=user.user)