
def take_square(x):
    return x**2


def estimate_derivative(func, x, h=1e-5):
    estimate = (func(x + h) - func(x - h)) / (2 * h) 
    return estimate

def integrate(func, steps=1000):
    dx = 1 / steps
    total_area = 0
    for i in range(steps):
        xi = (i + 0.5) * dx
        total_area = total_area + func(xi) * dx
    return total_area


def f_x_twice(x, f_x):
    
    return f_x(f_x(x))

print(estimate_derivative(take_square, 3))
print("Integral of x^2:", integrate(take_square))
print(f_x_twice(2, take_square))