"""
@file: feed_HMS.py
@original authors: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@new authors: Quinton Wiley, Omar Alzubbi, Julia Drahozal, Kate Strombom
@date: 2016.03.06
@brief: Feed_HMS class. Used get input from the user and update time.
"""

######################################################################
########################### VALIDATE INPUTS ##########################
######################################################################

# check if time input is valid
def str_input_time_check (string):

		# variables
		is_acceptable = False
		time_in_sec = 0

		# get inputs
		input_hr = int (string[0] + string[1])
		input_min = int (string[3] + string[4])
		input_sec = int (string[6] + string[7])

		# tests:
		# hr, min, and sec within bounds
		if (input_hr > 23 or input_min > 59 or input_sec > 59):
				is_acceptable = False
		# passed!
		else:
				is_acceptable = True
				time_in_sec =  input_hr * 3600 + input_min * 60 + input_sec
		return (is_acceptable, time_in_sec)

# check if date input is valid
def str_input_date_check (string):

		# variables
		is_acceptable = False
		date = [0, 0]

		# get inputs
		input_mo = int (string[0]+string[1])
		input_date = int (string[3]+string[4])

		# tests:
		# month within bounds and date != 0
		if (input_mo > 12 or input_mo == 0 or input_date == 0):
				is_acceptable = False
		# months with 31 days
		elif ((input_mo == 1 or input_mo == 3 or input_mo == 5 or input_mo == 7 or input_mo == 8 or input_mo == 10 or input_mo == 12) and (input_date > 31)):
				is_acceptable = False
	   	# months with 30 days
		elif ((input_mo == 4 or input_mo == 6 or input_mo == 9 or input_mo == 11) and (input_date > 30)):
				is_acceptable = False
		# month with 29 days
		elif (input_mo == 2 and input_date > 29):
				is_acceptable = False
		# passed!
		else:
				is_acceptable = True
				date[0] = input_mo
				date[1] = input_date
		return (is_acceptable, date)

######################################################################
############################# UPDATE TIME ############################
######################################################################

# increment time
def update_time (time):

	time += .1
	return time

# increment date
def update_date (calendar, day):

	day = day + 1
	if (day == 8):
		day == 1
	date = calendar[1]
	calendar[1] = date + 1
	calendar = wrapDate (calendar)
	return (calendar, day)

# wrap date around to next month
def wrapDate (calendar):

	# variables
	mo_31 = [1, 3, 5, 7, 8, 10, 12]
	mo_30 = [4, 6, 9, 11]
	mo_29 = [2]
	mo = calendar[0]
	date = calendar[1]

	# months with 31 days
	if ((mo in mo_31) and (date == 32)):
		mo = x_mo + 1
		date = 1
		# wrap dec to jan
		if (mo == 13):
			mo = 1
	# months with 30 days
	if ((mo in mo_30) and (date == 31)):
		mo = x_mo + 1
		date = 1
	# months with 29 days
	if ((mo in mo_29) and (date == 30)):
		mo = x_mo + 1
		date = 1

	return [mo, date]

# calculate day of week given month and date
def calculateDay (cal):

	# Jan 01 2016 = FRIDAY

	# variables
	mo_31 = [1, 3, 5, 7, 8, 10, 12]
	mo_30 = [4, 6, 9, 11]
	mo_29 = [2]
	mo = cal[0]
	day = cal[1]
	count = 0

	# count days passed
	for i in xrange (mo):

		if ((i + 1) == mo):
			for j in xrange (day):
				count = count + 1
		elif ((i + 1) in mo_31):
			for j in xrange (31):
				count = count + 1
		elif ((i + 1) in mo_30):
			for j in xrange (30):
				count = count + 1
		elif ((i + 1) in mo_29):
			for j in xrange (29):
				count = count + 1

	# calculate day of week
	day = (count + 4) % 7
	if (day == 0):
		day = 7
	return day
