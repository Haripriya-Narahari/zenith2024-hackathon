from TemporaryVariableStorage import TemporaryVariable
from datetime import date
import os

attendance_log_vs = TemporaryVariable('attendance_log_tvs')

def get_todays_attendance(attendance_log):
    today = str(date.today())
    attendance_today = []

    for entry in attendance_log:
        session_details = entry['session_details']
        if session_details['date'] == today:
            attendance_today.append(entry)

    return attendance_today


def clean_attendance_data(attendance_today):
    '''
    Create a singular 'day details' list from the session details.
    Remove unnecessary student data.
    '''

    attendance_today_cleaned = {
        'date': str(date.today()),
        'details': []
    }

    for count, entry in enumerate(attendance_today):
        session_details = entry['session_details'] # Dictionary
        attendance_details = entry['attendance_details'] # List of dictionaries

        # Remove redundant session details
        redundant_session_details = ['date']
        for key in redundant_session_details:
            session_details.pop(key)

        # Identify students by UniqueID - Registration Number
        attendance_details_cleaned = {}
        for student in attendance_details:
            unique_id = student['reg_num'] # Can change to any other field - e.g. roll_num
            attendance = student['attendance']
            attendance_details_cleaned[unique_id] = attendance


        attendance_today_cleaned['details'].append({
            'session_details': session_details, 
            'attendance_details': attendance_details_cleaned
        })

    return attendance_today_cleaned


def save_attendance_as_file(attendance_today_cleaned):
    # Get date from data
    date = attendance_today_cleaned['date']

    # Data Path
    data_path = 'AttendanceData/'
    
    if not os.path.exists(data_path):
            os.makedirs(data_path)

    with open(f'{data_path}{date}.txt', 'w') as file:
        file.write(str(attendance_today_cleaned))

def push_to_database(attendance_today):
    # Clean the attendance data
    attendance_today_cleaned = clean_attendance_data(attendance_today)

    save_attendance_as_file(attendance_today_cleaned)


def main():
    # Load all attendance data
    attendance_log = attendance_log_vs.get_value()

    # Merge Attendance Logs from instances

    # Get today's attendance (entire day)
    attendance_today = get_todays_attendance(attendance_log)

    # Save it in the database
    push_to_database(attendance_today)

if __name__ == '__main__':
    main()