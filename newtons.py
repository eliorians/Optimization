import numpy as np

def f(x):
    return x**2 + 4 * np.cos(x)

def f_prime(x):
    return 2*x - 4*np.sin(x)

def newton_method(x0, num_iterations):

    #initialize x_n as x0
    x_n = x0

    #output table header
    print("| Iteration k  | x_n    | f(x_n) | f'(x_n) |")

    for k in range(x0, num_iterations):
        #calculate function value and its derivative at x_n
        f_x_n = f(x_n)
        f_prime_x_n = f_prime(x_n)

        #output intermediate results
        print(f"| {k:12} | {x_n:.4f} | {f_x_n:.4f} | {f_prime_x_n:.4f} |")

        #update x_n using Newton's method formula
        x_n = x_n - f_x_n / f_prime_x_n

    #output for the last iteration
    print(f"| {num_iterations:12} | {x_n:.4f} | {f(x_n):.4f} | {f_prime(x_n):.4f}  |")

def main():
    x0 = 1
    num_iterations = 5

    newton_method(x0, num_iterations)

if __name__ == "__main__":
    main()
