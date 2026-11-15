import os

from dotenv import load_dotenv
from mongoengine import connect

load_dotenv()

mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_host = os.getenv("MONGO_HOST")
mongo_db = os.getenv("MONGO_DB")

connection = connect(
    db=mongo_db,
    host=f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_host}/{mongo_db}?retryWrites=true&w=majority"
)