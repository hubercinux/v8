# -*- encoding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (c) 2015 S&c. (http://salazarcarlos.com).
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

import urllib
import re

import logging
_logger = logging.getLogger(__name__)





def get_url(url):
    """Return a string of a get url query"""
    try:
        import urllib
        objfile = urllib.urlopen(url)
        rawfile = objfile.read()
        objfile.close()
        return rawfile
    except ImportError:
        raise Exception ('Error: Unable to import urllib !')
    except IOError:
        raise Exception ('Error: Web Service [%s] does not exist or it is non accesible !' % url)



class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def _type_doc(self):
        doc = [
            ('1','DOCUMENTO NACIONAL DE IDENTIDAD (DNI)'),
            ('6','REGISTRO UNICO DE CONTRIBUYENTES (RUC)'),
            ('4','CARNET DE EXTRANJERIA'),
            ('7','PASAPORTE'),
            ('A','CEDULA DIPLOMATICA DE IDENTIDAD'),
            ]
        return doc

    doc_type = fields.Selection(selection='_type_doc',string="Tipod de Doc.",default='1')
    doc_number = fields.Char('RUC/DNI ',size=32)

    _sql_constraints = [
        ('doc_number_uniq', 'unique(doc_number)', 'Numero de documento ya existe!')
        ]

    @api.onchange('doc_number')
    def onchange_doc_number(self):        
        #_logger.error("MI wwwww: %r", api.onchange('doc_number'))
        if self.doc_number:
            if self.doc_type in ('6') and len(self.doc_number) == 11:
                self.ref = self.doc_number
                self.vat = 'PER' + self.doc_number #PARA VALIDAR RUC DEBE DE INICIAR CON PER
                self.vat_subjected = True        

            elif self.doc_type in ('1') and len(self.doc_number) == 8:     

                dni= self.doc_number
                #---------------------

                url='http://aplicaciones.pronabec.gob.pe/b18/postula/registro?__RequestVerificationToken=8uZps7DLpSQzvgqYMQkUmnq7-Se6i1KsPwOfwj7MPPgPE-L59q1DjCGqHBxQM5SghWYkOOv6ROXCwtPy71tsY1q968F_yHuHp1KjugMLPm01&numero_documento='+dni
                data = get_url(url)                
                res_partner = re.findall('''<input class="form-control required" id="nombre_completo" name="nombre_completo" readOnly="true" type="text" value=".*" />''', data)
                for d in res_partner:
                    name_partner =  (d[116:-4])
                    n = name_partner.split()    
                    #_logger.error("wennnnnnnnn----: %r", name_empresa)                    
                    if len(n)==4:
                        self.name = (n[2] + ' ' +  n[3]+ ' ' + n[0] + ' ' +  n[1]) 
                        #res['value']['apellidopaterno'] = (n[2])
                        #res['value']['apellidomaterno'] = (n[3])
                        #res['value']['nombres'] = (n[0] + ' ' + n[1])
                    if len(n)==3:
                        self.name = (n[1] + ' ' +  n[2]+ ' ' + n[0])
                        #res['value']['apellidopaterno'] = (n[1])
                        #res['value']['apellidomaterno'] = (n[2])
                        #res['value']['nombres'] = (n[0])
                    if len(n)==6 and n[2]=='DE':
                        self.name = (n[2] + ' ' +  n[3]+ ' ' + n[4]+ ' ' + n[5]+ ' ' + n[0]+ ' ' + n[1])
                        #res['value']['apellidopaterno'] = (n[2]+ ' ' + n[3]+ ' ' + n[4])
                        #res['value']['apellidomaterno'] = (n[5])
                        #res['value']['nombres'] = (n[0]+ ' ' + n[1])

                    if len(n)==6 and n[2]!='DE':
                        self.name = (n[2] + ' ' +  n[3]+ ' ' + n[4]+ ' ' + n[5]+ ' ' + n[0]+ ' ' + n[1])
                        #res['value']['apellidopaterno'] = (n[2])
                        #res['value']['apellidomaterno'] = (n[3]+ ' ' + n[4]+ ' ' + n[5])
                        #res['value']['nombres'] = (n[0]+ ' ' + n[1])
                
                self.ref = self.doc_number
                
        else:
            self.street = False
            self.name = False
        

                            
                           
   
 