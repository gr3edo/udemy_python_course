import shelve

# with shelve.open('ShelfTest') as fruit:       # with closes himself
fruit = shelve.open('ShelfTest')                # should be closed after finish with file
# fruit['orange'] = 'a sweet, orange citrus fruit'
# fruit['apple'] = 'good for making cider'
# fruit['lemon'] = 'a sour, yellow citrus fruit'
# fruit['grape'] = 'a small sweet fruit growing on bunches'
# fruit['lime'] = 'a sour, green citrus fruit'

# print(fruit['lemon'])
# print(fruit['grape'])
#
# fruit['lime'] = 'great with tequila'
#
# for snack in fruit:
#     print(snack + ': ' + fruit[snack])

# while True:
#     dict_key = input("PLease, enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We dont have a " + dict_key)
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()
