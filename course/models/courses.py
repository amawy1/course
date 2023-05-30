from odoo import models, fields


class Courses(models.Model):
    _name = "open.academy.course"
    # _description = "Open Academy"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one(string="instructor", comodel_name="res.users")
    session_ids = fields.One2many(
        comodel_name='open.academy.session', inverse_name='course_id', string="Sessions")
