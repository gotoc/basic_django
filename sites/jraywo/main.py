#!/usr/bin/env python
import os
import sys
import logging

APP_NAME = "jraywo"

def main():
    ENVIRON_MODULE = ".".join(["config.settings", APP_NAME])
    os.environ['DJANGO_SETTINGS_MODULE'] = ENVIRON_MODULE
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

    
