{
    'name': 'Scheduled Reminders',
    'version': '1.0',
    'summary': 'Module for creating and managing scheduled reminders',
    'author': 'Your Name',
    'category': 'Tools',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/scheduled_reminder_views.xml',
        'views/reminder_cron_data.xml',
        'security/groups.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
