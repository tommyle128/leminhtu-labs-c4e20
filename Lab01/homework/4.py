import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
customers = db['customers']

all_customers = customers.find()

all_refs = {}
all_refs['Events'] = 0
all_refs['Advertisement'] = 0
all_refs['Word of mouth'] = 0

for c in all_customers:
    if c['ref'] == 'events':
        all_refs['Events'] += 1
    elif c['ref'] == 'ads':
        all_refs['Advertisement'] += 1
    elif c['ref'] == 'wom':
        all_refs['Word of mouth'] += 1

labels = []
values = []
for key, value in all_refs.items():
    print("The number of customer from", key, ":", value)
# Draw pie chart
    labels.append(key)
    values.append(value)

colors = ["green", "blue", "orange"]
explode = [0, 0.1, 0.1]

pyplot.pie(
        values,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        )
pyplot.axis('equal')

pyplot.show()











        

    
