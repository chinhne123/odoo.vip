from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    vn168_primary_color = fields.Char(
        string="Primary Color", 
        config_parameter='vn168.primary_color', 
        default='#714B67'
    )
    vn168_navbar_color = fields.Char(
        string="Navbar Background", 
        config_parameter='vn168.navbar_color', 
        default='#714B67'
    )
    vn168_navbar_text_color = fields.Char(
        string="Navbar Text Color", 
        config_parameter='vn168.navbar_text_color', 
        default='#ffffff'
    )
    vn168_button_color = fields.Char(
        string="Action Button Color", 
        config_parameter='vn168.button_color', 
        default='#00A09D'
    )
