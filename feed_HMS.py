"""
@file: feed_HMS.py
@author: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@date: 2016.02.14
@brief: Feed_HMS class. Used get input from the user and handle exceptions.
"""

hour_range = [x+1 for x in range(13)] #[1,2,....,12]
minute_range = [x for x in range(60)] #[0,1,2,....,59]
second_range = [x for x in range(60)] #[0,1,2,....,59]

#needs extreme case testing 
def str_input_check(string):
        is_acceptable = False
        time_in_sec = 0
        input_hr = int(string[0]+string[1])
        input_min = int(string[3]+string[4])
        input_sec = int(string[6]+string[7])
        if input_hr>23 or input_min>59 or input_sec>59:
                is_acceptable = False
        else:
                is_acceptable = True
                time_in_sec =  input_hr*3600 + input_min *60 + input_sec
                #print time_in_sec
        
        return (is_acceptable, time_in_sec)

def hour():
	hour = -1
	while hour not in hour_range:
		try:
			hour = input("Please enter the hour (0-12)! : ")
			hour = int(hour)
		except:
			hour = -1
			print ("User entered a non-numeric argument.")
	
	# return hour in the unit of seconds
	return hour*60*60
	
		
def am_pm():
	am_pm = input("Please enter am or pm: ")
	
	while am_pm.lower() != "am" and am_pm.lower() != "pm" :
		am_pm = input("Please enter either am or pm! : ")

	return am_pm	

def minute():
	
	minute = -1
	while minute not in minute_range:
		try:
			minute = input("Please enter the minute (0-60)! : ")
			minute = int(minute)
		except:
			minute = -1
			print ("User entered in a non-numeric argument.")

	# return minute in the unit of seconds	
	return minute*60
		
		
def second():
	second = -1
	while second not in second_range:
		try:
			second = input("Please enter the second (0-60)! : ")
			second = int(second)
		except:
			second = -1
			print ("User entered a non-numeric argument.")
	return second
	
def run():
	h = hour()
	m = minute()
	s = second()
	return h + m + s
	
def run2():
	ap = am_pm()
	return ap

if __name__ == '__main__':
	h = hour()
	ap = am_pm()
	m = minute()
	s = second()
	
	h = (h/60)/60
	m = m/60
	print("Right now it's {0}:{1}:{2},{3}!".format(h,m,s,ap))
