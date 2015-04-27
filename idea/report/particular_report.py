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

from openerp import api, models

class idea_report(models.AbstractModel):
    _name = 'report.idea.report_idea_print_particular' # es el nombre del reporte que se mostrara en el formulario pestaña imprimir

    def get_formato(self, val):
        return val

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('idea.report_idea_print_particular')
        
        idea_obj = self.env['idea.demo'] #para que docs tome otra clase de otro objeto
        select_idea = idea_obj.browse(self.ids)  #para que docs tome  este valor

        docargs = {
            'get_formato': self.get_formato,
            'doc_ids': self.ids, #lista de identificadores de los registros docs, ver clase PosInvoiceReport de point_of_sale/report
            'doc_model': report.model, #Model es el modelo o clase para los registros docs 
            #'docs': self.env[report.model].browse(self.ids), # Otra forma es agregando la linea 32 y 33  y docs toma la forma sigueinte:
            'docs': select_idea ,#registros para el informe actual
        }
        return report_obj.render('idea.report_idea_print_particular', docargs)