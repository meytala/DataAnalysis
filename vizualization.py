import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2,]
working  = [7,8,7,2,2,]
playing = [8,5,7,8,13]

#####stackplot

plt.stackplot(days, sleeping, eating, working, playing, colors = ['m', "c", "r","k"])
###for some reason, you cannot add lables to the stack plot. therefor, you can add a plot that is transparent
plt.plot([],[], color = "m", label="Sleeping", linewidth=5)
plt.plot([],[], color = "c", label="Eating", linewidth=5)
plt.plot([],[], color = "r", label="Working", linewidth=5)
plt.plot([],[], color = "k", label="Playing", linewidth=5)

plt.xlabel("days")
plt.ylabel("hours")
plt.title("stack plot")
plt.legend()
plt.show()


####piechart
slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c', 'm', 'r', 'g']
plt.pie(slices,
        labels=activities,
        colors =colors,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct = '%1.1f%%')
plt.title("Piechart")
plt.show()


