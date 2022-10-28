# -*- coding: utf-8 -*-
{
    'name': "map_product_cogs_sol",

    'summary': """ Custom solution for cogs value store in order lines""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Techneith Inc",
    'website': "https://www.techneith.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','stock_account','sale','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
