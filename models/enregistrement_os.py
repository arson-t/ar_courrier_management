# -*- coding: utf-8 -*-


import re
from odoo import models, fields, api

class EnregistrementOs(models.Model):
    _name = 'ar.enregistrement_os'

    name = fields.Char(string="Name")
    type_courrier = fields.Many2one('ar.type_courrier', string="type courrier")
    createur = fields.Char(string="Createur")
    num_chrono = fields.Char(string="Num Chrono")
    date_os = fields.Date(string="Date Os")
    numero_os = fields.Char(string="Numéro Os")
    date_notification_os = fields.Date(string="Date Notification OS")
    titulaire = fields.Char(string="Titulaire")
    num_marche = fields.Char(string="Numéro marché")
    autre_destinataire = fields.Char(string="Autre Destinataire")
    objet = fields.Char(string="Objet")
    responsable = fields.Many2one('hr.employee', string='Responsable')
    autre_responsable = fields.Many2many('hr.employee', string="Autre Responsable")
    relatif_courier = fields.Many2one('ar.courrier', string="relatif à courrier")
    state = fields.Selection([('draft', 'Brouillon'), ('confirm', 'Confirmer'), ('send_mail', 'Mail envoyée'),
                              ('mail_received', 'Mail réçu')], string="Status", default="draft")

    def btn_confirm(self):
        self.write({
            'state': 'confirm'
        })

    def send_mail(self):
        self.write({
            'state': 'send_mail'
        })

    def cancel_tbn(self):
        self.write({
            'state': 'draft'
        })
