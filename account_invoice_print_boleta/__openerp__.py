# -*- coding: utf-8 -*-
{
    'name': "Account Print Boleta",

    'summary': """
        Imprime Boleta de Venta""",

    'description': """
        Imprime boleta
    """,

    'author': "Ing. Javier Salazar Carlos ",
    'website': "http://www.salazarcarlos.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','report','account'],
    'data': [
        'view/invoice_print_boleta.xml',
        'report.xml',

    ],
    'demo': [
    ],
}