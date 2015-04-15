# -*- encoding: utf-8 -*-
 
{
    'name' : 'Modulo Tienda de Mascotas',
    'version': '1.0',
    'summary': 'Venta de mascotas',
    'category': 'Tools',
    'description':
        """
Odoo Modulo Web - Tienda de Mascotas
====================================
 
PRINCIPIOS DE ODOO MODULO ODOO WEB
Bienvenido aqui encontrara variedad para elegir su mascota
        """,
    'data': [
        "tienda_mascota.xml",
    ],
    'depends' : ['base','base_translate_tools'],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}