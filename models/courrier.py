# -*- coding: utf-8 -*-


import re
from odoo import models, fields, api


class Courrier(models.Model):
    _name = 'ar.courrier'

    name = fields.Char(string='Reference courrier', required=True)
    type_courrier = fields.Many2one('ar.type_courrier', string='Type courrier')
    input_form_creator = fields.Many2one('res.users', string='Input form creator')
    date_time_arrived = fields.Datetime(string='Arrived date')
    date_courrier = fields.Datetime(string='Date courrier')
    expeditor = fields.Char(string='Expeditor')
    object_courrier = fields.Char(string='Object')
    responsible = fields.Many2one('hr.employee', string='Responsible', required=True)
    other_destinator = fields.Many2many('hr.employee', string='Other destinator')
    write_create_form = fields.Datetime(string='date create')
    priority = fields.Selection([
        ('normal', 'normal'),
        ('urgent', 'urgent'),
        ('very_urgent', 'very urgent')], string='Priority', default='normal')
    objervation = fields.Text(string='Observation')
    color = fields.Integer("color", compute="_set_color_kanban")
    testaaa = fields.Boolean(string="test", default=True)
    response = fields.Selection([('yes', 'yes'), ('no', 'no')], default='no')
    transmission = fields.Selection([
        ('trans_receptionniste', 'récéptionniste'),
        ('trans_secretaire', 'Transmission SPDG'),
        ('traitement_dg', 'Traitement DG'),
        ('scan_spdg', 'Scan SPDG'),
        ('dispatching', 'Dispatch physique'),
    ], default='trans_receptionniste')
    necessite_reponse = fields.Selection([('oui', 'Oui'), ('nom', 'Non')], string="Necessite une réponcse")
    state = fields.Selection([('draft', 'Brouillon'), ('confirm', 'Confirmer'), ('send_mail', 'Mail envoyée'),
                              ('mail_received', 'Mail réçu')], string="Status", default="draft")

    @api.depends('priority')
    def _set_color_kanban(self):
        for rec in self:
            if rec.priority == 'normal':
                rec.color = 0
            if rec.priority == 'urgent':
                rec.color = 3
            if rec.priority == 'very_urgent':
                rec.color = 1

    def btn_confirm(self):
        pass

    def send_mail(self):
        pass
