# -*- coding: utf-8 -*-
import base64
from odoo import models, fields, api, _
from odoo.exceptions import Warning
from datetime import datetime
import logging
import json
import requests

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    costo_cero = fields.Boolean(string="Costo cero?", compute= "_costo_cero", readonly=True)

    @api.one
    def _costo_cero(self):
        _logger = logging.getLogger(__name__)

        if self.amount_total <= 0.0:
            self.costo_cero = True

            raise Warning(_("El monto total de la factura no puede ser cero. Porfavor corríjalo."))
        else:
            self.costo_cero = False