from odoo import models, fields


class ScheduledReminder(models.Model):
    _name = 'scheduled.reminder'
    _description = 'Scheduled Reminder'

    description = fields.Text(string='Description', required=True)
    recipients = fields.Many2many('res.partner', string='Recipients')
    user_id = fields.Many2one('res.users', string='Send from')
    scheduled_reminders = fields.One2many('reminder.schedule', 'reminder', string='Scheduled Reminders')


class ReminderSchedule(models.Model):
    _name = 'reminder.schedule'
    _description = 'Reminder Schedule'

    reminder = fields.Many2one('scheduled.reminder', string='Reminder', ondelete='cascade')
    scheduled_time = fields.Datetime(string='Scheduled Time')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    scheduled_reminders = fields.Many2many('scheduled.reminder', string='Scheduled Reminders')




