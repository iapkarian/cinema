from peewee import *

db = SqliteDatabase('cinema.db')


class Ticket(Model):
    line = IntegerField()
    seat = IntegerField()
    price = IntegerField()
    type_seat = CharField()

    class Meta:
        database = db

# class Session(Model):



