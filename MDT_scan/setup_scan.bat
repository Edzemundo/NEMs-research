@ECHO OFF

ECHO Created by ESA
ECHO ===============================================


ECHO Please make sure you have Pyhton 3 and pip 3 fully installed

ECHO Setting up packages required for scan and imaging function...

PAUSE

pip install PyVISA
pip install pyvisa-py
pip install Pillow
pip install numpy
pip install tk

ECHO ================
ECHO All done! ...hopfully - didn't have time to learn how to and make integrate catching errors lol


PAUSE