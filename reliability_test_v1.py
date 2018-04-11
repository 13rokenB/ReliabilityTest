#!/home/omega/Desktop/webContents/env/bin/python3
######################################################
#                     NOTES
# 1) Make a function that will tell how much time passed
#    during the currently displayed measurement data. 
#
#
######################################################

#import modules for CGI handling 
import cgi, cgitb
import os, sys
import traceback

cgitb.enable()
_ABSLT_ADR_ = '/home/omega/Desktop/webContents/'
_RELT_WEB_ = '/'
import matplotlib
matplotlib.use('Agg')       
import matplotlib.pyplot as plt
import numpy as np

#os.environ[ 'HOME' ] = '/tmp/'

print("Content-type:text/html\r\n\r\n") #Always include before main html

#os.environ['HOME'] = '/tmp'
#import matplotlib.pyplot as plt

import time

####################CONSTANTS#########################
TIME_FOR_ONE_DATAPOINT = 10 #seconds
##################END CONSTANTS#######################

def getTime(measurmentNumber):
	tempTime = measurmentNumber * TIME_FOR_ONE_DATAPOINT
	timeSpentHr = tempTime//3600
	tempTime = tempTime%3600 
	timeSpentMin = tempTime//60
	tempTime = tempTime%60
	timeSpentSec = tempTime
	
	return [timeSpentHr, timeSpentMin, timeSpentSec]

def plotMe(fromData, toData):
	csvData = np.genfromtxt('dummyData.txt', delimiter=',')
	xCord, yCord, zCord = csvData.transpose()
	timeSpent = getTime(len(xCord))
	tempFromRange = int(fromData)
	tempToRange = int(toData)
	measNum = xCord[(tempFromRange-1):(tempToRange)]
	rdsOnBot = yCord[(tempFromRange-1):(tempToRange)]
	rdsOnTop = zCord[(tempFromRange-1):(tempToRange)]
#	timestp = time.strftime("Testing -- Year: %Y, Month: %m, Day: %d - %Hh : %Mm : %Ss")
	timestp = "testPlot"
	#########################################################################
	#adding text to plot
#	plt.text(3,1, "test", style="italic",bbox = {'facecolor':'white', 'alpha':0.5, 'pad':20})
	#########################################################################
	#set x,y bounds for plot
	plt.axis([tempFromRange-1, tempToRange+1, -.0001, .010])

	#plt.plot([1,2,5,8]) #plot y cordinates only, xme
	#plt.plot([1,2,3,4], [1,4,9,16], 'ko', markersize=2, color='red') #plot points 
	#xCord.append(.5)
	#yCord.append(.5)
	
	#add a grid
	plt.grid(color='b', linestyle='-', linewidth=.5, alpha=.5)		
	
	p1 = plt.plot(measNum, rdsOnBot, 'k^', markersize=10, color='blue')
	p2 = plt.plot(measNum, rdsOnTop, 'ko', markersize=10, color='green')
	plt.plot(measNum,rdsOnTop, '-r', color='green', alpha=-0.5)
	plt.plot(measNum, rdsOnBot, '-r', color='blue', alpha=0.5)
	plt.title('GaN Reliability Trend Over Time')
	plt.ylabel('Resistance')
	plt.xlabel('Measurment Number')
	plt.legend((p2[0], p1[0]), ('rdsOn Bottom', 'rdsOn Top'), loc='upper left', shadow=True)
	#########################################################################
	#save as picture	
	plt.savefig(_ABSLT_ADR_ + 'pic/'+timestp)
	#plt.show()
	#plt.draw()
	#########################################################################
	return [timestp, len(xCord)]

def myFunction():
	#get the 3 col of data stored into 3 lists	
	#xCord, yCord, zCord = getData()


	# Create instance of FieldStorage 
	form = cgi.FieldStorage()
	
	# Get data from fields
	if form.getvalue("fromData"):
		fromData = form.getvalue("fromData")
	else:
		fromData = "1"
	if form.getvalue("toData"):
		toData = form.getvalue("toData")
	else:
		toData = "1"
	
	fileName,measurementNumber = plotMe(fromData, toData)
	################## HTML #####################
	print("<html>")
	print("<head>")
	print('<link href="style.css" type="text/css" rel="stylesheet">')
	print("<title>Reliability Test for GaN</title>")
	print("</head>")
	print("<body>")
	#print("<h2>Hello %s %s</h2>" % (first_name, last_name))
	print("<h2> Reliability Test for GaN </h2>")
	print('<img id="Reliability Test" src="{}.png" alt="Image not avaliable" rotate="45" width="600" hight = "300"  vspace="0" hspace="0">'.format(_RELT_WEB_+'pic/'+fileName))
	print('<p class="container"> &nbsp;&nbsp;&nbsp;&nbsp;The graph illistrated to the left is a real-time reliability assessment of GaN converters. The default bounds for the data are the start and real-time current data points.  </p>')
	timerHr, timerMin, timerSec  = getTime(int(toData))
	print('<p class="timeContainer">To produce the above graph the test was running for '+ str(timerHr)+' hours, '+str(timerMin)+' minutes and '+str(timerSec)+' seconds. </p>')
	print('<p class="timeContainer">The current possible maximum measurment number is ' + str(measurementNumber) +' </p>')
	print("<h4>Data from measurment " + fromData  + " to " + toData + "</h4>")
	print('<form method="post" action="reliability_test_v1.py"')
	print('<p>From: <input type="text" name="fromData"/>&nbsp; &nbsp; To: <input type="text" name="toData"/></p>')

#The follow code for a dropdown box will take too long to load all data points if the number of points is over 100,000	
#	print('<p>From: <select name = "fromData">')
#	for options in range(0,len(xCord)):
#		print('<option value = '+ str(xCord[options]) +' selected>' + str(xCord[options]) +'</option>')
#	print('</select>')
#
#	print('To: <select name = "toData">')
#	for optionsTwo in range(0,len(xCord)):
#		print('<option value = '+ str(xCord[optionsTwo]) +' selected>' + str(xCord[optionsTwo]) +'</option>')
#	print('</select>')
	

	print('<Input type="submit" value="Submit" />')
	print("</form>")
	print("</body>")
	print("</html>")
	################ END HTML ###################

if __name__ == "__main__":
	myFunction()
