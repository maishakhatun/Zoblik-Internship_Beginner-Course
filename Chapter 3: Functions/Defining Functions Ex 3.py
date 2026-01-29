#Exercise 3: Return Statements
#Let's build a function that calculates the area of a rectangle and returns the result, instead of just printing it.

# Exercise 3: Define a function that returns a value
def calculate_rectangle_area(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # This sends both 'area' and 'perimeter' values back

# Use the function and store the result
room_length = 10
room_width = 5
my_room_area, my_room_perimeter = calculate_rectangle_area(room_length, room_width)
print(f"The area of my room is: {my_room_area} square units.")
print(f"The perimeter of my room is: {my_room_perimeter} units.")

# Use the function result in another calculation or print directly
cost_per_sq_unit = 2.5
total_cost = my_room_area * cost_per_sq_unit
print(f"The total cost for flooring is: ${total_cost:.2f}")

# Calculate area for a Zoblik warehouse section
warehouse_section_area, warehouse_section_perimeter = calculate_rectangle_area(50, 20)
print(f"The area of a Zoblik warehouse section is: {warehouse_section_area} square meters.")
print(f"The perimeter of a Zoblik warehouse section is: {warehouse_section_perimeter} meters.")