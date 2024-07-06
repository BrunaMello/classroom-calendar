from datetime import timedelta


def calculate_end_date(start_date, end_date_old_programme, holiday_old):
	course_total_hours = 375
	# days old programme: 125
	# days new programme: 100

	# dias entre as duas datas
	weekdays_count = 0 

	while start_date <= end_date_old_programme:
		if start_date.weekday() < 5:
			weekdays_count += 1
		start_date += timedelta(days=1)
		
    # dias de ferias
	weekdays_count -= holiday_old

	total_days_performed_old_programme = weekdays_count
	print(total_days_performed_old_programme)
	remaing_hours_old_programme = (125 - total_days_performed_old_programme) * 3

	days_to_complete_new_programme = round(remaing_hours_old_programme / 4)
	new_date_to_complete = end_date_old_programme
	added_days=0

	while added_days < days_to_complete_new_programme:
		new_date_to_complete +=timedelta(days=1)
		if new_date_to_complete.weekday() < 4:
			added_days += 1


	return (new_date_to_complete, days_to_complete_new_programme, total_days_performed_old_programme)