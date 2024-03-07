import numpy as np

#Part 2 of the midterm programming assignment

def f(x):
    return x**2 + 4 * np.cos(x)

def golden_section(a, b, tolerance):

    golden_ratio = (1 + np.sqrt(5)) / 2
    uncertainty_interval = b - a
    #iteration counter
    k = 1

    #output table header
    print("| Iteration k  | ak     | bk     | f(ak)  | f(bk)  | New uncertainty interval |")

    while uncertainty_interval > tolerance:
        
        #calculate new points
        c = b - (b - a) / golden_ratio
        d = a + (b - a) / golden_ratio

        #evaluate the function at new points
        f_c = f(c)
        f_d = f(d)

        #output intermediate results
        print(f"| {k:12} | {a:.4f} | {b:.4f} | {f_c:.4f} | {f_d:.4f} | [{a:.4f}, {b:.4f}]         |")

        #narrow down the interval
        if f_c < f_d:
            b = d
        else:
            a = c

        #update uncertainty interval
        uncertainty_interval = b - a

        #increment iteration counter
        k += 1

    #final output for the last iteration
    print(f"| {k:12} | {a:.4f} | {b:.4f} | {f_c:.4f} | {f_d:.4f} | [{a:.4f}, {b:.4f}]         |")


def main():
    a = 1
    b = 2
    tolerance = 0.2

    golden_section(a, b, tolerance)

if __name__ == "__main__":
    main()
