import datetime

from peewee import *

from src.helper.config import get_config

db = SqliteDatabase(get_config()["database"]["path"])


class BaseModel(Model):
    class Meta:
        database = db


class Chat(BaseModel):
    cost = FloatField(default=0)
    tokens = IntegerField(default=0)
    start_time = DateTimeField(default=datetime.datetime.now)


def get_cost_of_current_month():
    db_result = db.execute_sql(
        "SELECT SUM(cost) as cost from chat where start_time >= ?",
        (
            str(
                datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                )
            ),
        ),
    ).fetchone()[0]
    if not db_result:
        db_result = 0
    return db_result


db.connect()
db.create_tables([Chat])
