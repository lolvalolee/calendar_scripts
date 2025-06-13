from app.social.models import Friend

for item in Friend.get_objects():
    print(item)
