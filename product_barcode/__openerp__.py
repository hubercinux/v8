# -*- coding: utf-8 -*-
{
    'name': "Product Barcode",

    'summary': """
        Permite imprimir el codigo de barra de un producto""",

    'description': """
        Imprime el codigo de barra
    """,

    'author': "Ing. Javier Salazar Carlos ",
    'website': "http://www.salazarcarlos.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','report','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report.xml',
        'wizard/print_barcode_wizard.xml',
        'views/report_barcode.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}