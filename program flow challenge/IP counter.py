ip = input("Enter IP: ")

number_of_segments = 1
counter = 0
char = ""

for char in ip:
    len_of_segment = 0
    if char != ".":
        counter += 1
    else:
        print("Segment is over. It's length is {}".format(counter))
        counter = 0
        number_of_segments += 1

if char != ".":
    print("Segment is over. It's length is {}".format(counter))
print("There is {} segments".format(number_of_segments))
