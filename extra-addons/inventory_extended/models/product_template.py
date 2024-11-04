from odoo import fields, models, _, api


class Product(models.Model):
    _inherit = "product.template"
    unique_id = fields.Char("Unique ID", required=True)
    all_fields = fields.Char(
        string='All', compute='_compute_all', search='_search_all')

    _sql_constraints = [
        ('unique_id_unique', 'UNIQUE (unique_id)', _("ID must be unique!")),
    ]

    @api.depends('unique_id', 'name', 'barcode')
    def _compute_all(self):
        for product in self:
            product.all_fields = f"{product.unique_id} {product.name} {product.barcode}"

    def _search_all(self, operator, value):
        return ['|','|', ('unique_id', operator, value), ('name', operator, value), ('barcode', operator, value)]
    