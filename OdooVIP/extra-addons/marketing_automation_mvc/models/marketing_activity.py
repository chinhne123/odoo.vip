from odoo import models, fields

class MarketingActivity(models.Model):
    _name = 'mvc.marketing.activity'
    _description = 'Marketing Campaign Activity'
    _order = 'sequence, id'

    name = fields.Char(string='Activity Name', required=True)
    campaign_id = fields.Many2one('mvc.marketing.campaign', string='Campaign', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    
    activity_type = fields.Selection([
        ('email', 'Send Email'),
        ('sms', 'Send SMS'),
        ('push', 'Push Notification'),
        ('action', 'Server Action')
    ], string='Activity Type', required=True, default='email')
    
    trigger_type = fields.Selection([
        ('begin', 'Beginning of Campaign'),
        ('time', 'Time Delay'),
        ('action', 'After Another Activity')
    ], string='Trigger', required=True, default='time')
    
    delay_count = fields.Integer(string='Delay Interval', default=1)
    delay_unit = fields.Selection([
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('months', 'Months')
    ], string='Delay Unit', default='days')
