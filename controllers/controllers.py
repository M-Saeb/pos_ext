# -*- coding: utf-8 -*-
from odoo import http


class PosExt(http.Controller):
    @http.route('/pos_ext/pos_ext/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/pos_ext/pos_ext/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('pos_ext.listing', {
            'root': '/pos_ext/pos_ext',
            'objects': http.request.env['pos_ext.pos_ext'].search([]),
        })

    @http.route('/pos_ext/pos_ext/objects/<model("pos_ext.pos_ext"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pos_ext.object', {
            'object': obj
        })
