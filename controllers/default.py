# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def display_form():
    form = FORM('Your name:', INPUT(_name='name'), INPUT(_type='submit'))
    return dict(form=form)


def index():
    
    courses = db.executesql("SELECT * FROM courses", as_dict=True)

    return dict(courses=courses)

def list_students():

    students = db.executesql("SELECT * FROM students", as_dict=True)

    return dict(students=students)

def addStudentForm():

    form = SQLFORM(db.students)
    if form.process().accepted:
       response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)

def students():
    grid = SQLFORM.grid(db.students)

    return dict(grid=grid)


def add_user():

    name = request.vars['name']
    email = request.vars['email']

    return locals()
    

def addSchedule():

    form = SQLFORM(db.courseSchedules)
    if form.process().accepted:
       response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)

def courses():

    grid = SQLFORM.grid(db.courses)

    return dict(grid=grid)

def addcourse():


    form = SQLFORM(db.courses)
    if form.process().accepted:
       response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)


def addStudent():

    if request.vars['firstName']:
        first_name = request.vars['firstName']
        last_name = request.vars['lastName']
        email = request.vars['email']

        db.executesql("INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)", placeholders=(first_name,last_name, email))
    else:
        redirect(URL('addStudentForm'))

    return locals()

def details():

    if request.vars['id']:
        id = request.vars['id']
        students = db.executesql("SELECT * FROM students WHERE id=" + id, as_dict=True)

    return dict(student=students[0], students=students)


def delete():

    if request.vars['id']:
        id = request.vars['id']

        db.executesql("DELETE FROM students WHERE id=" + id)
    
    redirect(URL('list_students'))


# ---- API (example) -----
@auth.requires_login()
def manage_users():
    grid = SQLFORM.grid(db.auth_user)
    return locals()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
