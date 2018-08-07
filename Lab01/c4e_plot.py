import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

# 1. Prepare data
labels = ["Web", "Android", "iOS", "React Native"]
values = [400, 250, 200, 150]
colors = ["green", "blue", "orange", "gold"]
explode = [0, 0, 0, 0.2]


# 2. Plot
pyplot.pie(
            values,
            labels=labels,
            colors=colors, 
            explode=explode
            )
pyplot.axis('equal')

# 3. Show graph
pyplot.show()