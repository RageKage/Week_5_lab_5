from peewee import *


db = SqliteDatabase('cats.sqlite')



class Cat(Model): # this creates a cat table with three columns
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db
        
        
    def __str__(self):
        return f'{self.name} is a {self.color} cat and is {self.age} years old.'
    # peewee will create the database for us 


db.connect()
db.create_tables([Cat])


Cat.delete().execute() # deletes all the cats in the database

zoe = Cat(name='Zoe', color='gray', age=3)
zoe.save()

holly = Cat(name='Holly', color='black', age=5)
holly.save()

fluffy = Cat(name='Fluffy', color='white', age=1)
fluffy.save()


cats = Cat.select() # this is a query that selects all the cats in the database
print("")
print("")
cats = Cat.select()
for cat in cats:
    print(cat)
    
fluffy.age = 2
fluffy.save()
print("")
print("Fluffy's age is now 2")
cats = Cat.select() 
for cat in cats:
    print(cat)
    
Cat.update(age=4).where(Cat.name == 'Holly').execute()

print("Holly's age is now 4")
print("")
cats = Cat.select()
for cat in cats:
    print(cat)

    

petter = Cat(name = 'Petter', color= "red", age= 3)
petter.save()


cat_who_are_3 = Cat.select().where(Cat.age == 3)

print("")
print("")
for cat in cat_who_are_3:
    print(cat)
    



search_cat_name = Cat.select().where(Cat.name.contains('l'))
print("")
print("")
for cat in search_cat_name:
    print(cat)
    
    




    
find = Cat.get_or_none(Cat.name == 'Petter')
print("")
print("")
print(find)


find_2 = Cat.get_or_none(Cat.name == 'Peter')
print("")
print("")
print(find_2)


# TOTAL CAT IN DB

total = Cat.select().count()
print("")
print("")
print(total)



num_of_cats_over_3 = Cat.select().where(Cat.age >= 3).count()
print("")
print("")
print(num_of_cats_over_3)



cats_by_name = Cat.select().order_by(Cat.name)

# use desc to reverse order

# you can order by age
print("")
print("")
print(list(cats_by_name))



first_three_cats = Cat.select().order_by(Cat.name).limit(3)
print("")
print("")
print(list(first_three_cats))



