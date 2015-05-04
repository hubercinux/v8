# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class product_barcode_wizard(models.TransientModel):
    _name = 'product.barcode.wizard'

    col = fields.Integer(string="Columna", required=True, default=1)
    row = fields.Integer(string="Fila",required=True, default=1)
    qty = fields.Integer(string="Cantidad",required=False, default=1)
    start = fields.Integer(string="Posicion de Inicio",required=True, )

    @api.onchange('col','row')
    def onchange_start(self):
        #_logger.error("updateee: %r", self.sequence_id) 
        if self.col<=3 and self.row<=8:
            self.start = self.row*3 - (3-self.col) 
        else:
            self.start = 1

    @api.multi
    def print_barcode(self):
        datas = {'ids': self._context.get('active_ids')}
        res = self.read(['col','row','qty','start'])
        #_logger.error("PINCKING id1: %r", res)
        res = res and res[0] or {}  
        datas['qtys'] = range(1,res['qty']+1,)
        datas['form'] = res
        #_logger.error("PINCKING id2: %r", datas)  
        return self.env['report'].get_action(self, 'product_barcode.report_barcode_print_template', data=datas)
        #return self.pool['report'].get_action(self._cr, self._uid, [], 'product_barcode.report_barcode_print_template', data=datas, context=self._context)

