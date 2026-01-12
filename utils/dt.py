from datetime import datetime, timedelta


class DateUtils:

    @classmethod
    def today(cls, now: datetime):
        return now.replace(hour=0, minute=0, second=0, microsecond=0)

    @classmethod
    def tomorrow(cls, now: datetime):
        return cls.today(now + timedelta(days=1))
