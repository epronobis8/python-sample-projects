current_movies = {'The Grinch':'11:00am',
'Ruldolp':'1:00pm',
'Frosty the Snowman':'3:00pm',
'Christmas Vacation':'5:00pm'
}

print("We're showing hte following moves:")
for key in current_movies:
    print(key)
movie = input("What movie would you like the showtime for?\n")

#using get method to pick something from the dictionary based on movie title.
showtime = current_movies.get(movie)
if showtime == None:
    print("The movie isn't playing")
else:
    print(movie, 'is playing at', showtime) 