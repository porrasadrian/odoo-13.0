# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date = fields.Datetime(string="Fecha de seguimiento")
    comments = fields.Text(string="Comentarios")
    prueba = fields.Char(string="Prueba")

    def button_method(self):
        menu_xmlid = "bluemetric_extended.comments_form"
        return {
            'type': 'ir.actions.act_window',
            'name': 'Comentarios',
            'res_model': 'wizard.comments',
            'context': {'default_comments': self.comments},
            "views": [[self.env.ref(menu_xmlid).id, "form"]],
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

class WizardComments(models.TransientModel):
    _name = 'wizard.comments'

    comments = fields.Text(string="Comentarios")
