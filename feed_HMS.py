#setup time!
#
#



def hour():
	hour = input("Please enter the hour (1-12): ")
	hour = int(hour)
	
	while hour > 12 and hour < 12:
		hour = input("Please enter the hour (1-12)! : ")
		hour = int(hour)
	
	# return hour in the unit of seconds
	return hour*60*60
	
		
def am_pm():
	am_pm = input("Please enter am or pm: ")
	
	while am_pm.lower() != "am" and am_pm.lower() != "pm" :
		am_pm = input("Please enter either am or pm! : ")

	return am_pm	

def minute():
	minute = input("Please enter the minute(s) (1-60): ")
	minute = int(minute)
	while minute > 60 and minute < 0:
		minute = input("Please enter the minute (1-60)! : ")
		minute = int(minute)
	# return minute in the unit of seconds	
	return minute*60
		
		
def second():
	second = input("Please enter the second(s) (1-60): ")
	second = int(second)
	while second > 60 and second < 0:
		second = input("Please enter the second (1-60)! : ")
		second = int(second)
		
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
