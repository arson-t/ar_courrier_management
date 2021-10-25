# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OutGoingCourrier(models.Model):
    _name = 'ar.out_going_courier'

    name = fields.Char(string='reference', Required=True)
    numero = fields.Char(string="Numéro")
    type_courrier = fields.Many2one('ar.type_courrier', string='Type courrier', Required=True)
    date_out_going = fields.Datetime(string='Date de depart')
    destinataire = fields.Char(string="Destinataire")
    autre_destinataire = fields.Many2one('hr.employee', string='Autre destinataire')
    objet = fields.Char(string='Objet')
    responsable = fields.Many2many('hr.employee', string='Responsable', Required=True)
    ralatif_courrier = fields.Many2one('ar.courrier', string="Relatif au courrier")
    observation = fields.Text(string='Observation')
    envoie_mail_au_responsable = fields.Boolean(string="Envoi mail au responsable")
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






