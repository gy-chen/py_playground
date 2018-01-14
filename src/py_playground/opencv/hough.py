import numpy as np


def get_hough_y(x, theta, p):
    return (x * np.cos(theta) - p) / np.sin(theta)


if __name__ == '__main__':
    x = np.arange(100)
    theta = np.deg2rad(75)
    p = 0
    y = np.array([get_hough_y(xv, theta, p) for xv in x])
    import matplotlib.pyplot as plt
    plt.plot(x, y)
    plt.axis([0, 200, 0, 200])
    plt.show()
