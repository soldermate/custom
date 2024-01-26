#!/bin/bash

echo "Installing odoo dependencies.."

cd ./odoo && sed -n -e '/^Depends:/,/^Pre/ s/ python3-\(.*\),/python3-\1/p' debian/control | sudo xargs apt-get install -y

