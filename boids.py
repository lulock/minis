from matplotlib import pyplot as plt
from matplotlib import animation
from celluloid import Camera
import numpy as np
import os
np.random.seed(0)

# N boids
boid_count = 10

# boundary of sim
bounds = np.array([2000, 2000])
print(bounds.shape)
# initiate random positions (x,y) for N boids within boundaries
positions0 = np.random.rand(2, boid_count) * bounds[:, np.newaxis]
# numpy.newaxis is used to increase the dimension of the existing array by one more dimension, when used once.
# print(positions0)


def flock(count, lower_bound, upper_bound):
    width = upper_bound - lower_bound
    return lower_bound[:, np.newaxis] + np.random.rand(2, count) * width[:, np.newaxis]


positions = flock(boid_count, np.array([0, 0]), np.array([2000, 2000]))
# print(positions)

velocities = flock(boid_count, np.array([0, -20]), np.array([10, 20]))
# print(velocities)


figure = plt.figure()
plt.style.use('dark_background')
axes = plt.axes(xlim=(0, bounds[0]), ylim=(0, bounds[1]))
scatter = axes.scatter(
    positions[0, :], positions[1, :], marker='*', color="chartreuse", edgecolor="yellow", lw=.5)
plt.show()


def update(positions, velocities):

    # fly toward the middle using mean positions
    middle = np.mean(positions, 1)
    # print(middle)

    direction_towards_middle = positions - middle[:, np.newaxis]
    # print(direction_towards_middle)

    middle_strength = 0.02

    velocities -= direction_towards_middle * middle_strength
    positions += velocities


def animate(frame):
    update(positions, velocities)
    scatter.set_offsets(positions.transpose())


anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

positions = flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = flock(100, np.array([0, -20]), np.array([10, 20]))

anim.save("img/boids.gif", writer="PillowWriter", fps=2)
