import math as m
import matplotlib.pyplot as plt
from utils import *

def pi_monte_carlo(circle, square, number_points):
    pi_values = []
    count_points_in_circle = 0

    for i in range(1, number_points + 1):
        point = square.random_point()
        if circle.is_inside(point):
            count_points_in_circle += 1

        # Calculate the ratio of points inside the circle to total points
        proportion_circle = count_points_in_circle / i
        area_square = square.area()

        # Estimate Pi using the Monte Carlo method
        pi_calculated = (area_square * proportion_circle) / (circle.radius**2)
        pi_values.append((i, pi_calculated))

    return pi_calculated, m.pi, pi_values

# Plot function
def plot_points(values_points, expeted_result):
    x = [p[0] for p in values_points]
    y = [p[1] for p in values_points]

    plt.plot(x, y, color="red", label="Estimated Value")
    plt.axhline(y=expeted_result, color="blue", linestyle="--", label="Expeted Value")

    plt.title("Value Estimation using Monte Carlo")
    plt.xlabel("Number of Points")
    plt.ylabel("Estimated Value")
    plt.grid(True)
    plt.legend()
    plt.show()

def estimate_exponential_area(exp_function, square, number_points):
    
    if not square.function_mode:
        print("The square must be in function mode")
        return None
    area_values = []
    count_points_in_area = 0
    x0, x1 = 0, square.length
    
    for i in range(1, number_points + 1):
        point = square.random_point()
        if exp_function.is_inside(point):
            count_points_in_area += 1

        # Calculate the ratio of points inside the area to total points
        proportion_area = count_points_in_area / i

        # Estimate the area using the Monte Carlo method
        area_calculated = square.area() * proportion_area
        area_values.append((i, area_calculated))
    
    return area_calculated, exp_function.real_area(x0, x1), area_values