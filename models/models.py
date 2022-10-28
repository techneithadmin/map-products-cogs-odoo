# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrdeInheritedTechneith(models.Model):

    _inherit = 'sale.order'

    sales_rep_name = fields.Char(related='user_id.partner_id.name',store=True)

class ResPartnerCategoryInheritedTechneith(models.Model):

    _inherit = 'res.partner.category'
    parent_category_string = fields.Char(string='parent path' ,compute='_get_category_string' ,store=True)

    @api.depends('parent_path')
    def _get_category_string(self):
        for rec in self:
            rec.parent_category_string = rec.name_get()[0][1]
