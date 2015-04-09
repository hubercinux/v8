# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import models, fields, api, _

from openerp.exceptions import except_orm, Warning, RedirectWarning

import logging
_logger = logging.getLogger(__name__)


class idea_demo(models.Model):
    _name = 'idea.demo'

    @api.one
    @api.depends('n1', 'n2')
    def compute_total(self):        
        self.resultado = self.n1 + self.n2

    name = fields.Char(string='Nombre', required=True, readonly=True, default='/')
    cliente_id = fields.Many2one('res.partner', string="Cliente", domain=[('customer', '=', True)])
    description	= fields.Text('Observacion')
    n1 = fields.Integer(string='Numero 1')
    n2 = fields.Integer(string='Numero 2')
    operacion = fields.Selection([('suma', 'Sumar'),('restar','Restar')])
    resultado = fields.Float(compute='compute_total')
    state = fields.Selection([('draft', 'Nuevo'),('done','Realizado'),('cancel','Anulado')],default='draft')
    user_id = fields.Many2one('res.users', string="Usuario", default = lambda self: self.env.user, readonly=True)
    date = fields.Date(default=fields.Date.today , string='Fecha')

    @api.multi
    def confirmar(self):        
        #_logger.error("PINCKING id1: %r", self) 
        self.write({'state': 'done' })
        return True
    @api.one
    def anular(self):
        return self.write({'state': 'cancel' })
        
    @api.multi
    def borrador(self):  
    	#_logger.error("PINCKING id1: %r", self)      
        self.state = 'draft'

    @api.one
    def unlink(self):
        if self.state not in ('draft', 'cancel'):
        	raise Warning('No puedes eliminar un registo en estado Realizado, debes de Anual primero')
        return super(idea_demo, self).unlink()

    @api.onchange('cliente_id')
    def onchange_cliente_id(self):
    	#_logger.error("AL CAMBIAR: %r", self.cliente_id.name) 
        if self.cliente_id:
	        self.description = "Estimado %s" % (self.cliente_id.name or "") + ' Bienvenido'
        else:
            self.description = ''

    @api.model
    def create(self, vals):
        #_logger.error("MOSTRANDO CONTENIDO CREATE(): %r", vals)
        vals['name'] = self.env['ir.sequence'].get('idea.demo') or '/'
        res = super(idea_demo, self).create(vals)
        #_logger.error("MOSTRANDO RES: %r", res.name)
        return res
         





