{
    'name': 'Marketing Automation MVC',
    'version': '1.0',
    'category': 'Marketing',
    'summary': 'Basic Marketing Automation Module (MVC Architecture)',
    'description': """
        This module demonstrates the Model-View-Controller (MVC) architecture in Odoo.
        It provides a foundation for a Marketing Automation system, including:
        - Models: Campaign definition
        - Views: Web UI forms and lists
        - Controllers: API/Web endpoint for campaigns
    """,
    'author': 'Antigravity AI',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/marketing_activity_views.xml',
        'views/marketing_participant_views.xml',
        'views/marketing_campaign_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
