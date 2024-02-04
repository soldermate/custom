# -*- coding: utf-8 -*-
{
    'name': "KiCad",

    'summary': "Module to control KiCAD symbols and footprints",

    'description': """
        References to KiCAD symbols and footprints are tracked in this module.
        The symbols and footprints are referenced by products.
    """,

    'author': "Cameron Carslake",
    'website': "https://www.switchlabs.com.au",
    'license': "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/kicad_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    'application': True
}