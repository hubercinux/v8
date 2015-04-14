
# -*- encoding: utf-8 -*-
from openerp import models, fields, api

class tienda_mensaje(models.Model):
    _name = "tienda.mensaje"

    @api.model
    def mostrar_mensaje(self):
        return {"mensaje": "HOLA MUNDO, DESDE LA CLASE mostrar_mensaje]()"}
        

    message = fields.Text(),
    color = fields.Char(size=20),

    @api.model
    def write(self):
    	print self.env.context
        return {"mensaje": "HOLA MUNDO, DESDE LA CLASE mostrar_mensaje]()"}