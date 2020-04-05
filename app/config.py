# pylint: disable=line-too-long
"""
Config file, kinda follows the 12Factor app style, but with less relying on environment variables
it contains multiple dictionaries, like default_settings, development_settings,
deployment_settings, each is loaded depending on the type of environment we are running in
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

default_settings = dict(
    SQLALCHEMY_DATABASE_URI='postgresql://adminuser:adminpass@localhost/petsdb',
    SQLALCHEMY_TRACK_MODIFICATIONS=True,

    CSRF_ENABLED = True,
    SECRET_KEY='\xa3p\xfa\xf0s\xef<@\xac\x17t\xa7!\xff\xa0B\x16\xc5\x8590\x8a\xde\xcb',
    DEBUG = True,
)
app_settings = default_settings
