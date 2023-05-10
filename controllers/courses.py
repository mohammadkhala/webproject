# -*- coding: utf-8 -*-
# try something like
def search():
    query = request.vars.query
    if not query:
        courses =[]
    else:
        courses = db(db.courses.name.contains(query) | db.courses.code.contains(query) | db.courses.instructor.contains(query)).select
    return dict(courses=courses ,query=query)

def student():
    query=request.vars.query
    if not query:
        students=[]
    else:
        students=db(db.students.name.contains(query) | db.students.id.contains(query))
    return dict(student=student,query=query)

def details():
    code=request.args(0)
    courses=(db.courses.ALL)
    return dict(courses=courses)


def courses():
    grid =SQLFORM.grid(db.courses,csv=False)
    return dict(grid=grid)
