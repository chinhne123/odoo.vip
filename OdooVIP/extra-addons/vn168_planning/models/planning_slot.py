from odoo import models, fields, api
from datetime import timedelta

class PlanningSlot(models.Model):
    _name = 'planning.slot'
    _description = 'Planning Slot'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_datetime'

    name = fields.Char(string='Activity', required=True, tracking=True)
    plan_id = fields.Many2one('planning.plan', string='Planning Reference', ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', string='Resource', required=True, tracking=True)
    start_datetime = fields.Datetime(string='Start DateTime', required=True, tracking=True)
    end_datetime = fields.Datetime(string='End DateTime', required=True, tracking=True)
    duration = fields.Float(string='Duration (Hours)', compute='_compute_duration', store=True)
    color = fields.Integer(string='Color Index')
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('done', 'Completed'),
    ], string='Status', default='draft', tracking=True)

    @api.depends('start_datetime', 'end_datetime')
    def _compute_duration(self):
        for slot in self:
            if slot.start_datetime and slot.end_datetime:
                diff = slot.end_datetime - slot.start_datetime
                slot.duration = diff.total_seconds() / 3600.0
            else:
                slot.duration = 0.0

    def action_publish(self):
        self.state = 'published'

    def action_complete(self):
        self.state = 'done'
