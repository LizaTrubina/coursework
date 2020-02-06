#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

   # Значения по X и Y, если в данный год родился один математик 
   data_x = []
   with open("x_one.txt") as f:
      for line in f:
         data_x.append(int(line))
         
   data_y = []
   with open("lifespan1.txt") as f:
      for line in f:
         data_y.append(float(line))

# Значения по X и Y, если в данный год родилось больше одного математика (среднее значение) 
   m_data_x = []
   with open("x_many.txt") as f:
      for line in f:
         m_data_x.append(int(line))
         
   mean_data_y = []
   with open("lifespan_mean.txt") as f:
      for line in f:
         mean_data_y.append(float(line))
         
# Значения по Y, если в данный год родилось больше одного математика (max значение)       
   max_data_y = []
   with open("lifespan_max.txt") as f:
      for line in f:
         max_data_y.append(float(line))

# Значения по X и Y, если в данный год родилось больше одного математика (min значение) 
   min_data_y = []
   with open("lifespan_min.txt") as f:
      for line in f:
         min_data_y.append(float(line))

         
   plt.axis([1669 , 1980, 0, 100])
   plt.xlabel("Год")
   plt.ylabel("Продолжительность жизни")
   
   # представляем точки (х,у) кружочками диаметра 10
   plt.plot(data_x, data_y, 'o', color = 'gray')


   plt.plot(m_data_x, mean_data_y, 'o', color = 'green')
   plt.plot(m_data_x, max_data_y, '--', color = 'red')
   plt.plot(m_data_x, min_data_y, '--', color = 'blue')
   
   plt.minorticks_on()
   # Определяем внешний вид линий основной сетки:
   plt.grid(which='major', color = 'k',  linewidth = 1)
   #  Определяем внешний вид линий вспомогательной сетки:
   plt.grid(which='minor', color = 'k',  linestyle = ':')
   
   plt.savefig('ValueDispersion.png', fmt='png')
   plt.show()
   
