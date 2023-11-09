from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    fuente = fields.Many2one(related='order_id.source_id', string="Fuente", compute='_compute_fuente_group', store=True)

    @api.depends('order_id.source_id')
    def _compute_fuente_group(self):
        for line in self:
            line.fuente_group = line.order_id.source_id

    equipo = fields.Many2one(related='order_id.team_id', string="Equipo de ventas", compute='_compute_equipo',
                             store=True)

    @api.depends('order_id.team_id')
    def _compute_equipo(self):
        for line in self:
            line.equipo_group = line.order_id.team_id

    date = fields.Datetime(related="order_id.date_order", string="Fecha de cotizacion", compute='_compute_date_group',
                           store=True)

    @api.depends('order_id.date_order')
    def _compute_date_group(self):
        for line in self:
            line.date_group = line.order_id.date_order

    order_group = fields.Many2one('sale.order', string="Pedido para agrupación", compute='_compute_order_group',
                                  store=True)

    @api.depends('order_id')
    def _compute_order_group(self):
        for line in self:
            line.order_group = line.order_id

    quote_group = fields.Many2one('sale.order', string="Presupuesto para agrupación", compute='_compute_quote_group',
                                  store=True)

    @api.depends('order_id', 'order_id.state')
    def _compute_quote_group(self):
        for line in self:
            if line.order_id.state == 'draft':
                line.quote_group = line.order_id

    sent_quote_group = fields.Many2one('sale.order', string="Presupuesto Enviado para agrupación",
                                       compute='_compute_sent_quote_group', store=True)

    @api.depends('order_id', 'order_id.state')
    def _compute_sent_quote_group(self):
        for line in self:
            if line.order_id.state == 'sent':
                line.sent_quote_group = line.order_id

    total_amount = fields.Monetary(string='Total', compute='_compute_total_amount', store=True)

    @api.depends('price_subtotal', 'price_tax')
    def _compute_total_amount(self):
        for line in self:
            line.total_amount = line.price_subtotal + line.price_tax
