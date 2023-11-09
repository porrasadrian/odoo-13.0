# -*- coding: utf-8 -*-

from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    n_invoice = fields.Char(string="N° de factura")
    provider_name = fields.Many2one(string="Nombre del proveedor", comodel_name="res.partner")
    payment_date = fields.Date(string="Fecha de pago")
    type_trip = fields.Selection([('aerial', 'Aereo'), ('land', 'Terrestre'),
                                  ('ship', 'Barco')], string="Tipo de flete")
    customs_arrival_date = fields.Date(string="Fecha de arribo a la aduana")
    warehouse_arrival_date = fields.Date(string="Fecha de pedimento")
    date_capture = fields.Date(string="Fecha de captura en Odoo")

