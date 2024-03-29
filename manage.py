#!/usr/bin/env python
import os
import sys
import logging

APP_NAME = "jeffreyvwong"

APP_DIR = os.path.abspath(os.path.dirname(__file__))
SITE_DIR = os.path.abspath(os.path.join(APP_DIR, ".."))
PARENT_DIR = os.path.abspath(os.path.join(SITE_DIR, ".."))
STATIC_PATH = os.path.abspath(os.path.join(PARENT_DIR, "static"))

def main():
    ENVIRON_MODULE = ".".join(["config.settings", APP_NAME])
    os.environ['DJANGO_SETTINGS_MODULE'] = ENVIRON_MODULE
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
