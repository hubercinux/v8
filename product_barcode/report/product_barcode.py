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

import logging
_logger = logging.getLogger(__name__)

class product_barcode_print(report_sxw.rml_parse):

    def _product_details(self, data):
        datas = []
        result = {  'name1':'', 'price1':'', 'ean13_1':'',
                    'name2':'', 'price2':'', 'ean13_2':'',
                    'name3':'', 'price3':'', 'ean13_3':'',
                    }

        result1 = { 'name1':'', 'price1':'', 'ean13_1':'',
                    'name2':'', 'price2':'', 'ean13_2':'', 
                    'name3':'', 'price3':'', 'ean13_3':'',
                    }
        q = 1 #Cantidad inicia en 1
        f = 1 # fila menor a la fila de inicio
        fila = data['form']['row'] #NUmero de fila
        columna = data['form']['col'] #NUmero de columna
        qty = data['form']['qty'] #cantidad
        start = data['form']['start'] #inicio

        fil=fila

       # _logger.error("PINCKING id111111: %r", data['form']['row'])
        prod_obj = self.pool.get('product.product')
        prod_id = prod_obj.search(self.cr, self.uid, [('id','in',data['ids']),])
        #for i in range(1,data['form']['qty'] + 1):
        for producto in prod_obj.browse(self.cr, self.uid, prod_id):             
            while f < fila: 
                result1.update({'name1': '', 'price1':'', 'ean13_1':'',})
                result1.update({'name2': '', 'price2':'', 'ean13_2':'',})
                result1.update({'name3': '', 'price3':'', 'ean13_3':'',})
                datas.append(result1)
                f += 1

            while fil == fila:
                columna = 1            
                if ( columna == 1 and q <= qty ):
                    if (fila*3-(3-columna))>= start:
                        result.update({'name1': producto.name, 'price1': producto.lst_price, 'ean13_1':producto.ean13,})
                        q += 1                                            
                    columna += 1

                if (columna == 2 and q <= qty  ):                    
                    if (fila*3-(3-columna))>= start:
                        result.update({'name2': producto.name, 'price2': producto.lst_price, 'ean13_2':producto.ean13,})
                        q += 1                                        
                    columna += 1

                if (columna == 3 and q <= qty ):
                    if (fila*3-(3-columna))>= start:
                        result.update({'name3': producto.name, 'price3': producto.lst_price, 'ean13_3':producto.ean13,})
                        q += 1                               
                fil += 1
                fila += 1
                                            
                #_logger.error("PINCKING id555555555: %r", datas)
                datas.append(result)
                result={'name1':'', 'price1':'', 'ean13_1':'',
                        'name2':'', 'price2':'', 'ean13_2':'',
                        'name3':'', 'price3':'', 'ean13_3':'',
                        }
                if q > qty:
                    break   
                     
        return datas


    def __init__(self, cr, uid, name, context):
        super(product_barcode_print, self).__init__(cr, uid, name, context=context)
        self.pricelist=False
        self.quantity=[]
        self.localcontext.update({
            'time': time,
            'product_details':self._product_details,

        })

class report_product_barcode(osv.AbstractModel):
    _name = 'report.product_barcode.report_barcode_print_template' #Nombre= report.name_module.name_report -> report.xml
    _inherit = 'report.abstract_report'
    _template = 'product_barcode.report_barcode_print_template'#Nombre= name_module.name_template -> views/report_barcode.xml
    _wrapped_report_class = product_barcode_print

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
