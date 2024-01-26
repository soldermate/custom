from odoo import fields, models


class EngPart(models.AbstractModel):
    _name = "cad.part"
    _description = "CAD Part"

    cattyboy = fields.Char()

    # This is the new syntax for delegation inheritance
    product_id = fields.Many2one(
        "product.template",
        delegate=True,
        ondelete="cascade",
        required=False
    )