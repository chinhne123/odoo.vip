from odoo import models, fields, api  # pyre-ignore[21]

class MarketingCampaign(models.Model):
    _name = 'mvc.marketing.campaign'
    _description = 'Marketing Automation Campaign'

    name = fields.Char(string='Campaign Name', required=True)
    active = fields.Boolean(default=True)
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('running', 'Running'),
        ('stopped', 'Stopped'),
        ('completed', 'Completed')
    ], string='Status', default='draft')
    description = fields.Text(string='Description')

    # 2025 Best Practices: Relations & Analytics
    activity_ids = fields.One2many('mvc.marketing.activity', 'campaign_id', string='Activities')
    participant_ids = fields.One2many('mvc.marketing.participant', 'campaign_id', string='Participants')
    
    total_participants = fields.Integer(string='Total Participants', compute='_compute_analytics', store=True)
    success_rate = fields.Float(string='Success Rate (%)', compute='_compute_analytics', store=True)
    
    @api.depends('participant_ids', 'participant_ids.state')
    def _compute_analytics(self):
        for record in self:
            total = len(record.participant_ids)
            record.total_participants = total
            
            completed = len(record.participant_ids.filtered(lambda p: p.state == 'completed'))
            record.success_rate = (completed / total * 100) if total > 0 else 0.0
