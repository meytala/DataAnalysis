##This is a 2x2 layout, with 3 slots occupied.

# 1. Sine function, with blue solid line; cosine with red '+' markers; the
#    extents fit the plot exactly. Hint: see the axis() function for setting the
#    extents.
# 2. Sine function, with gridlines, axis labels, and title; the extents fit the
#    plot exactly.
# 3. Image with color map; the extents run from -10 to 10, rather than the
#    default.

# Save the resulting plot image to a file. (Use a different file name, so you
# don't overwrite the sample.)

# The color map in the example is 'winter'; use 'cm.<tab>' to list the available
# ones, and experiment to find one you like.

# Start with the following statements::

from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, pi, sin, cos
import matplotlib.image as mpimg

x = np.linspace(0, 2*pi, 101)
s = sin(x)
c = cos(x)

##fig, axes = plt.subplots(nrows = 2, ncols=2, figsize=(3,3))


#####first plot - upper left

plt.subplot(2,2,1)
plt.plot(x,s,color="b")
plt.plot(x,c, "r+")
plt.axis("tight")
# print(plt.axis())
# xmin, xmax = plt.xlim()  # return the current xlim
# plt.xlim((xmin, xmax))   # set the xlim to xmin, xmax


#####second plot - upper right

plt.subplot(2,2,2)
plt.plot(x,s,color="b")
plt.xlabel("x")
plt.ylabel("Sin(x)")
plt.title("Sin(x) by X", fontsize=12)
plt.tight_layout()
plt.axis("tight")


#####third plot - lower left

img = mpimg.imread('dc_metro.jpg')
#lum_img = img[:,:,0]
plt.subplot(2,2,3)
#plt.imshow(lum_img)
#plt.colorbar()
plt.imshow(img, cmap="winter")



# Tip: If you find that the label of one plot overlaps another plot, try adding
# a call to `tight_layout()` to your script.

plt.tight_layout()  ###relayout in a better way

plt.show()
plt.savefig("a layout of figures")