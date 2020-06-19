{
    'name': 'Sales Oder Tag',
    'version': '1.0',
    'sequence': 1,
    'depends': [
        'base', 'sale'
    ],
    'data': [
        'views/sale_order_tag_views.xml',
        'views/sale_order_sub_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
