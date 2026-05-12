{
    'name': 'Security Services Management',
    'version': '17.0.0.0.1',
    'summary': 'Security Guard Services Management for Odoo 17 Community',
    'category': 'Services',
    'depends': ['base', 'sale_management', 'account', 'hr', 'contacts', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/security_menu.xml',
        'views/security_contract_views.xml',
        'views/security_site_views.xml',
        'views/security_operations_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
