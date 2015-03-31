# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 SC. (http://salazarcarlos.com).
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

import logging
_logger = logging.getLogger(__name__)

class tipo_documento_sequence_wizard(models.TransientModel):
    _name = "tipo.documento.sequence.wizard"

    def _default_sequence(self):
        recs = self.env['account.invoice'].browse(self._context.get('active_ids'))
        #recs = self.env['account.invoice'].search([('id', '=', recs.id)], )
        #_logger.error("updateee: %r", recs.journal_id.sequence_id.id)
        return recs.journal_id.sequence_id.id

    sequence_id = fields.Many2one('ir.sequence', string='Secuencia', default=_default_sequence)
    next_number = fields.Char(string='Siguiente numero')

    @api.onchange('sequence_id')
    def onchange_sequence_id(self):
        #_logger.error("updateee: %r", self.sequence_id) 
        if self.sequence_id:
            self.next_number = self.sequence_id.number_next_actual


    @api.multi
    def update_sequence(self):
        recs = self.env['ir.sequence'].search([('id', '=', self.sequence_id.id)], )
        #_logger.error("updateee: %r", recs)
        recs.write({'number_next_actual': self.next_number})
        return True    


    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
