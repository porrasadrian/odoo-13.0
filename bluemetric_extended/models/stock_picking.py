# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'stock.picking'

    pago_dhl = fields.Selection([('pay', 'Pagado'), ('not_pay', 'No pagado')], string="Pago DHL", default='not_pay')
