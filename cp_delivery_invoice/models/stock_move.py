# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'

    is_invoiced = fields.Boolean(string="Is Invoiced", default=False, copy=False)
