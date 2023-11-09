# -*- coding: utf-8 -*-

from odoo import models, fields


class BluemetricPurchase(models.Model):
    _name = 'bluemetric.arribos'
    _description = 'Modulo para arribos de productos'

    n_invoice = fields.Char(string="N° de factura")
    provider_name = fields.Many2one(string="Nombre del proveedor",comodel_name="res.partner")
    payment_date = fields.Date(string="Fecha de pago")
    type_trip = fields.Selection([('aerial', 'Aereo'), ('land', 'Terrestre'),
                                        ('ship', 'Barco')], string="Tipo de flete")
    customs_arrival_date = fields.Date(string="Fecha arribo aduana")
    warehouse_arrival_date = fields.Date(string="Fecha arribo almacén")
    date_capture = fields.Date(string="Fecha de captura en Odoo (Almacén)")



