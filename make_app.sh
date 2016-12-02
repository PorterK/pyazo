#!/bin/bash
pyinstaller -F -w --distpath="./dist" -p "./modules/requests" App.py
