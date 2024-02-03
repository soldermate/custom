#!/bin/bash

# Run http://localhost:8069/
# User: admin
# Password : admin

./odoo/odoo-bin --addons-path=./odoo/addons,./custom_addons -u cad -u kicad --db_host="erp-db-1" --db_user="odoo" --db_password="odoo" -d postgres
