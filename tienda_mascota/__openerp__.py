{
    'name' : 'Modulo Tienda de Mascotas',
    'version': '1.0',
    'summary': 'Venta de mascotas',
    'category': 'Tools',
    'description':
        """
Odoo Modulo Web - Tienda de Mascotas
====================================
 
Bienvenido aqui encontrara variedad para elegir su mascota
        """,
    'data': [
        "tienda_mascota.xml",
    ],
    'depends' : ['sale_stock'],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}