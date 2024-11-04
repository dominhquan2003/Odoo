from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    _order = "name, date_published desc"
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    author_ids = fields.Many2many("res.partner", string="Authors")
    publisher_country_id = fields.Many2one(
        "res.country", string="Publisher Country",
        compute="_compute_publisher_country",
    )
    book_publisher_name = fields.Char(
        string='Book & Publisher Name', compute='_compute_book_publisher_name', search='_search_book_publisher_name')

    @api.depends("publisher_id.country_id")
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    @api.depends('name', 'publisher_id')
    def _compute_book_publisher_name(self):
        for book in self:
            book.book_publisher_name = f"{book.name} ({book.publisher_id.name})"

    def _search_book_publisher_name(self, operator, value):
        return ['|', ('name', operator, value), ('publisher_id.name', operator, value)]

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError(
                    "Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
            return True
