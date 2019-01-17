imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda

print("The artist is: " + artist)
print("The title of album is: " + title)
print("The year is: " + str(year))

for item in tracks:
    track_number, track_title = item
    print("\tNo {}\t{}".format(track_number, track_title))
