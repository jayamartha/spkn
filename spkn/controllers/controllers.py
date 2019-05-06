# -*- coding: utf-8 -*-
from odoo import http

# class Spkn(http.Controller):
#     @http.route('/spkn/spkn/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spkn/spkn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('spkn.listing', {
#             'root': '/spkn/spkn',
#             'objects': http.request.env['spkn.spkn'].search([]),
#         })

#     @http.route('/spkn/spkn/objects/<model("spkn.spkn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spkn.object', {
#             'object': obj
#         })