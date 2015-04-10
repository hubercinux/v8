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

import time
from openerp.osv import osv
from openerp.report import report_sxw


class idea_details(report_sxw.rml_parse):

    def _get_user_names(self, user_ids):
        user_obj = self.pool.get('res.users')
        return ', '.join(map(lambda x: x.name, user_obj.browse(self.cr, self.uid, user_ids.id)))

    def convertir_pe(self, amount, currency="NUEVOS SOLES"):
        amount = float(amount)
        return self.pool.get('ir.translation').amount_to_text(amount, 'pe', currency or 'Nuevo Sol')

    def convertir_hn(self, amount, currency="LEMPIRAS"):
        amount = float(amount)
        return self.pool.get('ir.translation').amount_to_text(amount, 'hn', currency or 'LEMPIRAS')

    def __init__(self, cr, uid, name, context):
        super(idea_details, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_user_names': self._get_user_names,
            'to_text_pe': self.convertir_pe,
            'to_text_hn': self.convertir_hn,
        })


class report_idea_details(osv.AbstractModel):
    _name = 'report.idea.report_parser_idea'
    _inherit = 'report.abstract_report'
    _template = 'idea.report_parser_idea'
    _wrapped_report_class = idea_details

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: