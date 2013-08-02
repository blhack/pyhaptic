import os
import glob
import sys
import time
import serial
import logging
import random

logging.basicConfig(level=logging.DEBUG)

from pyhaptic import HapticInterface

def find_comm_port():
	comm_port = []
	if os.name == 'posix':
		comm_port = glob.glob('/dev/tty.*')
		comm_port.extend( glob.glob('/dev/ttyACM*'))
		comm_port.extend( glob.glob('/dev/ttyUSB*'))
	elif os.name == 'nt':
		available = []
		for i in range(256):
			try:
				s = serial.Serial(i)
				available.append('COM'+str(i + 1))
				s.close()
			except serial.SerialException:
				pass
		comm_port.extend(available)
	print "Printing current available comm ports.\n"
	for i in comm_port:
		print i
	comm_choice = raw_input("\nPlease choose the full path to the comm port that the haptic controller is connected to:") 
	return comm_choice


def button_handler(option=-1):

	#negative 1 is a default value that will cause the function to do nothing.  I like having default values, but that is just my preference.
	
	if option == 0:

	print "running zero"
	for x in xrange(two_d_display.qry_number_motors()):
		two_d_display.vibrate(x,0,0,1)
		time.sleep(.1)
	print "completed zero"

	if option == 1:

	print "running one"
	number = two_d_display.qry_number_motors()
	for x in xrange(number):
		two_d_display.vibrate(x,0,0,1)
		time.sleep(.1)
	for x in reversed(xrange(number-1)):
		two_d_display.vibrate(x,0,0,1)
		time.sleep(.1)
	print "completed one"

	if option == 2:
	print "running two"
	num_motors = two_d_display.qry_number_motors()

		#I'm not sure what you're doing here, but I think this accomplishes the same thing in a much cleaner way.
		
		for i in range(0,8):
			for x in range(0,num_motors):
	if x % i == i:
		two_d_display.vibrate(x,0,0,1)
			time.sleep(.5)

		time.sleep(.5)

		#now go the other way

		for i in range(7,-1,-1):
			for x in range(0,num_motors):
	if x % i == i:
		two_d_display.vibrate(x,0,0,1)
			time.sleep(.5)
	print "completed two"

	if option == 3:
	print "running three"
	num_motors = two_d_display.qry_number_motors()
	for x in xrange(num_motors):
		two_d_display.vibrate(random.randrange(num_motors),0,0,1)
		time.sleep(.1)
	print "completed three"

	if option == 4:
	print "running four"
	print "completed four"

	if option == 5:
	print "running five"
	print "completed five"

	if option == 6:
	print "running six"
	print "completed six"

	if option == 7:
	print "running seven"
	print "completed seven"

	if option == 8:
	print "running eight"
	print "completed eight"

	if option == 9:
	print "running nine"
	print "completed nine"

if __name__ == '__main__':
	
	two_d_display = HapticInterface(find_comm_port())
	try:
		two_d_display.connect()
	except:
		print "Failed to connect on ..."
		sys.exit(1)
	
	print "enter a number 0-9 to activate that function"
	print "anything else to exit"
	while True:
		comm_choice = sys.stdin.read(1)
		sys.stdin.read(1) #dump the newline char

	if int(comm_choice) in range(0,10):
		button_handler(int(comm_choice))
		else:
			sys.exit(0)
