import matplotlib.pyplot as plt

train_trips = [5, 0]
bus_trips = [0, 15]

plt.plot(bus_trips, train_trips)
plt.xlabel('Bus Trips')
plt.ylabel('Train Trips')
plt.title('Jordan\'s Budget Constraint')
plt.show()