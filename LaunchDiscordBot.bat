@echo OFF
title Jril Bot
set CONDAPATH={path to anaconda/miniconda}
set PYTHONAPP={patch to discordAI.py}\discordAI.py
set ENVNAME=textgenCPU

if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=%CONDAPATH%\envs\%ENVNAME%)

echo Activating virtual env...
call %CONDAPATH%\Scripts\activate.bat %ENVPATH%

echo Starting discord bot...
python %PYTHONAPP%

