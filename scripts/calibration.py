import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import matplotlib.ticker as ticker
calibration = {}

with open('40mmHg.txt', 'r') as f:
    text = np.array(list(map(int, f.readlines()[10:])))
    calibration['ACP40mm'] = np.round(np.average(text), 5)
with open('80mmHg.txt', 'r') as f:
    text = np.array(list(map(int, f.readlines()[10:])))
    calibration['ACP80mm'] = np.round(np.average(text), 5)
with open('120mmHg.txt', 'r') as f:
    text = np.array(list(map(int, f.readlines()[10:])))
    calibration['ACP120mm'] = np.round(np.average(text), 5)
with open('160mmHg.txt', 'r') as f:
    text = np.array(list(map(int, f.readlines()[10:])))
    calibration['ACP160mm'] = np.round(np.average(text), 5)

part1x = np.linspace(40, 80, 200)
part1y = np.linspace(calibration['ACP40mm'], calibration['ACP80mm'], 200)
part2x = np.linspace(80, 120, 200)
part2y = np.linspace(calibration['ACP80mm'], calibration['ACP120mm'], 200)
part3x = np.linspace(120, 160, 200)
part3y = np.linspace(calibration['ACP120mm'], calibration['ACP160mm'], 200)

datax = np.vstack([part1x, part2x, part3x])[0]
datay = np.vstack([part1y, part2y, part3y])[0]
p = np.polyfit(datax, datay, 1)
result_x = np.linspace(40, 160, 240)
result_y = np.polyval(p, result_x)
k = p[0]

fig, ax = plt.subplots(figsize=(13, 10), dpi=75)
plt.plot(result_x, result_y, color='b', linestyle='-',  linewidth=2)
ax.scatter(40, (calibration['ACP40mm']), color='red', marker='+', s=150, linewidth=2)
ax.scatter(80, (calibration['ACP80mm']), color='purple', marker='+', s=150, linewidths=2)
ax.scatter(120, (calibration['ACP120mm']), color='black', marker='+', s=150, linewidths=2)
ax.scatter(160, (calibration['ACP160mm']), color='orange', marker='+', s=150, linewidths=2)
plt.rcParams['font.size'] = '14'
title = 'Калибровочнай график зависимость показаний АЦП от давления'
ax.set_title("\n".join(wrap(title, 100)))

plt.xlabel('Давление, [Па]', fontsize=14)
plt.ylabel('Отчёты АЦП', fontsize=14)

ax.set_xlim(min(result_x) - 5, max(result_x) + 5)
ax.set_ylim(min(result_y) - 50, max(result_y) + 50)

ax.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=14)

ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

ax.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(50))

ax.grid(which='minor', linewidth='0.5', linestyle='-', color='grey')
ax.grid(which='major', linewidth='1.25', linestyle='-', color='grey')

plt.show()
