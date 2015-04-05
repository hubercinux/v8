# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class idea_wizard(models.TransientModel):
    _name = 'idea.wizard'

    def _default_name(self):
        recs = self.env['idea.demo'].browse(self._context.get('active_ids'))
        #recs = self.env['account.invoice'].search([('id', '=', recs.id)], )
        #_logger.error("updateee: %r", recs.journal_id.sequence_id.id)
        return recs.name

    name = fields.Char(string="Nuevo Nombre",default=_default_name)

    @api.one
    def update_name(self):
    	if self.name:
	    	recs = self.env['idea.demo'].browse(self._context.get('active_ids'))
	    	#_logger.error("updateee: %r", recs.name) 
	    	recs.name = self.name