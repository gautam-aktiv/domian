# -*- coding: utf-8 -*-
#
{
    'name': 'Sales Price Suggestion',
    'version': '17.0.1.0.0',
    'category': 'Sales/Sales',
    'description':
        """
        This Module Suggest Best Price for every
         sale order line according to price list.
        """,
    'depends': [
        'sale',
        'sale_management',

    ],
    'data': [
        'views/product_pricelist_view.xml',
        'views/sale_order_views.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
