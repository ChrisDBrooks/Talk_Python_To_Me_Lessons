import datetime

def print_header():
	print('------------------------')
	print('     BIRTHDAY APP       ')
	print('------------------------')
	print()

def get_birthday_from_user():
	print('Tell us when you were born: ')
	year = int(input('Year [YYYY]: '))
	month = int(input('Month [MM]: '))
	day = int(input('Day [DD]: '))

	birthday = datetime.datetime(year, month, day)
	return birthday
	# datetime is the module we imported .datetime is the sub module 
	
def compute_days_between_dates(orginal_date, now):
	date1 = now
	date2 = datetime.datetime(now.year, orginal_date.month, orginal_date.day)
	change_in_time = date1 - date2
	days = int(change_in_time.total_seconds() / 60 / 60 /24)
	return days


def print_birthday_information(days):
	if days < 0:
		print('Your birthday is in {} days'.format(-days))
	elif days > 0:
		print('You already had your birthday this year! {} days ago'.format(days))
	else:
		print('Happy birthday!!')

def main():
	print_header()
	bday = get_birthday_from_user()
	now = datetime.datetime.now()
	number_of_days = compute_days_between_dates(bday, now)
	print(number_of_days)
	print_birthday_information(number_of_days)

main()