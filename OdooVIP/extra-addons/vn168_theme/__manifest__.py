{
    'name': 'VN168 Custom Branding',
    'version': '1.0.1',
    'category': 'Theme/Backend',
    'summary': 'White-label theme for VN168: custom logo, favicon, and backend UI redesign.',
    'description': """
        This module provides full branding for VN168 Enterprise:
        - Replaces Odoo logo and favicon with VN168 assets
        - Renames "Odoo" strings to "VN168" across the UI
        - Redirects /odoo to /vn168
        - Custom SCSS backend theme with Inter font and Blue/Navy color palette
    """,
    'author': 'VN168 Tech Team',
    'website': 'https://vn168.vn',
    'license': 'LGPL-3',
    'depends': ['web'],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'vn168_theme/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            'vn168_theme/static/src/scss/backend_theme.scss',
            'vn168_theme/static/src/js/remove_account_menu.js',
        ],
    },

    'data': [
        'views/web_layout_branding.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

