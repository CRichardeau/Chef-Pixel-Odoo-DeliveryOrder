# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    stock_picking_ids = fields.Many2many(
        'stock.picking', string='Stock Picking', store=True, compute='_compute_stock_picking_ids')

    @api.depends('order_id', 'order_id.picking_ids')
    def _compute_stock_picking_ids(self):
        for vals in self:
            vals.stock_picking_ids = False
            picking_list = []
            if vals.order_id.picking_ids:
                for picking in vals.order_id.picking_ids:
                    for move in picking.move_ids_without_package:
                        if move.sale_line_id == vals.id and move.picking_id not in picking_list:
                            picking_list.append(move.picking_id)
            if picking_list:
                vals.stock_picking_ids = picking_list

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        for vals in self:
            picking_list = []
            for picking_id in vals.order_id.picking_ids.filtered(lambda x: x.state == 'done'):
                if picking_id.move_ids_without_package:
                    for line in picking_id.move_ids_without_package:
                        if line.id in vals.move_ids.ids and not line.is_invoiced:
                            if picking_id not in picking_list:
                                picking_list.append(picking_id)
                                line.is_invoiced = True
        res['stock_picking_ids'] = [(4, picking.id) for picking in picking_list]
        return res
