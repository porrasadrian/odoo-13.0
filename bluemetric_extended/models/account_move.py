# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    estado_republica = fields.Many2one(related='partner_id.state_id', string="Estado de la republica", store=True)
