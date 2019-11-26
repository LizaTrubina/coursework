#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

   # Значения по X
   data_x = []
   with open("1x.txt") as f:
      for line in f:
         data_x.append(line)
   # Значения по Y
   data_y = []
   with open("1y.txt") as f:
      for line in f:
         data_y.append(line)
 

   plt.xlabel("X")
   plt.ylabel("Y")
   # представляем точки (х,у) кружочками диаметра 10
   plt.plot(data_x, data_y, 'r')
 
   # Сетка на фоне для улучшения восприятия
   # plt.grid(True, linestyle='-', color='0.75')
 
   plt.show()
