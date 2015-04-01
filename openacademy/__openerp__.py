# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        modulo con fines educativos""",

    'description': """
        Para fines eduactivos
    """,

    'author': "Ing. Javier Salazar Carlos ",
    'website': "http://www.salazarcarlos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report.xml',
        'templates.xml',        
        'views/report_openacademy.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}