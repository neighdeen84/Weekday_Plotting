import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import datetime
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator

neo = pd.read_csv('EV2.csv')
neo.columns =['timestamp', 'Power']
fig1 = plt.figure(1, figsize=(18,18))


neo['timestamp'] = pd.to_datetime(neo['timestamp'], format='%Y-%m-%d %H:%M:%S')
plt1 = plt.plot(neo.timestamp,neo['Power'], label='EV profile', color='red', marker='.', markersize='1')
plt.xlabel('Time')
plt.ylabel('Real Power (W)')
plt.legend()

# ax is an axes object, e.g. from figure.get_axes()
ax = fig1.get_axes()[0].xaxis

# Hide major tick labels:
ax.set_major_formatter(ticker.NullFormatter())

# Customize minor tick labels:
minor_locator = AutoMinorLocator(2)
ax.set_minor_locator(minor_locator)
ax.set_minor_formatter(ticker.FixedFormatter(['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday']))
plt.tick_params(axis='x',which='minor',bottom=False,top=False,labelbottom=True)
plt.grid()
plt.show()

