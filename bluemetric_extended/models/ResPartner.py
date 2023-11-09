# -*- coding: utf-8 -*-

from odoo import models, fields

class ResParter(models.Model):
    _inherit = 'res.partner'

    catalog_mailing_date = fields.Datetime(string="Fecha de envio de catalogo")
    tax_status = fields.Datetime(string="Fecha de envio de situacion fiscal")







