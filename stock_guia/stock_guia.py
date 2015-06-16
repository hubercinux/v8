# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 S&C (<http://salazarcarlos.com>).
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


from openerp import api, fields, models, _


import logging
_logger = logging.getLogger(__name__)


class stock_guia(models.Model):
    _name ='stock.guia'

    name = fields.Char(string='Nombre')
    sequence_id = fields.Many2one('ir.sequence', string="Secuencia")
    warehouse_id = fields.Many2one('stock.warehouse', string="Almacen")


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    name_default = fields.Char(string='Nombre original')
    guia_id = fields.Many2one('stock.guia', string="Guia remision")

    @api.model
    def create(self, vals):        
        res = super(stock_picking, self).create(vals)
        res.name_default = res.name
        return res    

