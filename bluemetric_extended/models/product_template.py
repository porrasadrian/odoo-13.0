# -*- coding: utf-8 -*-

from odoo import models, fields,api

class ProductsTemplate(models.Model):
    _inherit = 'product.template'

    range = fields.Char(string="Rango", size=15)
    correctness = fields.Char(string="Exactitud", size=10)
    delivery_time = fields.Many2one('account.payment.term',string="Tiempo de entrega")
    common_discount = fields.Selection([('discount_one', '5%'), ('discount_two', '7%'),
                                        ('discount_tree', '10%')], string="Descuento comun")
    special_discount = fields.Selection([('discount_one', '15%'), ('discount_two', '20%')],
                                        string="Descuento especial")
    common_use = fields.Text(string="Uso comun")
    freight_cost = fields.Float(string="% Costo del Flete")
    percent_increase = fields.Float(string="% de Incremento")
    bluemetric_coste = fields.Float(string="Coste")


    @api.onchange('bluemetric_coste','freight_cost','percent_increase')
    def onchange_price_list(self):
        for product in self:
            fleet = product.bluemetric_coste * (product.freight_cost/100)
            subtotal = fleet + product.bluemetric_coste
            increase = subtotal * (product.percent_increase/100)
            product.list_price =increase + subtotal



