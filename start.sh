#!/bin/bash

# Run http://localhost:8069/
# User: admin
# Password : admin

./odoo/odoo-bin --addons-path=./odoo/addons,./custom_addons -u cad -d default
