{
    'name': 'VN168 Planning',
    'version': '1.0',
    'category': 'Operations/Planning',
    'summary': 'Standard Planning Module for VN168',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/planning_plan_views.xml',
        'views/planning_slot_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
