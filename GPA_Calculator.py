def get_grade_point(grade):
    grade_points = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
    return grade_points.get(grade, 0.0)

def calculate_gpa(credit_hours, grade_points):
    total_grade_points = sum(credit_hours[i] * grade_points[i] for i in range(len(credit_hours)))
    total_credit_hours = sum(credit_hours)
    return total_grade_points / total_credit_hours

def main():
    num_subjects = int(input("Enter the number of subjects: "))

    course_names = []
    credit_hours = []
    grades = []

    for _ in range(num_subjects):
        course_name = input("Enter course name: ")
        credit_hour = float(input("Enter credit hours for {}: ".format(course_name)))
        grade = input("Enter grade for {}: ".format(course_name))

        course_names.append(course_name)
        credit_hours.append(credit_hour)
        grades.append(grade)

    print("\nSubject-wise GPA:")
    print("{:<15} {:<15} {:<10}".format('Course', 'Credit Hours', 'GPA'))
    print("-" * 40)

    total_credit_points = 0
    for i in range(num_subjects):
        grade_point = get_grade_point(grades[i])
        gpa = credit_hours[i] * grade_point
        total_credit_points += gpa
        print("{:<15} {:<15} {:<10}".format(course_names[i], credit_hours[i], gpa/credit_hours[i]))

    cgpa = total_credit_points / sum(credit_hours)

    print("\nCGPA: {:.2f}".format(cgpa))

if __name__ == "__main__":
    main()

    