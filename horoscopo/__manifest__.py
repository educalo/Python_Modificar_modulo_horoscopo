# -*- coding: utf-8 -*-
{
    'name': "horoscopo",

    'summary': "Modificacion de un modulo existente",

    'description': """
    Este modulo añade funcionalidad a la aplicación de contactos con 3 nuevos campos:
        - Fecha de nacimiento
        - Edad (calculado automaticamente)
        - Signo de zodiaco (calculado automaticamente)
    """,

    'author': "Eduardo",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # dependencia de la base y del modulo contacts
    'depends': ['base', 'contacts'],

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

