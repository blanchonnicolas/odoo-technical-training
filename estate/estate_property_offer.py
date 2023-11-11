# -*- coding: utf-8 -*-
from odoo import api, fields, models #Inherit from global "models" library from odoo
# api package used for computational functions
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

#Here, class EstateProperty is created directly in main folder. 
# However, it is recommended to use folder tree arborescence to ease navigation (and inheritance)

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer" # Dot characters are replaced by Underscore when table is created by ORM
    _description = "Property offer Table listing buyer offers to the seller with proposed  price and decisions"
    
    price = fields.Float('Offer price')
    status = fields.Selection(
        string='Offer status',
        copy=False,
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="Decision following offer")
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)

    # -------------------------------------------------------------------------
    # COMPUTED VARIABLES WITH INVERSE FUNCTIONS
    # -------------------------------------------------------------------------
    validity = fields.Integer('Leadtime in days', default=7, required=False)
    date_deadline = fields.Date('Date Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    # -------------------------------------------------------------------------
    # COMPUTE METHODS WITH INVERSE FUNCTIONS
    # -------------------------------------------------------------------------
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=+record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=+record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date:
                record.validity = (record.date_deadline - record.create_date.date()).days #
            else:
                record.validity = (record.date_deadline - fields.Date.today()).days

    # -------------------------------------------------------------------------
    # CREATE METHOD THAT TRIGGER STATE CHANGE like it is in WORKFLOW
    # -------------------------------------------------------------------------
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            property = self.env['estate.property'].browse(vals['property_id'])
            property.state = "offer_received"
            for offers_id in property.offer_ids:
                if vals['price'] < offers_id.price:
                    raise UserError("Your offer cannot be considered as it is lower than an existing one")
        return super().create(vals_list)


    # -------------------------------------------------------------------------
    # ACTION METHODS THAT ENSURE THAT trigger offer state update with accept/reject buttons ...
    # -------------------------------------------------------------------------
    def action_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.status"):  #BUG HERE TO FIX : Do not retrieve property_id.offer_ids.state
            raise UserError("An offer for this property has already been accepted")
        return self.write(
            {
                "status": "accepted",
            }
        )

    def action_refuse(self):
        return self.write(
            {
                "status": "refused",
            }
        )

