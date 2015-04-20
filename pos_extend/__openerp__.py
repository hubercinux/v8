# -*- encoding: utf-8 -*-
 
{
    'name' : 'Mount to Text',
    'version': '1.0',
    'author' : 'Ing. Javier Salazar Carlos',
    'category' : 'Point Of Sale',
    'website' : 'https://sysneoconsulting.com',
    'summary': 'Monto a texto',
    'description':
        """
Odoo Modulo Web - Monto a texto
====================================
 
Convierte el monto a texto en el POS
        """,
    'data': [ 
        'views/template.xml',
        'pos_extend.xml',
        ],
    'depends' : ['base','base_translate_tools','point_of_sale',],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}