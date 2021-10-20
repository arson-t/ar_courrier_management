# -*- coding: utf-8 -*-


from odoo import models, fields, api

class TypeCourrier(models.Model):
	_name = 'ar.type_courrier'

	name = fields.Char(string='Type courrier')
	