# -*- encoding: utf-8 -*-
 
{
    'name' : 'Modulo Pos Demo',
    'version': '1.0',
    'summary': 'Venta de productos',
    'category': 'Tools',
    'description':
        """
Odoo Modulo Web - POS DEMO
====================================
 
PRINCIPIOS DE ODOO MODULO ODOO WEB
        """,
    'depends' : ['base',],
    'data': [
        "pos_demo_view.xml",
    ],

    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}