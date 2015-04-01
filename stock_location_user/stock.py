# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-2014 (<http://salazarcarlos.com>).
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

#from openerp import models
from openerp import models, fields, api, _

class stock_location(models.Model):
    _name = 'stock.location'
    _inherit = 'stock.location'
    
    user_ids = fields.Many2many('res.users')
    #user_ids = fields.Many2many('res.users','stock_location_user_rel', 'user_id', 'location_id', "Users"),
    
class res_users(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    
    #location_ids = fields.Many2many('stock.location','stock_location_user_rel', 'location_id', 'user_id', 'Locations'),
    location_ids = fields.Many2many('stock.location')
