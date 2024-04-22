from odoo import api, fields, models 

class SmtzTodo(models.Model):
    _name = 'smtz.todo'
    _description = 'SmtzTodo'

    name = fields.Char()
    completed = fields.Boolean(default=False)