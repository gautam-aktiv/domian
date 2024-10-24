# -*- coding: utf-8 -*-
{
    'name': 'Domain Practice',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'description':
        """
        a custom module for practice on diffrent usage of domain.
        """,
    'depends': [
        'contacts',
        'sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/category_hierarchy_report.xml',
        'reports/category_hierarchy_report_template.xml',
        'wizards/category_hierarchy_wizard.xml',
        'views/product_template_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
