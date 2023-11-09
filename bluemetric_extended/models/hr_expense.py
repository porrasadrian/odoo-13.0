# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.tools import date_utils


class HrExpenseExtended(models.Model):
    _inherit = 'hr.expense'

    def copy_expense(self,default=None):
        default = dict(default or {})
        default['date'] = date_utils.add(self.date, months=1)
        new_log = super(HrExpenseExtended,self).copy(default)
        return {
            'res_model': 'hr.expense',
            'type': 'ir.actions.act_window',
            'context': {},
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': new_log.id,
            'view_id': self.env.ref("hr_expense.hr_expense_view_form").id,
            'target': 'current'
        }


