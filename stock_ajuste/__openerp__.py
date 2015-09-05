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


{
	'name' : 'Ajuste de Inventario',
	'version' : '0.1',
	'author' : 'Ing. Javier Salazar Carlos',
	"website" : "http://salazarcarlos.com",
	'summary' : 'Opción para ajuste de inventario',
	'description' : 'Permite gestionar los ajustes de inventario en los almacenes',
	'depends' : [
			'base',
			'stock',
			'product',
			],
	'data' : [
				#'security/idea_security.xml',
				#'security/ir.model.access.csv',
				'views/stock_ajuste.xml',
				'sequence.xml',
				'location_data.xml',
				],
	'installable' : True,
	'aplication' : True,
	
}