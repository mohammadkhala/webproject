def student_completed_prerequisites(course, student_id):
    if not courses.prerequisites:
        return True

    completed_courses = db((db.registration.courses == db.courses.id) &
                            (db.registration.student == student_id) &
                            (db.registration.status == 'completed')).select(db.courses.ALL)
    completed_course_ids = [c.id for c in completed_courses]

    for prereq in course.prerequisites:
        if prereq not in completed_course_ids:
            return False

    return True
def completed_prerequisites():
    student_id = auth.user_id  # get the current student's ID
    student_courses = db(db.studentsreg.studentId == student_id).select(db.studentsreg.courseId)  # get the courses the student is registered for
    completed_courses = [course.courseId for course in student_courses]  # extract the course IDs from the above query
    query = db.courses.prerequisites == None  # query to select courses with no prerequisites
    query |= db.courses.prerequisites.belongs(completed_courses)  # query to select courses with completed prerequisites
    grid = SQLFORM.grid(query, fields=[db.courses.name, db.courses.description, db.courses.instructor, db.courses.capacity, db.courses.scheduleID],
                        headers={'courses.name': 'Name', 'courses.description': 'Description', 'courses.instructor': 'Instructor', 'courses.capacity': 'Capacity', 'courses.scheduleID': 'Schedule'})
    return dict(grid=grid)



def add_course_to_schedule():
    student_id = request.vars.student_id
    course_id = request.vars.course_id

    course = db.courses(course_id)
    if not course:
        return 'Invalid course ID'

    if not student_completed_prerequisites(course, student_id):
        return 'Prerequisites not completed'

    if db(db.registration.student == student_id and db.registration.courses == course_id).count():
        return 'Course already registered'

    db.registration.insert(student=student_id, course=course_id)

    redirect(URL('default', 'index'))

def display_course_schedule():
    student_id = request.vars.studentid

    courses = db((db.courses.code == db.courses) &
                 (db.students.student_id == student_id)).select(db.courses.ALL)

    return dict(courses=courses)

def index():

    courses = db(db.courses).select()


    student_id = request.vars.studentid

    form = SQLFORM.factory(
        Field('courseid', 'integer', label='Course ID'),
        Field('studentid', 'integer', default=student_id, readable=False, writable=False),
        submit_button='Add Course',
    )

    if form.process().accepted:
        response.flash = add_course_to_schedule()
        course_schedule = display_course_schedule()

    return dict(form=form, course_schedule=course_schedule,courses=courses)

def completed_prerequisites():
    student_id = auth.user_id  # get the current student's ID
    student_courses = db(db.studentsreg.studentId == student_id).select(db.studentsreg.courseId)  # get the courses the student is registered for
    completed_courses = [course.courseId for course in student_courses]  # extract the course IDs from the above query
    courses = db(db.courses).select()  # get all the courses in the database
    eligible_courses = []
    for course in courses:
        if not course.prerequisites:  # if the course has no prerequisites, it's eligible
            eligible_courses.append(course)
        else:
            prereq_codes = course.prerequisites.split(', ')  # get a list of prerequisite course codes for the current course
            prereq_completed = all(prereq in completed_courses for prereq in prereq_codes)  # check if all prerequisites have been completed
            if prereq_completed:
                eligible_courses.append(course)
    return dict(courses=eligible_courses)
