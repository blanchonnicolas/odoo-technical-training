{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'views/estate_property_views.xml', #This file contains List/Entry/Search views and associated Actions for estate_property model
        'security/ir.model.access.csv', #This file contains security rules to access the data (Chapter 5)
        'views/estate_menus.xml', #This file contains 3 levels of menus, and calls associated action; Therefore it is important to load this file after xml file defining action
    ],
    "installable": True,
    'license': 'LGPL-3',
}
