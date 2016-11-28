#!/bin/bash

checkPip () {
  python3 -c "import pip"

  pip=$?

  if [ $pip -eq 0 ]; then
    return 0
  else
    echo 'Please install pip!'
  fi
}

checkPyQt5 () {

  python3 -c "import PyQt5"

  pyqt=$?

  if [ $pyqt -eq 0 ]; then
    return 0
  else
    return 1
  fi

}

checkPip
pipInstalled=$?

checkPyQt5
pyqtInstalled=$?

if [ $pipInstalled -eq 0 ]; then
  #Make sure all fo the libraries are properly installed
  if [ $pyqtInstalled -eq 0 ]; then
    exit
  else
    pip install pyqt5
  fi
else
  echo 'Please install pip to use this program'
fi
