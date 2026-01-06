# Task
# Create a function:
# Copy code
# Python
# check_attendance(login_time)

# Rules
# Login before 9:30 AM → Present
# Login between 9:30–10:00 AM → Late
# After 10:00 AM → Absent

def check_attendance(login_time):
    if  login_time > 9.00 and login_time < 9.30 :
        print("your present..!")
    elif login_time > 9.30 and login_time < 10.00 :
        print("your late..!")
    elif login_time > 10.00 :
        print("absent..!")
    else:
        print("your fired..!")

check_attendance(10.40)