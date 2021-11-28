import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from textwrap import wrap
import calibration as C

with open('preasure_rest.txt', 'r') as f:
    text = f.readlines()
    T = float(re.search(r'\d+\.\d+', text[3]).group(0))
    print(T)
    data_rest = np.array(text[10:], dtype=int) / C.k


time_list = np.linspace(0, T, len(data_rest))
fig, ax = plt.subplots(figsize=(13, 10), dpi=75)
plt.plot(time_list, data_rest, color='b', linestyle='-',  linewidth=2)
plt.rcParams['font.size'] = '14'
title = 'Артериальное давление до физической нагрузки'
ax.set_title("\n".join(wrap(title, 100)))
plt.xlabel('Время, [с]', fontsize=14)
plt.ylabel('Давление [мм рт. ст.]', fontsize=14)
plt.legend(['Давление - 117/59 [мм. рт. ст.]'])
ax.set_xlim(0, 30)
ax.set_ylim(40, 170)
ax.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=14)
ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.grid(which='minor', linewidth='0.5', linestyle='-', color='grey')
ax.grid(which='major', linewidth='1.25', linestyle='-', color='grey')
time_sistola = 5.3
time_diastola = 22.1
ind_sistola = list(abs(time_list - time_sistola)).index(min(abs(time_list - time_sistola)))
ind_diastola = list(abs(time_list - time_diastola)).index(min(abs(time_list - time_diastola)))
ax.scatter(time_list[ind_sistola], data_rest[ind_sistola], color='red', marker='X', s=150, linewidth=2)
ax.text(time_list[ind_sistola], data_rest[ind_sistola] + 2.5, 'Systole')
ax.scatter(time_list[ind_diastola], data_rest[ind_diastola], color='green', marker='X', s=150, linewidth=2)
ax.text(time_list[ind_diastola], data_rest[ind_diastola] + 2.5, 'Diastole')

plt.show()