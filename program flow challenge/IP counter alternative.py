ipAddress = input("Please, add an IP address: ")
if ipAddress and ipAddress[-1] != ".":
    ipAddress += "."

segment = 1
segment_length = 0

for character in ipAddress:
    if character == ".":
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
