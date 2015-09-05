# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _
import time
import openerp.addons.decimal_precision as dp


import logging
_logger = logging.getLogger(__name__)


class stock_location(models.Model):
	_inherit = 'stock.location'

	usage=fields.Selection(selection_add=[('ajuste','Ajuste Inventario')])

class stock_move(models.Model):
	_inherit = 'stock.move'

	ajuste_move_id = fields.Many2one('stock.ajuste', string='Ajuste relacionado', ondelete='cascade')

class stock_ajuste_line(models.Model):
	_name = 'stock.ajuste.line'

	product_id = fields.Many2one('product.product', string="Producto", required=True)
	product_uom_qty = fields.Float(string="Cantidad", digits_compute=dp.get_precision('Product Unit of Measure'), required=True)
	ajuste_id = fields.Many2one('stock.ajuste', string="Ajuste", required=True, ondelete='cascade')

class stock_ajuste(models.Model):
	_name = 'stock.ajuste'
	_order = 'date desc'

	concept_selec = [
		('ingreso','Ingreso por ajuste de inventario'),
		('salida', 'Salida por ajuste de inventario'),
	]

	edit_states = {'done':[('readonly',True)], 'cancel':[('readonly',True)]}

	@api.model
	def _default_location_source(self):
		location_id = False
		location_xml_id = 'location_ajuste_inventario'		
		try:
			location_model, location_id = self.env['ir.model.data'].get_object_reference('stock_ajuste', location_xml_id)			
		except (Exception, ValueError):
			location_id = False
		return location_id

	name = fields.Char(string="Nombre", default="/")
	description = fields.Char(string="Descripción", states=edit_states)
	user_id = fields.Many2one('res.users', string="Usuario", select=True, default= lambda self: self.env.user)
	location_id = fields.Many2one('stock.location', string="Ubicación de origen", default=_default_location_source, states=edit_states)
	location_dest_id = fields.Many2one('stock.location', string="Ubicación destino", required=True, states=edit_states)
	date = fields.Datetime(string="Fecha", required=True, select=True, default= fields.Datetime.now(), states=edit_states)
	concepto = fields.Selection(concept_selec, string="Concepto", select=True, required=True, states=edit_states)
	move_line_ids = fields.One2many('stock.move', 'ajuste_move_id', string="Movimientos relacionados", states=edit_states)
	ajuste_line_ids = fields.One2many('stock.ajuste.line', 'ajuste_id', string="Productos para ajustes", states=edit_states)
	state = fields.Selection([('draft','Nuevo'),('done','Realizado'),('cancel','Cancelado')], string="Estado", readonly=True, required=True, default='draft')
	
	@api.multi
	def _prepare_move(self,line):
		data = {
				'name': self.name,
				'date': self.date,
				'date_expected': self.date,
				'product_id': line.product_id.id,
				'product_uom': line.product_id.uom_id.id,
				'product_uom_qty': line.product_uom_qty,
				'location_id': self.location_id.id if self.concepto=='ingreso' else self.location_dest_id.id,
				'location_dest_id': self.location_dest_id.id if self.concepto == 'ingreso' else self.location_id.id,
				'state': 'draft',
				'ajuste_move_id': self.id,
			}
		return data
	
	@api.multi
	def _move_ajuste_line(self, line):
		move_id = None
		move_id = self.env['stock.move'].create(self._prepare_move(line))			
		self.pool.get('stock.move').action_done(self._cr,self._uid, move_id.id, self._context)
		#_logger.error("El valor de SECUENCIA es: %r", move_id)
		return move_id

	@api.multi
	def button_validar(self):
		for line in self.ajuste_line_ids:
			self._move_ajuste_line(line)			
		self.state = 'done'		

	@api.one
	def button_cancel(self):
		if self.move_line_ids:
			for move in self.move_line_ids:
				if move.state == 'done':
					raise exceptions.ValidationError("No puede eliminar éste registro, antes debe anular los movimientos vinculados")
		self.state = 'cancel'

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].get('ajuste.inventario') or '/'
		res = super(stock_ajuste, self).create(vals)
		return res
		
	@api.one
	def unlink(self):
		if self.state not in ('draft'):
			raise exceptions.ValidationError("No puede eliminar éste registro. Antes debe estar en estado borrador")
		return super(stock_ajuste, self).unlink()

