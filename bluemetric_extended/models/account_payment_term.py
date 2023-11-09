# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    for_products = fields.Boolean(string='Uso para productos')
