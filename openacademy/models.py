# -*- coding: utf-8 -*-
 
from openerp import models, fields, api
 
class openacademy_curso(models.Model):
    _name = 'openacademy.curso'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()