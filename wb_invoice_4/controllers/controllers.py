# -*- coding: utf-8 -*-
from odoo import http

# class WbInvoice4(http.Controller):
#     @http.route('/wb_invoice_4/wb_invoice_4/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wb_invoice_4/wb_invoice_4/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wb_invoice_4.listing', {
#             'root': '/wb_invoice_4/wb_invoice_4',
#             'objects': http.request.env['wb_invoice_4.wb_invoice_4'].search([]),
#         })

#     @http.route('/wb_invoice_4/wb_invoice_4/objects/<model("wb_invoice_4.wb_invoice_4"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wb_invoice_4.object', {
#             'object': obj
#         })