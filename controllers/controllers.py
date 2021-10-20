# -*- coding: utf-8 -*-
# from odoo import http


# class ArCourrierManagement(http.Controller):
#     @http.route('/ar_courrier_management/ar_courrier_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ar_courrier_management/ar_courrier_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ar_courrier_management.listing', {
#             'root': '/ar_courrier_management/ar_courrier_management',
#             'objects': http.request.env['ar_courrier_management.ar_courrier_management'].search([]),
#         })

#     @http.route('/ar_courrier_management/ar_courrier_management/objects/<model("ar_courrier_management.ar_courrier_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ar_courrier_management.object', {
#             'object': obj
#         })
