# -*- coding: utf-8 -*-
{
    'name': "Facturación Versión 4.0",

    'summary': """
        Modifica el módulo de facturación para la versión 4.0""",

    'description': """
        Añade una restricción al campo de costo para evitar el costo 0.0 en las facturas y modifica el campo descuento para que nop pueda modificarse
    """,

    'author': "Wonderbrands",
    'website': "https://wonderbrands.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoice',
    'version': '12.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/message_wizard.xml',
    ],
}