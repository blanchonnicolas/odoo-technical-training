# -*- coding: utf-8 -*-
from odoo import fields, models #Inherit from global "models" library from odoo

#Here, class EstateProperty is created directly in main folder. 
# However, it is recommended to use folder tree arborescence to ease navigation (and inheritance)

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag" # Dot characters are replaced by Underscore when table is created by ORM
    _description = "Property Tag Table giving information on estate characteristics, for example, cozy or renovated"
    _order = "name" #Sort the entries following name (alphabetically)
    
    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer("Color Index")
