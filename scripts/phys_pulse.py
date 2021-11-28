import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from textwrap import wrap
import numpy as np
import phys_preasure as PP

fig, ax = plt.subplots(figsize=(13, 10), dpi=75)
ind_end = list(abs(PP.time_list - PP.time_sistola - 10)).index(min(abs(PP.time_list - PP.time_sistola - 10)))
time_pulse = PP.time_list[PP.ind_sistola: ind_end + 1]
data_pulse = PP.data_rest[PP.ind_sistola: ind_end + 1]
delta = max(data_pulse) - min(data_pulse)
delta_ind = ind_end - PP.ind_sistola
data_pulse -= max(data_pulse)
for i in range(delta_ind + 1):
    data_pulse[i] += delta * i/delta_ind
bot = min(data_pulse)
top = max(data_pulse)
left = list(np.linspace(0, top-bot/4, len(data_pulse)//2))
right = list(np.linspace(top-bot/6, -(top-bot)/5, len(data_pulse)//2))
data_pulse[1:] += np.array(left + right)

plt.plot(time_pulse, data_pulse, color='green', linestyle='-',  linewidth=2)
plt.rcParams['font.size'] = '14'
title = 'Пульс после физической нагрузки'
ax.set_title("\n".join(wrap(title, 100)))
plt.xlabel('Время, [с]', fontsize=14)
plt.ylabel('Давление [мм. рт. ст.]', fontsize=14)
plt.legend(['Пульс - 66 [уд/мин]'], loc='upper right')
ax.set_xlim(min(time_pulse) - 0.5, max(time_pulse) + 0.5)
ax.set_ylim(min(data_pulse) - 0.5, max(data_pulse) + 0.5)
ax.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=14)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.grid(which='minor', linewidth='0.5', linestyle='-', color='grey')
ax.grid(which='major', linewidth='1.25', linestyle='-', color='grey')

plt.show()

