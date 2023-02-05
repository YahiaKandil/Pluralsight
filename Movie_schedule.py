current_movies =   {'The Grinch':'11:00 am',
                    'Runolph':'1:00 pm',
                    'Frosty the snowman': '3:00 pm',
                    'Christmas Vacation':'5:00 pm'}

print("\nWe're showing the following movies:\n")

for key in current_movies:
    print(key)

movie = input("\nWhat movie would you like the showtime for?\n\n")

showtime = current_movies.get(movie)

if showtime == None:
    print(' ')
    print("The requested showtime isn't playing\n\n")

else:
    print(' ')
    print(movie, "is playing at", showtime, "\n")
