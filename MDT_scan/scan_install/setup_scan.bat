@ECHO OFF

ECHO Created by Edmund (ESA)
ECHO ===============================================


ECHO Please make sure you have Python3 and pip3 fully installed

ECHO Setting up packages required for scan and imaging function...

PAUSE

pip install PyVISA
pip install pyvisa-py
pip install Pillow
pip install numpy
pip install PySimpleGUI

ECHO ================
ECHO All done! ...hopefully - didn't have time to learn how to and make integrate catching errors lol


PAUSE