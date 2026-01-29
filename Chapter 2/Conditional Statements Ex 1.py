#Exercise 1: Movie Age Check
# checks if a user is old enough to watch a movie.

#taking user input of age and movie rating
user_age=int(input("Enter your age: "))
movie_rating=input("Enter the movie rating (R/PG-13/NC-17/P/PG): ").upper()

# Displaying the age and movie rating
print(f"Checking if user of age {user_age} gets access to watch the movie of rating {movie_rating}...")

print("\n-----Checking Started-----\n")

#applying conditions and displaying suitable outputs
if movie_rating == 'R':
    if user_age >= 17:
        print("Access Granted to watch the 'R' rated movie. Enjoy!")
    else:
        print("Access Denied: 'R' rated movie requires user of age 17 or above.")
elif movie_rating == 'PG-13':
    if user_age >=13:
        print("Access Granted to watch the 'PG-13' rated movie. Enjoy!") 
    else:
        print("Access Denied: 'PG-13' rated movie requires user of age 13 or above.")
elif movie_rating == 'NC-17':
    if user_age >= 18:
        print("Access Granted to watch the 'NC-17' rated movie. Enjoy!")
    else:
        print("Access Denied: 'NC-17' rated movie requires user of age 18 or above.")
else: #for P/PG rated movie
    print("Access Granted to watch the 'G/PG' rated movie. Enjoy!")

print("\n-----Checking Completed-----")