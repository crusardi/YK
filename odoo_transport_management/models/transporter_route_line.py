# -*- coding: utf-8 -*-

from odoo import fields, models

class TransporterRouteLine(models.Model):
    _name = 'transporter.route.line'
    _rec_name = 'source_location'

    transporter_id = fields.Many2one(
        'res.partner',
        string='Transporter',
    )
    route_id = fields.Many2one(
        'transporter.route',
        string='Transporter Route',
    )
    source_location = fields.Many2one(
        'route.location',
        string='Source Location',
        required=True,
    )
    destination_location = fields.Many2one(
        'route.location',
        string='Destination Location',
        required=True,
    )
    distance = fields.Float(
        string='Distance(Km)',
        required=True,
    )
    hour = fields.Float(
        string='Hours',
        required=True,
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
