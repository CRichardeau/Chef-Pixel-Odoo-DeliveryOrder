# -*- coding: utf-8 -*-
{
    'name': "Display Delivery number on the Invoice",
    'summary': "This module helps to show the delivery number into the invoice.",
    'description': """Purpose of this module is to show the delivery number based on the product wise 
    in invoice.""",
    'author': "CHEF PIXEL",
    'website': "https://chef-pixel.fr",
    'support': "hello@chef-pixel.fr",
    'category': 'Extra Tools',
    'version': '18.0.1.0.0',
    'depends': ['sale', 'account', 'sale_stock', 'stock'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],
}
