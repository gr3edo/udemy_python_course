import shelve

books = shelve.open("book")
books["recipies"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_on_toast": ["beans", "bread"],
                     "scrambled eggs": ["eggs", "butter", "milk"],
                     "soup": ["tin of soup"],
                     "pasta": ["pasta", "cheese"]}
books["maintance"] = {"stuck": ["oil"],
                      "loose": ["gaffer tape"]}

print(books["recipies"])
# print(books["recipies"]["scrambled eggs"])
#
# print(books["maintance"]["loose"])
books.close()
