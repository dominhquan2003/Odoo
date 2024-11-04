# -*- coding: utf-8 -*-
# from odoo import http


# class InventoryExtended(http.Controller):
#     @http.route('/inventory_extended/inventory_extended', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_extended/inventory_extended/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_extended.listing', {
#             'root': '/inventory_extended/inventory_extended',
#             'objects': http.request.env['inventory_extended.inventory_extended'].search([]),
#         })

#     @http.route('/inventory_extended/inventory_extended/objects/<model("inventory_extended.inventory_extended"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_extended.object', {
#             'object': obj
#         })
