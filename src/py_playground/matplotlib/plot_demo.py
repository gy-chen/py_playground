import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(-10, 10)
    y = np.sin(x)
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

if __name__ == '__main__':
    main()
