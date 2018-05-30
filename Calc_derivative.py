# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Calculate Derivative
--------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

Implement integration of the same function using Riemann sums or the
trapezoidal rule.

See :ref:`calc-derivative-solution`.
"""
from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, subplot, legend, title

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)

y_dev = y[1:]-y[0:-1]
x_dev = x[1:]-x[0:-1]

# print("x", x[0:10])   ###testing if dev X and dev y are OK
# print("y", y[0:10])
# print("dev_x", x_dev[0:10])
# print("dev_y", y_dev[0:10])

derivate = y_dev/x_dev

# print("derivate", derivate)  ##testing if the derivate make sense. it dose - I can see the slop changeging signs

#### calculate a mid point between each 2 x's: half way between 2 sequenced x - add it to the first
mid_x = x[:-1] + ((x[1:]-x[:-1])/2)
#print("mid_x", x[0],x[1], mid_x[0] ) ###test if mid X is working. work perfect!!

plot(x,y)
plot(mid_x,derivate)
show()
