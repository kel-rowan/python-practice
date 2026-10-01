import numpy  as np
import matplotlib.pyplot as mpl 
Xt = input("What is the second x value?")
Xo = input("What is the first x value?")
Yt = input("What is the second y value?")
Yo = input("What is the first y value?")
B = input("What is the Y-Intercept? (if unknown you can put 0)")
L1 = input("What is the first value of the x limit? (lowest value the graph can go on the x axis")
L2 = input("What is the second value of the x limit? (highest value the graph can go on the x axis")
L3 = input("What is the first value of the y limit? (lowest value the graph can go on the y axis")
L4 = input("What is the second value of the y limit? (highest value the graph can go on the y axis")
print("As Rise over Run:")
print( int(Yt) - int(Yo), "/", int(Xt) - int(Xo) )
print( "As single digit slope:")
print(int(Yt) - int(Yo) / int(Xt) - int(Xo))

S = int(Yt) - int(Yo) / int(Xt) - int(Xo)
fig, ax = plt.subplots()
ax.set_xlim(int(L1),int(L2))
ax.set_ylim(int(L3), int(L4))

ax.axline((0,int(B)), slope=int(S))


plt.grid(True)

plt.show()