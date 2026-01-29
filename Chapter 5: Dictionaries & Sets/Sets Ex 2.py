# Exercise 2: Comparing Movie Genres
# Your favorite movie genres
my_genres = {"Sci-Fi", "Comedy", "Action", "Thriller", "Horror","Rom-Com","Fantasy"}

# Your friend's favorite movie genres
friend_genres = {"Action", "Drama", "Sci-Fi", "Romance", "Comedy","Rom-Com"}

print(f"My genres: {my_genres}")
print(f"Friend's genres: {friend_genres}\n")

# Find genres you both like (intersection)
common_genres = my_genres.intersection(friend_genres)
print(f"Genres we both like: {common_genres}")

# Find genres I like but my friend doesn't (difference)
my_unique_genres = my_genres.difference(friend_genres)
print(f"Genres I like that my friend doesn't: {my_unique_genres}")

# Find genres my friend likes but I don't (difference in reverse)
friend_unique_genres = friend_genres.difference(my_genres)
print(f"Genres my friend likes that I don't: {friend_unique_genres}")

# Find all genres unique to either of us (symmetric difference)
# This shows genres that are in one set OR the other, but NOT in both
all_unique_to_either = my_genres.symmetric_difference(friend_genres)
print(f"Genres unique to either of us: {all_unique_to_either}")