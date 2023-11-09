##############################################################################
#
#
#
#
##############################################################################

{
    'name': 'Bluemetric_extended',
    'version': '13.0.8.0.1',
    'category': 'contactos',
    'summary': "Contactos module extension",
    'author': "Adrian Porras",
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'sale_management',
        'stock',
        'product',
        'account',
        'equipment_service',
        'bluemetric_tools',
        'hr'
        ],

     'data': [
         'security/ir.model.access.csv',
         'views/menu.xml',
         'views/sale_order_line.xml',
         'views/product_template_view.xml',
         'views/res_partner_view.xml',
         'views/sale_order_view.xml',
         'views/equipment_service_view.xml',
         'views/hr_expense_view.xml',
         'views/purchase_order_view.xml',
         'views/account_payment_term.xml',
         'views/account_move.xml',
         'views/stock_picking.xml',
     ],
    'installable': True,
}
