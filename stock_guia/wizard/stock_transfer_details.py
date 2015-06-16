# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-TODAY Salazar Carlos S&C. <http://www.salazarcarlos.com>
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


class stock_transfer_details(models.TransientModel):
    _inherit = 'stock.transfer_details'

    @api.one
    def do_detailed_transfer(self):
        res = super(stock_transfer_details, self).do_detailed_transfer()
        picking = self.env['stock.picking'].browse(self._context.get('active_ids'))
        if picking.guia_id:
            name_guia = self.env['ir.sequence'].get_id(picking.guia_id.sequence_id.id)           
            self._cr.execute("UPDATE stock_picking SET name=%s WHERE id=%s",(name_guia,picking.id) )
            _logger.error("PICKING NAME: %r", name_guia)

        return True


