# -*- coding: utf-8 -*-
{
    'name': "Chef Pixel Delivery Invoice",
    'summary': "This module helps to show the delivery into the invoice.",
    'description': """Purpose of this module is to show the delivery based on the product wise 
    in invoice lines.""",
    'author': "CHEF PIXEL PVT LTD",
    'website': "https://chef-pixel.fr",
    'category': 'Extra Tools',
    'version': '18.0.1.0.0',
    'depends': ['sale', 'account', 'sale_stock', 'stock'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
