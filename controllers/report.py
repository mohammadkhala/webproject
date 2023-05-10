import csv


def analytics():
    # Count number of students enrolled in each course
    student_counts = db.studentsreg.courseId.count()
    course_enrollments = db(db.studentsreg).select(db.courses.name, student_counts,
                                                   left=db.courses.on(db.studentsreg.courseId == db.courses.code),
                                                   groupby=db.courses.name,
                                                   orderby=~student_counts)
    # Create enrollment report in CSV format
    with open('enrollment_report.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Course Name', 'Number of Enrollments'])
        for row in course_enrollments:
            writer.writerow([row.courses.name, row._extra[student_counts]])

    # Count number of times each course has been added to student's schedules
    schedule_counts = db.studentsreg.courseId.count()
    course_popularity = db(db.studentsreg).select(db.courses.name, schedule_counts,
                                                  left=db.courses.on(db.studentsreg.courseId == db.courses.code),
                                                  groupby=db.courses.name,
                                                  orderby=~schedule_counts)
    # Create popularity report in CSV format
    with open('popularity_report.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Course Name', 'Number of Schedule Additions'])
        for row in course_popularity:
            writer.writerow([row.courses.name, row._extra[schedule_counts]])

    # Render reports in the view
    return dict(course_enrollments=course_enrollments, course_popularity=course_popularity)
