# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


{
	'name' : 'Modulo demo idea v8',
	'version' : '1.0',
	'author' : 'Ing. Salazar C. J.',
	'sumary' : 'Modulo de odoo para demo',
	'description' : 'modulo varios demo',
	'depends' : ['base'],
	'data' : [
				'idea_view.xml', 
				'idea_sequence.xml',
				'security/idea_security.xml',
				'security/ir.model.access.csv',
				],
	'installable' : True,
	'aplication' : True,
	
}
