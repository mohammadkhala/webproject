import datetime


db.define_table('courses',
	Field('code', 'string', required=True, notnull=True),
	Field('name', 'string'),
	Field('description', 'string'),
	Field('prerequisites', 'string', 'reference courses',requires=IS_IN_DB(db, 'courses.code', '%(name)s')),
	Field('instructor', 'string'),
	Field('capacity', 'integer'),
	Field('scheduleID', 'integer','reference courseSchedules',requires=IS_IN_DB(db, 'courseSchedules.id', '%(days)s- %(startTime)s - %(endTime)s')),
	primarykey=['code'])

db.define_table('deadlines',
				Field('id','integer',required=True,notnull=True),
				Field('deadline_date','date')
				)
db.define_table('students',
	Field('student_id', 'string'),
	Field('first_name', 'string'),
	Field('last_name', 'string'),
	Field('email', 'string'),
	Field('password', 'string'),
	Field('registration_key','string'),
	Field('reset_password_key','string'),
	Field('registration_id','string'),
	primarykey=['student_id'])

db.define_table('studentsreg',
	Field('id', 'integer', required=True, notnull=True),
	Field('studentId','integer'),
	Field('courseId','string'),
	primarykey=['id'])



db.define_table('rooms',
	Field('code', 'string', required=True, notnull=True),
	primarykey=['code'])


db.define_table('courseSchedules',
	Field('id', 'integer',required=True, notnull=True),
	Field('days', 'string'),
	Field('startTime', 'time', default=datetime.time(0,0)),
	Field('endTime', 'time', default=datetime.time(0,0)),
	Field('RoomNo', 'string', 'reference rooms', requires=IS_IN_DB(db, 'rooms.code', '%(code)s')),
	primarykey=['id']
	) 