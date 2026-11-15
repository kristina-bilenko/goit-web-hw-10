from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField


class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

    meta = {
        "collection": "authors"
    }


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors)
    quote = StringField()

    meta = {
        "collection": "quotes"
    }