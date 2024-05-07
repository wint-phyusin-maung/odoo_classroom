# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class Ownership(models.Model):
    _name = "estate.ownership"
    _description = "Estate Ownership"

    name = fields.Char(required=True)
    email = fields.Text()
    work = fields.Char()