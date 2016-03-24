from peewee import *

db = SqliteDatabase('cinema.db')


class Ticket(Model):

    line = IntegerField()
    seat = IntegerField()
    price = IntegerField()
    type_seat = CharField()

    class Meta:
        database = db

#
# class Pet(Model):
#     owner = ForeignKeyField(Person, related_name='pets')
#     name = CharField()
#     animal_type = CharField()
#
#     class Meta:
#         database = db


