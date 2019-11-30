#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

   # Значения по X
   data_x = []
   with open("x.txt") as f:
      for line in f:
         data_x.append( int(line))
   # Значения по Y
   data_y = []
   with open("y.txt") as f:
      for line in f:
         data_y.append( int(line))

# Значения по X
   data_x_usa = []
   with open("x_usa.txt") as f:
      for line in f:
         data_x_usa.append( int(line))
   # Значения по Y
   data_y_usa = []
   with open("y_usa.txt") as f:
      for line in f:
         data_y_usa.append( int(line))
         
  # rng = np.arange(50)
  # rnd = np.random.randint(0, 10, size=(3, rng.size))
  # yrs = 1600 + rng
  # fig, ax = plt.subplots(figsize=(5, 3))
   plt.axis([1669 , 2020, 0, 1100])
   plt.xlabel("Год")
   plt.ylabel("Число математиков")
   
   # представляем точки (х,у) кружочками диаметра 10
   plt.plot(data_x_usa, data_y_usa, 'r', color='green')
   plt.plot(data_x, data_y, 'r')

   # Сетка на фоне для улучшения восприятия
  #  plt.grid(True, linestyle='-', color='0.75')

   plt.minorticks_on()
   # Определяем внешний вид линий основной сетки:
   plt.grid(which='major', color = 'k',  linewidth = 1)
   #  Определяем внешний вид линий вспомогательной сетки:
   plt.grid(which='minor', color = 'k',  linestyle = ':')
   
   plt.savefig('count_math.png', fmt='png')
   plt.show()
   
