# List in Python

names = []
names.append("Sandro Henrique")
names.append("Isis Daniely")
names.append("Ana Clara")
names.append("Diogo Antunes")
names.append("Maria Cecilia")

# print(names)
# print(names[1:3])

# Dictionary in Python

persons = {'second' : 'Isis', 'third':'Ana', 'first':'Sandro', 'fourth': 'Diogo', 'fifth': 'Ceclia'}

# print(persons['first'])
# print(persons['second'])
# print(persons['third'])
# print(persons['fourth'])
# print(persons['fifth'])

persons['sixth'] = 'Bruce'

# Loops in Python

# for name in names:
#     print(name)
# print("")

# for person in persons:
#     print(person)

# print("")

# for person in persons.keys():
#     print(person)
# print("")

# for person in persons.values():
#     print(person)
# print("")

# for person in persons.items():
#     print(person)
# print("")

# Subconjunto em dicionários

# subconjunto = {chave: persons[chave] for chave in list(persons.keys())[1:3]}

# from itertools import islice

# subconjunto = {chave: persons[chave] for chave in islice(persons.keys(), 1, 3)}

# from collections import OrderedDict

# ordem = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6}

# subconjunto_ordenado = OrderedDict(sorted(persons.items(), key=lambda item: ordem[item[0]]))

# print(subconjunto_ordenado)

# for index in range(0,10):
#     print(index)


# While loop

index = 0
while index < len(names):
    print(names[index])
    index += 1
