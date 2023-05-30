from odoo import models, fields, api
from datetime import datetime
from odoo.tools import email_split


class ReminderCron(models.Model):
    _name = 'reminder.cron'
    _description = 'Reminder Cron'

    @api.model
    def _send_email_reminder(self):
        current_datetime = fields.Datetime.now()
        reminders = self.env['scheduled.reminder'].search([])

        for reminder in reminders:
            recipients = [email_split(recipient.email)[0] for recipient in reminder.recipients]
            user = reminder.user_id.email
            subject = 'Reminder: {}'.format(reminder.description)
            body = 'This is a reminder for: {}'.format(reminder.description)
            email_from = ['@gmail.com']

            mail_values = {
                'subject': subject,
                'body': body,
                'email_from': user,
                'email_to': recipients,
            }
            print('#####', user)
            print('%%%%%%%%', recipients)
            print('!!!!!', subject)
            print('@@@@@', body)

            self.env['mail.mail'].create(mail_values).send()


class ScheduledReminder(models.Model):
    _inherit = 'scheduled.reminder'

    @api.model
    def create(self, values):
        reminder = super(ScheduledReminder, self).create(values)
        self.env['reminder.cron']._send_email_reminder()
        return reminder
