from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'open.academy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    # duration = fields.Float(digits=(16, 2), help="Duration in days")
    seats = fields.Integer(string="Seats")
    instructor_id = fields.Many2one(comodel_name='res.partner', string="Instructor")
    course_id = fields.Many2one(comodel_name='open.academy.course', string="Course", required=True)
    attendee_ids = fields.Many2many(comodel_name='res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute="_taken_seats")
    end_date = fields.Date(string="End Date", )

    @api.depends("seats", "attendee_ids")
    def _taken_seats(self):
        for session in self:
            if session.attendee_ids and session.seats:
                session.taken_seats = (len(session.attendee_ids) / session.seats) * 100
            else:
                session.taken_seats = False

    @api.onchange("seats", "attendee_ids")
    def ge_message_for_user(self):
        for session in self:
            if session.seats < 0:
                return {'warning': {
                    'title': _("Validation"),
                    'message': "Must Seats largest Than 0"
                }}
            if session.seats < len(session.attendee_ids):
                raise ValidationError("Must seats Largest Than Attendees")

    # @api.constrains("seats", "attendee_ids")
    # def get_validation(self):
    #     if self.seats > 10:
    #         raise ValidationError("The Place Is Small")

    @api.constrains('instructor_id', 'attendee_ids')
    def check_instructor_attendee(self):
        for session in self:
            if session.instructor_id and session.instructor_id in session.attendee_ids:
                raise exceptions.ValidationError("A person cannot be an instructor and attendee of the same session.")
