# dict & zip combo

names = ['Ven', 'Scott', 'Len']
ages = [22, 321, 34]

for name, age in zip(names, ages):
    print(name, ': ', age)

people = dict(zip(names, ages))
print(people)

print(type(people))
print(type(True))
