import numpy as np

#Part 3 of the midterm programming assignment

def f(x):
    return x**2 + 4 * np.cos(x)

def fibonacci_method(a, b, epsilon):

    #fibonacci sequence initialization
    fib = [1, 1]
    while fib[-1] < (b - a) / epsilon:
        fib.append(fib[-1] + fib[-2])

    #iteration counter
    k = 1

    #output table header
    print("| Iteration k  | ρk     | ak     | bk     | f(ak)  | f(bk)  | New uncertainty interval |")

    while len(fib) > 2:

        #ratio for current iteration
        rho_k = fib[-3] / fib[-1]

        #calculate new points
        c = a + rho_k * (b - a)
        d = a + (1 - rho_k) * (b - a)

        #evaluate the function at new points
        f_c = f(c)
        f_d = f(d)

        #output intermediate results
        print(f"| {k:12} | {rho_k:.4f} | {a:.4f} | {b:.4f} | {f_c:.4f} | {f_d:.4f} | [{a:.4f}, {b:.4f}]         |")

        #narrow down the interval
        if f_c < f_d:
            b = d
        else:
            a = c

        #update Fibonacci sequence
        fib = fib[:-1]

        #increment iteration counter
        k += 1

    #output for the last iteration
    print(f"| {k:12} | {rho_k:.4f} | {a:.4f} | {b:.4f} | {f_c:.4f} | {f_d:.4f} | [{a:.4f}, {b:.4f}]         |")

def main():
    a = 1
    b = 2
    epsilon = 0.05

    fibonacci_method(a, b, epsilon)

if __name__ == "__main__":
    main()
