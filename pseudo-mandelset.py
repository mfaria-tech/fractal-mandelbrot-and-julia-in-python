### ========================================================================
### TITLE       : PSEUDOCODE - MANDELBROT SET
### AUTOR       : MARCUS FARIA
### DATE        : 14.11.2022
###
### DESCRIPTION :
###     A pseudocode for a brief visualization of the structure of
###     the Mandelbrot set.
###
### FOLLOW ME:
###     GITHUB (curr-account) --> https://github.com/mfaria-tech
###     GITHUB (old-account) --> https://github.com/Marcus-Faria
###     LINKEDIN --> https://www.linkedin.com/in/marcus-v-faria-4a2117213/
### ========================================================================

## Import libs for sample data generation and graphical visualization
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image


## Suppress overflow error alerts
#np.warnings.filterwarnings("ignore")



### =======================================================
### for each pixel (Px, Py) on the screen do
###   x0 := scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.00, 0.47))
###   y0 := scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1.12, 1.12))
###   x := 0.0
###   y := 0.0
###   iteration := 0
###   max_iteration := 1000
###   while (x*x + y*y ≤ 2*2 AND iteration < max_iteration) do
###       xtemp := x*x - y*y + x0
###       y := 2*x*y + y0
###       x := xtemp
###       iteration := iteration + 1
###
###   color := palette[iteration]
###   plot(Px, Py, color)
###
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2



### GRAPHICAL GENERATOR MANDELBROT SET

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


c = complex_matrix(-2, .5, -1.5, 1.5, pixel_density=512)

# members = get_members(c, num_iterations=20)
# plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
# plt.gca().set_aspect("equal")
# plt.axis("off")
# plt.tight_layout()
# plt.show()

image = Image.fromarray(~is_stable(c, num_iterations=20))
image.save('./img/fractal_high_density.png')
image.show()
