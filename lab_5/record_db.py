from peewee import *
import sqlite3


db = SqliteDatabase("records.sqlite")


class Record(Model):
    name = CharField()
    Country = CharField()
    catches = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f"{self.name} is from {self.Country} and has {self.catches} catches."


db.connect()
db.create_tables([Record])


class Records:
    def display_all_Records():
        return Record.select()

    def add_record(name, country, catches):
        existing_record = Record.select().where((Record.name == name) & (Record.Country == country) & (Record.catches == catches))
    
        if existing_record:
            print(f"Record for {name} already exists.")
        else:
            new_record = Record(name=name, Country=country, catches=catches)
            new_record.save()
            print(f"Record for {name} created.")



    def search_by_name(name):
        records = []

        for record in Record.select().where(Record.name == name):
            records.append(record)

        return records

    def edit_existing_record(name, country, catches):
        Record.update(Country=country, catches=catches).where(Record.name == name).execute()

    def delete_record(name):
        Record.delete().where(Record.name == name).execute()

