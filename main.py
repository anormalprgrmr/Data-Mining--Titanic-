import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('titanic.csv')

file.plot(kind='scatter',x='PassengerId',y='Age')

plt.savefig('out.png')
