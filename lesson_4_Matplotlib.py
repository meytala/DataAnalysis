import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.misc import face
from matplotlib import cm

##plt.plot(range(10))
##plt.show()

Time = [0,1,2,3,4,5,6]
CO2_con = [250, 265, 272, 260, 300, 320, 389]
Temp= [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
#
#
# plt.plot(Time, CO2_con, "b-^", label = "CO2")
# plt.plot(Time, Temp, "r-o", label = "Temp")
# plt.title("Chemistry data")
# plt.xlabel("Time")
# plt.ylabel("CO2 concsntrations")
# plt.legend()
# plt.show()


# np.random.seed(5)

# ###create x and y
# x= np.arange(1,101)
# x2 = (np.arange(1,101))*-1
# y= 20+3 * x + np.random.normal(0,60,100)
# y2= 10+2*x + np.random.normal(0,60,100)

# plt.scatter(x,y)
# plt.plot(x,y,"o", color = 'b', alpha=0.5, label="label x,y")
# plt.plot(x2,y2,"o", color = 'r', alpha=0.5, label="label x2,y2")
# plt.legend(loc="lower right")
# plt.show()


# slope, intercept, r_value, p_value, std,err = stats.linregress(x,y)
# line = slope*x+intercept



# plt.plot(x,y)
# plt.plot(x,np.poly1d(np.polyfit(x,y,1))(x))
# plt.show()

#
# img= face()
# plt.imshow(img, extent=[-25, 25, -25, 25], cmap=plt.cm.bone)
# plt.show()

ax1=plt.subplot()
ax1.plot(Time, CO2_con)
ax1.set_ylabel("[CO2]")
ax2=ax1.twinx()
ax2.plot(Time, Temp)
ax2.set_ylabel("Temp (degC)")
plt.show()


plt.subplot(1,3,1)
plt.plot(range(0,10,1))

plt.subplot(1,3,2)
plt.plot(range(10,0,-1))

plt.subplot(1,3,3)
plt.plot([4]*10)
plt.show()

