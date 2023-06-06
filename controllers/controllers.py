# -*- coding: utf-8 -*-
from odoo import http

# class MethodAccountUpdate(http.Controller):
#     @http.route('/method_account_update/method_account_update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_account_update/method_account_update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_account_update.listing', {
#             'root': '/method_account_update/method_account_update',
#             'objects': http.request.env['method_account_update.method_account_update'].search([]),
#         })

#     @http.route('/method_account_update/method_account_update/objects/<model("method_account_update.method_account_update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_account_update.object', {
#             'object': obj
#         })