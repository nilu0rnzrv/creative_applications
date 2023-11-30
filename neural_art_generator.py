from __future__ import print_function

import os
import sys
from PIL import Image, ImageFilter, ImageEnhance
import neuralart
import numpy as np

RENDER_SEED = 42
Z_SEED = 5
DEVICE = "cpu"
ITERATIONS = 5000
MIN_STEP_SIZE = 0.01
MAX_STEP_SIZE = 0.02
XRES = 1024
YRES = 1024
XLIM = np.array([-1.0, 1.0])
YLIM = XLIM * (float(YRES) / XRES)
DEPTH = 5
CHANNELS = 3  # Using RGB color channels
OUTPUT_STD = 1.5
HIDDEN_STD = 1.4
Z_DIMS = 5
Z_RANGE = (-1.6, 1.2)
RADIUS = False  # Disable radius for a different effect

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} DIRECTORY\n".format(sys.argv[0]))
    sys.exit(1)

output_directory = os.path.join(sys.argv[1], "output_images")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

rng = np.random.RandomState(seed=Z_SEED)

zfill = len(str(ITERATIONS - 1))

M = np.array([
    [-1, 3, -3, 1],
    [3, -6, 3, 0],
    [-3, 3, 0, 0],
    [1, 0, 0, 0]
])

P0 = rng.uniform(*Z_RANGE, size=Z_DIMS)
P1 = rng.uniform(*Z_RANGE, size=Z_DIMS)
P2 = rng.uniform(*Z_RANGE, size=Z_DIMS)
P3 = rng.uniform(*Z_RANGE, size=Z_DIMS)

count = 0
while count < ITERATIONS:
    P0 = P3
    P1 = 2 * P3 - P2
    P2 = rng.uniform(*Z_RANGE, size=Z_DIMS)
    P3 = rng.uniform(*Z_RANGE, size=Z_DIMS)
    pos = P0

    lo = 0.0
    hi = 1.0
    while np.linalg.norm(P3 - pos) > MIN_STEP_SIZE:
        if count >= ITERATIONS:
            break
        t = (lo + hi) / 2.0
        P = np.vstack((P0, P1, P2, P3)).T
        C = P.dot(M).dot(np.array([t ** 3, t ** 2, t, 1]))
        distance = np.linalg.norm(C - pos)
        if distance < MIN_STEP_SIZE:
            lo = t
            continue
        elif distance > MAX_STEP_SIZE:
            hi = t
            continue
        pos = C

        result = neuralart.render(
            depth=DEPTH,
            xres=XRES,
            yres=YRES,
            xlim=XLIM,
            ylim=YLIM,
            seed=RENDER_SEED,
            channels=CHANNELS,
            output_std=OUTPUT_STD,
            hidden_std=HIDDEN_STD,
            radius=RADIUS,
            z=C,
            device=DEVICE
        )

        # Convert the NumPy array to a PIL Image
        result_image = Image.fromarray((result * 255).astype(np.uint8))

        # Apply additional effects using PIL
        result_image = result_image.filter(ImageFilter.GaussianBlur(radius=2))
        result_image = ImageEnhance.Color(result_image).enhance(1.5)

        file = os.path.join(output_directory, f"image_{count:04d}_iter_{t:.2f}.png")
        result_image.save(file, "png")

        count += 1
        lo = t
        hi = 1.0
