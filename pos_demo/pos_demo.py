# -*- encoding: utf-8 -*-
from openerp import models, fields, api

class pos_demo(models.Model):
    _name = 'pos.demo'
   
    name = fields.Char(string='Producto')
    descripcion = fields.Text(string='Descripcion')
