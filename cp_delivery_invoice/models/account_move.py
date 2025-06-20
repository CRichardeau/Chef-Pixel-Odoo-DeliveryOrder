# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def button_cancel(self):
        res = super().button_cancel()
        for line in self.invoice_line_ids:
            if line.stock_picking_ids:
                for stock in line.stock_picking_ids:
                    for move in stock.move_ids_without_package:
                        move.write({"is_invoiced": False})
        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    stock_picking_ids = fields.Many2many(
        'stock.picking', string='Delivery Order Number')

    def unlink(self):
        for line in self:
            if line.stock_picking_ids:
                for stock in line.stock_picking_ids:
                    for move in stock.move_ids_without_package:
                        if line.product_id.id == move.product_id.id:
                            move.write({"is_invoiced": False})
        return super(AccountMoveLine, self).unlink()
