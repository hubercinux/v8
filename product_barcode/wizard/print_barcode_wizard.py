# -*- coding: utf-8 -*-

from openerp import models, fields, api

class product_barcode_wizard(models.TransientModel):
    _name = 'product.barcode.wizard'

    col = fields.Char(string="Columna", required=False)
    row = fields.Char(string="Fila",required=False)

    def print_barcode(self, cr, uid, ids, context=None):
        """
        To get the date and print the report
        @return : return report
        """
        if context is None:
            context = {}
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, ['col','row'], context=context)
        res = res and res[0] or {}        
        datas['form'] = res
        return self.pool['report'].get_action(cr, uid, [], 'product_barcode.report_barcode_print_template', data=datas, context=context)
