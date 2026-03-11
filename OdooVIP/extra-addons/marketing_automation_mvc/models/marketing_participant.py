from odoo import models, fields  # pyre-ignore[21]

class MarketingParticipant(models.Model):
    _name = 'mvc.marketing.participant'
    _description = 'Marketing Campaign Participant'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    
    campaign_id = fields.Many2one('mvc.marketing.campaign', string='Campaign', required=True, ondelete='cascade')
    current_activity_id = fields.Many2one('mvc.marketing.activity', string='Current Activity')
    
    state = fields.Selection([
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('opt_out', 'Opted-Out')
    ], string='Status', default='running')
