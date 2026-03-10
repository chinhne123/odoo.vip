from odoo import http
from odoo.http import request

class MarketingCampaignController(http.Controller):

    @http.route('/marketing/campaigns', type='http', auth='public')
    def list_campaigns(self, **kwargs):
        # Fetch active running campaigns
        campaigns = request.env['mvc.marketing.campaign'].sudo().search([('state', '=', 'running')])
        
        # Render a simple HTML response (or this could be a QWeb template)
        html_content = "<h1>Active Marketing Campaigns</h1><ul>"
        for campaign in campaigns:
            html_content += f"<li>{campaign.name} (Ends: {campaign.end_date or 'N/A'})</li>"
        html_content += "</ul>"
        
        return html_content

    @http.route('/api/marketing/campaigns', type='jsonrpc', auth='user')
    def api_list_campaigns(self, **kwargs):
        # JSON endpoint for API access
        campaigns = request.env['mvc.marketing.campaign'].search_read(
            [('state', '=', 'running')], 
            ['name', 'start_date', 'end_date', 'total_participants', 'success_rate']
        )
        return {'status': 200, 'data': campaigns}

    @http.route('/api/marketing/participants', type='jsonrpc', auth='user')
    def api_list_participants(self, campaign_id, **kwargs):
        # Fetch participants for a specific campaign
        participants = request.env['mvc.marketing.participant'].search_read(
            [('campaign_id', '=', int(campaign_id))],
            ['name', 'email', 'state']
        )
        return {'status': 200, 'data': participants}
