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


class product_barcode(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(product_barcode, self).__init__(cr, uid, name, context=context)
        self.pricelist=False
        self.quantity=[]
        self.localcontext.update({
            'time': time,
        })

 

class report_product_barcode(osv.AbstractModel):
    _name = 'report.product_barcode.report_barcode_print'
    _inherit = 'report.abstract_report'
    _template = 'product_barcode.report_barcode_print_template'
    _wrapped_report_class = product_barcode

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
