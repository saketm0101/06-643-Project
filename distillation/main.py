"""Main file for McCabe thiele method."""

ratio = 1.5


def mccabe_thiele_calculations(feed_flow, xf, xd):
    import numpy as np
    import matplotlib.pyplot as plt

    F = feed_flow
    xb = 0.2
    a = 2

    Q = [[1, 1], [xb, xd]]
    R = [F, F * xf]

    X = np.linalg.solve(Q, R)
    B = X[0]
    D = X[1]

    # VLE Curve
    x = np.arange(0, 1.025, 0.025)
    y = a * x / (1 + (a - 1) * x)

    # Calculating Ract and Rmin
    yrm = a * xf / (1 + (a - 1) * xf)
    xrm = xf
    Rmin = (xd - yrm) / (yrm - xrm)
    Ract = Rmin * ratio

    # q, rectifying, and stripping lines
    yi = (xd + Ract * xf) / (Ract + 1)  # intersection of these lines

    # Calculating number of stages
    x1 = xd
    y1 = xd
    m = (yi - xb) / (xf - xb)
    c = yi - m * xf
    n = 0

    while x1 >= xb:
        y2 = y1
        x2 = y1 / (a + y2 - a * y2)
        x3 = x2

        if x3 > xf:
            y3 = (xd + (Ract * x3)) / (Ract + 1)
        else:
            y3 = x3 * m + c

        x1 = x3
        y1 = y3
        n += 1

    return [n, D, B]


def mccabe_thiele_plot(feed_flow, xf, xd):
    import numpy as np
    import matplotlib.pyplot as plt

    F = feed_flow
    xb = 0.2
    a = 2

    Q = [[1, 1], [xb, xd]]
    R = [F, F * xf]

    X = np.linalg.solve(Q, R)
    B = X[0]
    D = X[1]

    # VLE Curve
    x = np.arange(0, 1.025, 0.025)
    y = a * x / (1 + (a - 1) * x)
    plt.plot(x, y, "k", label="VLE Curve")

    # Calculating Ract and Rmin
    yrm = a * xf / (1 + (a - 1) * xf)
    xrm = xf
    Rmin = (xd - yrm) / (yrm - xrm)
    Ract = Rmin * ratio

    # q, rectifying, and stripping lines
    yi = (xd + Ract * xf) / (Ract + 1)  # intersection of these lines
    plt.plot([xd, xf], [xd, yi], "b", label="Stripping Line")
    plt.plot([xf, xb], [yi, xb], "c", label="Rectifying Line")

    # Calculating number of stages
    x1 = xd
    y1 = xd
    m = (yi - xb) / (xf - xb)
    c = yi - m * xf
    n = 0

    while x1 >= xb:
        y2 = y1
        x2 = y1 / (a + y2 - a * y2)
        plt.plot([x1, x2], [y1, y2], "r")

        x3 = x2

        # Checking to avoid step landing on rectifying line after crossing xf
        if x3 > xf:
            y3 = (xd + (Ract * x3)) / (Ract + 1)
        else:
            y3 = x3 * m + c
        plt.plot([x2, x3], [y2, y3], "r")

        x1 = x3
        y1 = y3
        n += 1
    plt.plot([0, 1], [0, 1], "y", label="y=x")  # 45 degree line
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Number of Ideal Stages")
    plt.legend()
    plt.show()


def mccabe_thiele(feed_flow, xf, xd):
    """Takes the feed flow rate, feed mole fraction and the
    desired distillate mole fraction to plot mccabe-thiele plot,
    output flow rates and number of stages"""

    a = mccabe_thiele_calculations(feed_flow, xf, xd)
    print(f"The number of stages is {a[0]}")
    print(f"Distillate flow rate = {a[1]:1.3f} kg/hr")
    print(f"Bottoms flow rate = {a[2]:1.3f} kg/hr\n")
    print("The McCabe Thiele method plot - \n")
    mccabe_thiele_plot(feed_flow, xf, xd)
