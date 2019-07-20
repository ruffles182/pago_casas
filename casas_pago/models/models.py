# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Calle(models.Model):
    _name = 'casas_pago.calle'
    _rec_name = 'nombre'

    nombre = fields.Char('calle')

class Casa(models.Model):
    _name = 'casas_pago.casa'

    numero = fields.Integer('numero')
    calle = fields.Many2one('casas_pago.calle', 'nombre')
    estatus = fields.Boolean(string='Pagado')