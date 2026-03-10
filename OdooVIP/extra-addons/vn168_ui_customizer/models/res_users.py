from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    vn168_primary_color = fields.Char(
        string='Màu chủ đạo',
        default='#714B67',
    )
    vn168_navbar_color = fields.Char(
        string='Màu nền Navbar',
        default='#714B67',
    )
    vn168_navbar_text_color = fields.Char(
        string='Màu chữ Navbar',
        default='#ffffff',
    )
    vn168_button_color = fields.Char(
        string='Màu nút bấm',
        default='#00A09D',
    )
