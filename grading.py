def gradingStudents(grades):
    new_grade = []
    for grade in grades:
        i = grade % 5
        if grade < 38 or grade % 5 == 0:
            grade_new = grade
        elif i in [1, 2]:
            grade_new = grade
        else:
            grade_new = grade + (5 - i)
        new_grade.append(grade_new)
    return new_grade
