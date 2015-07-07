# -*- encoding: utf-8 -*-
from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class pos_demo(models.Model):
    _name = 'pos.demo'
   
    name = fields.Char(string='Producto')
    descripcion = fields.Text(string='Descripcion')

    @api.model
    def button_confirmar(self):
    	#_logger.error("MI wwwww: %r", self)
    	self.write({'descripcion': 'HOLA MUNDO' })
    	_logger.error("MI wwwww: %r", self.env.context)
    	return True

