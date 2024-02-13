from datetime import datetime

hours = 24
minutes = 60
seconds = 60

current_datetime = datetime.now()
formatted_time = current_datetime.strftime('%d %m %Y')
dob_str = input("Enter your DOB in Day Month Year (DD MM YYYY): ")
dob = datetime.strptime(dob_str, '%d %m %Y')
dob_in_days = (current_datetime - dob)

# Access the days component of the timedelta
days_difference = dob_in_days.days
# Convert days to minutes and seconds
hours_difference = days_difference * hours
minutes_difference = days_difference * hours * minutes
seconds_difference = days_difference * hours * minutes * seconds

print(f"Your date of birth in days: {days_difference}")
print(f"Your date of birth in hours: {hours_difference}")
print(f"Your date of birth in minutes: {minutes_difference}")
print(f"Your date of birth in seconds: {seconds_difference}")

# day = 7715
# hours = day * 24
# minutes = hours * 60
# sec = minutes * 60 
# print(hours, minutes, sec)
