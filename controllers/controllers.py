# -*- coding: utf-8 -*-
# from odoo import http


# class DataEntryQuote(http.Controller):
#     @http.route('/data_entry_quote/data_entry_quote', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/data_entry_quote/data_entry_quote/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('data_entry_quote.listing', {
#             'root': '/data_entry_quote/data_entry_quote',
#             'objects': http.request.env['data_entry_quote.data_entry_quote'].search([]),
#         })

#     @http.route('/data_entry_quote/data_entry_quote/objects/<model("data_entry_quote.data_entry_quote"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('data_entry_quote.object', {
#             'object': obj
#         })
