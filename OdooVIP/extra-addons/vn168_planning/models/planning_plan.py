from odoo import models, fields, api

class PlanningPlan(models.Model):
    _name = 'planning.plan'
    _description = 'Planning'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Planning Name', required=True, tracking=True)
    date_start = fields.Date(string='Start Date', required=True, tracking=True)
    date_end = fields.Date(string='End Date', required=True, tracking=True)
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user, tracking=True)
    slot_ids = fields.One2many('planning.slot', 'plan_id', string='Planning Slots')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
