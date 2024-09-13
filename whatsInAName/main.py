#Alec George raid: what's in a name?
def calculate_area(length, width):
    area = length * width
    return area

def calculate_volume(length, width, height):
    base_area = calculate_area(length, width)
    volume = base_area * height
    return volume

rectangle_length = 5
rectangle_width = 3
rectangle = calculate_area(rectangle_length, rectangle_width)
print(f"The rectangle's area is: {rectangle} square units.")

rectangular_prism_length = 4
rectangular_prism_width = 6
rectangular_prism_height = 2
rectangular_prism = calculate_volume(rectangular_prism_length, rectangular_prism_width, rectangular_prism_height)
print(f"The rectangular prism's volume is: {rectangular_prism} cubic units.")