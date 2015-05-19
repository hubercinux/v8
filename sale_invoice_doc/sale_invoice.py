# -*- encoding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (c) 2014 KIDDYS HOUSE SAC. (http://kiddyshouse.com).
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import api, fields, models, _
from openerp.exceptions import except_orm, Warning, RedirectWarning

import logging
_logger = logging.getLogger(__name__)

class sale_order(models.Model):
    _inherit = 'sale.order'
    
    ruc_dni = fields.Char(string='RUC/DNI',size=32, states={'manual':[('readonly',True)], 'progress':[('readonly',True)],'done':[('readonly',True)]}, )
    
    @api.multi
    def onchange_partner_id(self, partner_id):
        if not partner_id:
            return {'value': {'partner_invoice_id': False, 'partner_shipping_id': False,  'payment_term': False, 'fiscal_position': False, 'ruc_dni': False}}        
        val =  super(sale_order, self).onchange_partner_id(partner_id)        
        value = val['value']
        #_logger.error("MI wwwww: %r", value)
        partner = self.env['res.partner'].browse(partner_id)
        value.update({'ruc_dni': partner.doc_number })
        return {'value': value}

    @api.onchange('ruc_dni')
    def onchange_ruc_dni(self):
        value = {}
        if self.ruc_dni:
            partner_id = self.env['res.partner'].search([('doc_number','=', self.ruc_dni)])
            if partner_id:
                self.partner_id = partner_id
            else:
                raise Warning('Cliente no registrado en el sistema')
        else:
            self.partner_id =  False
            self.partner_shipping_id = False
            self.payment_term = False
            self.fiscal_position = False

    @api.model
    def _prepare_invoice(self, order, lines):    
        invoice_vals = super(sale_order, self)._prepare_invoice(order,lines)
        invoice_vals.update({
                'ruc_dni': order.ruc_dni or '', #agregado para que el RUC/DNI se elejido en la sale_order se muestre en el invoice
            })
        return invoice_vals
    

class account_invoice(models.Model):
    _inherit = 'account.invoice'
    ruc_dni = fields.Char(string='RUC/DNI',size=32, states={'paid':[('readonly', True)], 'open':[('readonly', True)], 'cancel':[('readonly',True)]},)

    @api.multi
    def onchange_partner_id(self, type, partner_id, date_invoice=False, payment_term=False, partner_bank_id=False, company_id=False):        
        val = super(account_invoice, self).onchange_partner_id(type, partner_id, date_invoice, payment_term, partner_bank_id, company_id)                
        result = val['value'] 
        partner = self.env['res.partner'].browse(partner_id)    
        #_logger.error("MI wwwww: %r", self.partner_id.doc_number) 
        if partner_id:
            result.update({
                   'ruc_dni': partner.doc_number or partner.parent_id.doc_number,# agregado nuevos cambios                   
                })
        else:
            result.update({
                   'ruc_dni': False,# agregado nuevos cambios                   
                })
        return {'value': result}
    


