from datetime import datetime, timedelta
from gluon.tools import Mail
import os
# Set up email
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = '201166@ppu.edu.ps'
mail.settings.login = '201166@ppu.edu.ps:ypuyqmvffplsyuon'


def check_deadline_notifications():
    # Retrieve the upcoming deadlines from your database or any other data source
    upcoming_deadlines = db(db.deadlines.deadline_date > datetime.now().date()).select()

    for deadline in upcoming_deadlines:
        # Calculate the time remaining until the deadline
        time_remaining = deadline.deadline_date - datetime.now().date()

        # Check if the deadline is approaching within a specified time threshold (e.g., 24 hours)
        if time_remaining < timedelta(days=1):
            # Get the relevant recipient email address from the database or user details
            recipient_email = deadline.student.email

            # Compose the email message
            subject = f"Upcoming Deadline: {deadline.title}"
            message = f"Dear student,\n\nThis is a reminder that the deadline for {deadline.title} is approaching. Please take necessary actions before the deadline.\n\nBest regards,\nThe Course Registration System"

            # Send the email notification
            mail.send(to=recipient_email, subject=subject, message=message)



def msg():
    subject = 'Hello from web2py'
    message = 'This is the body of the email.'
    to_email = 'mohammadkhallaf2002@gmail.com'

    mail.send(to=[to_email],
              subject=subject,
              message=message)


