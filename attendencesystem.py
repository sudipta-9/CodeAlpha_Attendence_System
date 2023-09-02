class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.attendance_record = []

    def input_attendance(self):
        print("Enter attendance record (1 for present, 0 for absent) for the last 10 weeks:")
        for i in range(10):
            attendance = int(input(f"Week {i + 1}: "))
            self.attendance_record.append(attendance)

    def calculate_attendance_percentage(self):
        total_attendance = sum(self.attendance_record)
        attendance_percentage = (total_attendance / len(self.attendance_record)) * 100
        return attendance_percentage

    def display_attendance(self):
        print("\nAttendance Record for", self.name)
        for i, attendance in enumerate(self.attendance_record):
            print(f"Week {i + 1}: {attendance}")
        attendance_percentage = self.calculate_attendance_percentage()
        print(f"Attendance Percentage: {attendance_percentage:.2f}%")

    def attendance_status(self):
        attendance_percentage = self.calculate_attendance_percentage()
        if attendance_percentage >= 75:
            print("You have a good percentage of attendance.")
        else:
            print("Your attendance is below 75%.")

    def run(self):
        print("Welcome to the Attendance Management System!")
        print("Enter your name:", self.name)
        print("Enter your register number:", self.id_number)
        self.input_attendance()
        self.display_attendance()
        self.attendance_status()


if __name__ == "__main__":
    name = input("Enter your name: ")
    id_number = int(input("Enter your register number: "))
    student = Student(name, id_number)
    student.run()
