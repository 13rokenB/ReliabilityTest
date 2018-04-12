try:
	from Tkinter import *
except ImportError:
	from tkinter import *

import matplotlib.pyplot as plt
import time

xCord = [1,2,3]
yCord = [1,2,3]

timestp = time.strftime("Testing -- Year: %Y, Month: %m, Day: %d - %Hh : %Mm : %Ss") #save the opperating systems date and time



#########################################################################
#adding text to plot
plt.text(3,1, "test", style="italic",
	bbox = {'facecolor':'white', 'alpha':0.5, 'pad':20})


#########################################################################
#setup for plot


#set x,y bounds for plot
plt.axis([0, len(xCord)+1, 0, len(yCord)+1])

#plt.plot([1,2,5,8]) #plot y cordinates only, x is abratraly picked

#plt.plot([1,2,3,4], [1,4,9,16], 'ko', markersize=2, color='red') #plot points 
xCord.append(.5)
yCord.append(.5)

plt.plot(xCord, yCord, 'ko', markersize=40, color='blue')


plt.plot(xCord, yCord, '-r', '''markersize=30''', color='red', alpha=0.6)

plt.ylabel('y-Lable')
plt.xlabel('x-Lable')

#########################################################################
#save as picture	


plt.savefig(timestp)
#plt.show()
#plt.draw()
#########################################################################


