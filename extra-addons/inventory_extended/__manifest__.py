{
    'name': "Inventory Extended",
    'description': "Adding location field, and unique number for searching",
    'author': "Chủm",
    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/product_view_invisible.xml',
    ],
}
