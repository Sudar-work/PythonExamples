 # This is fizzbuzz
import matplotlib.pyplot as plt
for i in range(1,101):
     if i % 3 ==0 and i % 5==0:
         print("Fizzbuzz", end=' ')
     elif i%3 == 0:
         print("Fizz",end=' ')
     elif i%5 ==0:
         print("Buzz",end = ' ')
     else:
         print(i)

x = [k for k in range(1,11)]
y = [j for j in range(1,11)]

plt.plot(x,y)
plt.show()