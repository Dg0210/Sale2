from odoo import fields, models

class SaleOrderTag(models.Model):
    _name = 'sale.order.tag'

    name = fields.Char(string='Tag')

