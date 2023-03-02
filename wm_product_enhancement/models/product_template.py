# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    brand = fields.Char(string='Brand')
    season = fields.Char(string='Season')