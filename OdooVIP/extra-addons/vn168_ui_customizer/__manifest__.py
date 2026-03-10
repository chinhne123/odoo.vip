{
    'name': 'VN168 UI Customizer',
    'version': '5.0',
    'category': 'Theme/Backend',
    'summary': 'Tùy chỉnh màu sắc giao diện cá nhân',
    'author': 'VN168',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/ui_custom_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'vn168_ui_customizer/static/src/js/user_menu_color.js',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
