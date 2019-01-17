# Create a program that takes a text and returns list of all characters in the text
# that are not vowels, sorted in alphabetical order

text = "Python is a very powerful language"

result_set = set()

for i in text:
    if i not in "aeiou" and i not in result_set:
        result_set.add(i)

print(sorted(result_set))


# actual solution

vowels = frozenset("aeiou")
final_set = set(text).difference(vowels)

final_list = sorted(final_set)
print(final_list)
