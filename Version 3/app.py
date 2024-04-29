'''
Variable Stores are stored locally for each running instance.
'''

from flask import Flask, render_template, request
from main import student_details, courses, sections, years, timeslots, attendance_values
from TemporaryVariableStorage import TemporaryVariable

app = Flask(__name__)

# Initialize Variable Stores (equivalent of React Hooks)
session_details_tvs = TemporaryVariable('session_details_tvs')
attendance_log_tvs = TemporaryVariable('attendance_log_tvs')

# Ensure empty list initialisation if no existing data
if attendance_log_tvs.get_value() is None:
    print("LOLL")
    attendance_log_tvs.set_value([])

# Main Page
@app.route('/')
def index():
    return render_template('index.html', courses=courses, sections=sections, years=years, timeslots=timeslots)

# Session Details Form
@app.route('/submit-session', methods=['POST'])
def submit_session():
    try:
        session_details = {
            'date': request.form['date'],
            'year': int(request.form['year']),
            'class': request.form['class'],
            'section': request.form['section'],
            'timeslot': request.form['timeslot']
        }

        session_details_tvs.set_value(session_details)

        # Get filtered student details based on session_details
        student_details = get_filtered_students(session_details)

        # Pass both session_details and student_details to the template
        return render_template('index.html', courses=courses, sections=sections, years=years, timeslots=timeslots, student_details=student_details, attendance_values=attendance_values)
    
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
# Student Attendance Form
@app.route('/submit-attendance', methods=['POST'])
def submit_attendance():
    try:
        # Access attendance data from the form
        attendance = request.form.getlist('attendance')

        session_details = session_details_tvs.get_value()

        # Access the subset of student details
        subset = get_filtered_students(session_details)

        for i, student in enumerate(subset):
            student['attendance'] = attendance[i]

        attendance_data = {
            'session_details': session_details,
            'attendance_details': subset
        }

        #print(attendance_data)

        # Store the attendance data
        temp = attendance_log_tvs.get_value()
        temp.append(attendance_data)

        print(temp)

        attendance_log_tvs.set_value(temp)

        return render_template('index.html', courses=courses, sections=sections, years=years, timeslots=timeslots)

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

def get_filtered_students(session_details):
    year = session_details['year']
    class_name = session_details['class']
    section = session_details['section']
    subset =  [student for student in student_details if student['year'] == year and student['class'] == class_name and student['section'] == section]
    return sorted(subset, key=lambda x: x['reg_num']) # Sort in Ascending order by Register Number

def main():
    pass
    
if __name__ == '__main__':
    app.run(debug=True)
