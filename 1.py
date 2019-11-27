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
         
   # plt.axis([2000, 2020, 0, 10])
   plt.xlabel("X")
   plt.ylabel("Y")
   # представляем точки (х,у) кружочками диаметра 10
 #  plt.plot(data_x, data_y, 'r')
   plt.plot(data_x, data_y, 'ro-') 

#   print("data_x") 
#   print(*data_x) 
#   print("data_y") 
#   print(*data_y) 

#   plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
#   plt.axis([0, 6, 0, 20])

   # Сетка на фоне для улучшения восприятия
   plt.grid(True, linestyle='-', color='0.75')
 
   plt.show()
