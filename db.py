from peewee import *

db = SqliteDatabase('cinema.db')


class Ticket(Model):
    line = IntegerField()
    seat = IntegerField()
    price = IntegerField()
    type_seat = CharField()

    class Meta:
        database = db
class Film(Model):
    name = TextField()
    duration = IntegerField()

    class Meta:
        database = db

class Session(Model):
    time_start = DateTimeField()
    film = ForeignKeyField(Film)
    price_low = IntegerField()
    price_height = IntegerField()

    class Meta:
        database = db



