#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

   # Значения по X
   data_x = []
   with open("x_lifespan_usa.txt") as f:
      for line in f:
         data_x.append(int(line))
   # Значения по Y
   data_y = []
   with open("y_lifespan_usa.txt") as f:
      for line in f:
         data_y.append(float(line))
    
   plt.axis([1700 , 2000, 0, 100])
   plt.xlabel("Год")
   plt.ylabel("Средняя продолжительность жизни")
   
   # представляем точки (х,у) кружочками диаметра 10
   plt.plot(data_x, data_y, 'o', color = "green")

   # Сетка на фоне для улучшения восприятия
  #  plt.grid(True, linestyle='-', color='0.75')

   plt.minorticks_on()
   # Определяем внешний вид линий основной сетки:
   plt.grid(which='major', color = 'k',  linewidth = 1)
   #  Определяем внешний вид линий вспомогательной сетки:
   plt.grid(which='minor', color = 'k',  linestyle = ':')
   
   plt.savefig('chart_usa.png', fmt='png')
   plt.show()
   
