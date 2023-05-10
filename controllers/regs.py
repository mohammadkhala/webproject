def addCourse():
   form = SQLFORM(db.courses)
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   else:
       response.flash = 'please fill out the form'
   return dict(form=form)


def courses():
   grid =SQLFORM.grid(db.courses,csv=False)
   return dict(grid=grid)

def addSchedule():
   form = SQLFORM(db.courseSchedules)
   if form.process().accepted:
      response.flash = 'form accepted'
   elif form.errors:
      response.flash ='form has erorrs'
   else:
      response.flash = 'please fill out the form'
   return dict(form=form)

def schedules():
   grid = SQLFORM.grid(db.courseSchedules, csv=False)
   return dict(grid=grid)


def addRooms():
   form = SQLFORM(db.rooms)
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   else:
       response.flash = 'please fill out the form'
   return dict(form=form)


def room():
   grid =SQLFORM.grid(db.rooms,csv=False)
   return dict(grid=grid)


def coursesSchedules():
   grid=SQLFORM.grid(db.courses.scheduleID==db.courseSchedules.id,
   fields=[db.courses.name,db.courses.code,db.courses.instructor,db.courses.prerequisites,db.courses.capacity,
   db.courseSchedules.days,db.courseSchedules.startTime,db.courseSchedules.endTime,db.courseSchedules.RoomNo],
   csv=False,editable=False,deletable=False,details=False,create=False,
   selectable=lambda ids:redirect(URL('regs','StudentSchedule',vars=dict(id=ids))))
   return dict(grid=grid)

def StudentSchedule():
   grid=SQLFORM.grid((db.courses.code == db.studentsreg.courseId) & (db.students.student_id==db.studentsreg.studentId),
   fields=[db.students.student_id,db.courses.code,db.courses.name,db.courses.instructor,db.courses.prerequisites,db.courses.capacity,
   db.courseSchedules.days,db.courseSchedules.startTime,db.courseSchedules.endTime,db.courseSchedules.RoomNo],
   csv=False,editable=False,deletable=False,details=False,create=False)
   return dict(grid=grid)
   
