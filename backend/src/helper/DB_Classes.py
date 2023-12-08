import datetime
from peewee import *
from src.helper.config import get_config

# Get the database path from the configuration file and create a SqliteDatabase instance
db = SqliteDatabase(get_config()["database"]["path"])


class BaseModel(Model):
    """
    BaseModel is a base class for all models in the application.
    It sets the database instance to be used by all child models.
    """

    class Meta:
        database = db


class Chat(BaseModel):
    """
    Chat is a model representing a chat in the application.
    It inherits from the BaseModel and thus uses the database instance set in BaseModel.

    Attributes:
        cost (FloatField): The cost of the chat. Defaults to 0.
        tokens (IntegerField): The number of tokens in the chat. Defaults to 0.
        start_time (DateTimeField): The start time of the chat. Defaults to the current time.
    """
    cost = FloatField(default=0)
    tokens = IntegerField(default=0)
    start_time = DateTimeField(default=datetime.datetime.now)


def get_cost_of_current_month():
    """
    This function calculates the total cost of all chats that started in the current month.

    Returns:
        float: The total cost of all chats in the current month.
    """
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


# Connect to the database and create the tables for the models
db.connect()
db.create_tables([Chat])
