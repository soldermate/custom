from odoo import fields, models


class kicadSymbol(models.Model):
    _name = "kicad.symbol"
    _description = "Electronic CAD symbol in kicad format"

    name = fields.Char()