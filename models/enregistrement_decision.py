# -*- coding: utf-8 -*-


import re
from odoo import models, fields, api


class EnregistrementDecision(models.Model):
    _name = 'ar.enregistrement_decision'

    name = fields.Char(string="Name")
    createur = fields.Char(string="Createur")
    num_chrono = fields.Char(string="Num Chrono")
    personnel_concerne = fields.Many2one('hr.employee', string='Personnel Concerné')
    date_decision = fields.Date(string="Date decision")
    date_notification = fields.Date(string="Date Notification")
    responsable_principale = fields.Many2one('hr.employee', string='Responsable principale')
    autre_destinataire = fields.Many2many('hr.employee', string='Autre destinataire')
    intitule_marche = fields.Char(string="intitulé marché")
    objet = fields.Char(string="Objet")
    relatif_a_courier = fields.Char(string="Relatif à courrier")
    observation = fields.Text(string="Observation")