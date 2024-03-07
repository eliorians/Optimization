import numpy as np
import matplotlib.pyplot as plt

#Part 1 of the midterm programming assignment

def f(x):
    return x**2 + 4 * np.cos(x)

def plot():

    #generate x values from 1 to 2
    x_values = np.linspace(1, 2)
    #generate y values
    y_values = f(x_values)

    #plot
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x) = x^2 + 4*cos(x) from 1 to 2')
    plt.grid(True)
    plt.legend()
    plt.savefig('plot.png')
    plt.show()
    
def main():
    plot()

if __name__ == "__main__":
    main()