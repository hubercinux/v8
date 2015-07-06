# -*- encoding: utf-8 -*-
from openerp import models, fields, api

class pos_demo(models.Model):
    _name = 'pos.demo'
   
    name = fields.Char(string='Producto')
    descripcion = fields.Text(string='Descripcion')

    @api.one
    def confirmar(self):        
        _logger.error("PINCKING id1: %r", self) 
        #self.write({'state': 'done' })
        return {'hola':Mundo}
