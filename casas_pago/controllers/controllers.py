# -*- coding: utf-8 -*-
from odoo import http

# class CasasPago(http.Controller):
#     @http.route('/casas_pago/casas_pago/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/casas_pago/casas_pago/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('casas_pago.listing', {
#             'root': '/casas_pago/casas_pago',
#             'objects': http.request.env['casas_pago.casas_pago'].search([]),
#         })

#     @http.route('/casas_pago/casas_pago/objects/<model("casas_pago.casas_pago"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('casas_pago.object', {
#             'object': obj
#         })