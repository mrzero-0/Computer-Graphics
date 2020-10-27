import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_axis_off()
R = 5
# ax.set_xlim(-5, 5)
# ax.set_ylim(-5, 5)
# ax.set_zlim(-5, 5)


def Show_Axes():

    X = (R, 0, 0)
    Y = (0, R, 0)
    Z = (0, 0, R)
    pos_vector(X, 'black')
    pos_vector(Y, 'black')
    pos_vector(Z, 'black')
    ax.text(R//2, 0, 0, "X-axis")
    ax.text(0, R//2, 0, "Y-axis")
    ax.text(0, 0, R//2, "Z-axis")


def point(A, color="r"):
    ax.scatter(A[0], A[1], A[2], color=color, s=25)
    ax.text(A[0], A[1], A[2], "(%d,%d,%d)" % (A[0], A[1], A[2]))


def pos_vector(A, color="cyan"):
    ax.quiver(0, 0, 0, A[0], A[1], A[2], length=1.0, arrow_length_ratio=0.1, color=color)


def vector(P, Q):
    x1, y1, z1 = P[0], P[1], P[2]
    x2, y2, z2 = Q[0], Q[1], Q[2]
    ax.quiver(x1, y1, z1, x2, y2, z2, length=1.0, arrow_length_ratio=0.1)


def line_segment(P, Q, color="b"):
    xs, ys, zs = (P[0], Q[0]), (P[1], Q[1]), (P[2], Q[2])
    ax.plot3D(xs, ys, zs, color=color)


def plane(N, d, color='r'):

    # a plane is a*x+b*y+c*z+d=0
    # [a,b,c] is the normal. Thus, we have to calculate
    # d and we're set

    # create x,y
    xx, yy = np.meshgrid(range(R), range(R))

    # calculate corresponding z
    z = (-N[0] * xx - N[1] * yy - d) * 1. / N[2]

    ax.plot_surface(xx, yy, z, alpha=0.4, color=color)
    vector((xx[2][2], yy[2][2], z[2][2]), N)


def cuboid(P, Q):
    points = [P,
              (P[0], P[1], Q[2]),
              (P[0], Q[1], P[2]),
              (P[0], Q[1], Q[2]),
              (Q[0], P[1], P[2]),
              (Q[0], P[1], Q[2]),
              (Q[0], Q[1], P[2]),
              Q]
    for i in range(0, 8):
        point(points[i])

    for i in (0, 3, 5, 6):
        for j in (1, 2, 4, 7):
            if abs(i-j) in (1, 2, 4)and(i != 3 or j != 4):

                line_segment(points[i], points[j])


def Sphere(radius, center=(0, 0, 0), alpha=0.2):
    r = radius
    u, v = np.mgrid[0:2*np.pi:600j, 0:np.pi:600j]
    x = r*np.cos(u)*np.sin(v)+center[0]
    y = r*np.sin(u)*np.sin(v)+center[1]
    z = r*np.cos(v)+center[2]
    ax.plot_surface(x, y, z, color="r", alpha=alpha)
    point(center, "black")


# plane((1, 0, 1), 0)
Show_Axes()
# cuboid((1, 1, 1), (2, 2, 2))
cuboid((0, 0, 0), (1, 1, 1))
# pos_vector((1, 1, 1), "r")
Sphere(1, (1, 1, 1))
plt.show()
