def coursestudents(students, course):
    return [student.name for student in students if student.attends(course)]