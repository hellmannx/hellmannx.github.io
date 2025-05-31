import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

# Parameters
D = 1.0
frames = []
point_size = 20

def power_of_two():
    # Generate frames
    for i in range(10):
        num_points = 2**i + 1
        x = np.linspace(0, D, num_points)
        y = np.zeros_like(x)

        fig, ax = plt.subplots(figsize=(6, 0.7))
        ax.scatter(x, y, c='black', s=point_size)
        ax.set_xlim(-0.1, D + 0.1)
        ax.set_ylim(-0.1, 0.1)
        ax.axis('off')
        ax.set_title(f"{num_points} points", fontsize=10)

        buf1 = io.BytesIO()
        plt.savefig(buf1, format='png', bbox_inches='tight')
        plt.close(fig)
        buf1.seek(0)
        frames.append(Image.open(buf1))

def one_by_one():
    for i in range (99):
        if i == 0:
            num_points = 2
        else:
            num_points = num_points + 1
        x = np.linspace(0, D, num_points)
        y = np.zeros_like(x)

        fig, ax = plt.subplots(figsize=(6, 0.7))
        ax.scatter(x, y, c='black', s=point_size)
        ax.set_xlim(-0.1, D + 0.1)
        ax.set_ylim(-0.1, 0.1)
        ax.axis('off')
        ax.set_title(f"{num_points} points", fontsize=10)

        buf2 = io.BytesIO()
        plt.savefig(buf2, format='png', bbox_inches='tight')
        plt.close(fig)
        buf2.seek(0)
        frames.append(Image.open(buf2))

# power_of_two()
one_by_one()

# Save GIF
frames[0].save("converging_line2.gif", format='GIF',
               save_all=True, append_images=frames[1:],
               duration=500, loop=0)
