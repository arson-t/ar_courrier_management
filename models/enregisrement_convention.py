# -*- coding: utf-8 -*-


import re
from odoo import models, fields, api


class enregistrementConvention(models.Model):
    _name = 'ar.enregistrement_convention'

    name = fields.Char(string="Name")
    createur = fields.Char(string="Createur")
    num_chrono = fields.Char(string="Num Chrono")
    date_approbation = fields.Date(string="Date d'aprobation")
    date_prevu_fin_execution = fields.Date(string="Date prevu fin exécution")
    num_convention = fields.Char(string="Numéro convention")
    titulaire = fields.Char(string="Titulaire")
    bailleur = fields.Char(string="bailleur")
    objet = fields.Char(string="Objet")
    responsable_projet = fields.Many2one('hr.employee', string="Responsable de projet")
    autre_destinataire = fields.Many2many('hr.employee', string='Autre destinataire')
    relatif_a_courier = fields.Char(string="Relatif à courrier")
    observation = fields.Text(string="Observation")
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

