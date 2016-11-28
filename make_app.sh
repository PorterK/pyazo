#!/bin/bash
pyinstaller -F -w --hidden-import=PyQt5 App.py
