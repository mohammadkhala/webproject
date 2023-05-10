# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Schedules'), False, URL('regs', 'schedules'), []),
    (T('Add Scehdule'), False, URL('regs', 'addSchedule'), []),
    (T('Courses'), False, URL('regs', 'courses'), []),
    (T('Add Course'), False, URL('regs', 'addCourse'), []),
    (T('rooms'), False, URL('regs', 'room'), []),
    (T('my Schedule'), False, URL('regs', 'StudentSchedule'), []),
    (T('report'), False, URL('report', 'analytics'), []),
    (T('Completed Prerequisites'), False, URL('coursereg', 'completed_prerequisites'), []),



]

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')) 
    ]
