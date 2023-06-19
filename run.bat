@Echo off
title FAST_Check
Pushd "%~dp0"
:loop
python challenge.py
goto loop