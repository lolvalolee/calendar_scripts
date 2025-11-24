from app.profile.models import Profile


def handle():
    profile = Profile.get()
    now = profile.now
