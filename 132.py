import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("stars_gravity.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius,mass)
plt.title("Radius and Mass")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,gravity)
plt.title("Mass and Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

plt.scatter(radius,mass)
plt.title("Mass and Radius")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(radius, gravity)
plt.title("Radius and Gravity")
plt.xlabel("Radius")
plt.ylabel("Gravity")
plt.show()