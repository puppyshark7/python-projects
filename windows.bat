@echo off
echo ------------------------ 
cd source
echo Would you like to run chatbot.py? (y/n)
set /p Input=Enter Yes or No:
If /I "%Input%"=="y" goto yes
goto no
:yes
python Chatbot.py
:no
echo Would you like to run Calculator.py? (y/n)
set /p Input2=Enter Yes or No:
If /I "%Input2%"=="y" goto yes
goto no
:yes
python Calculator.py
:no
echo Would you like to run Creating Geometric Art.py (y/n)
set /p Input3=Enter Yes or No:
If /I "%Input3%"=="y" goto yes
goto no
:yes
python 'Creating Geometric Art.py'
:no
echo Would you like to run Adventure Game.py (y/n)
set /p Input4=Enter Yes or No:
If /I "%Input4%"=="y" goto yes
goto no
:yes
python 'Adventure Game.py'
:no
echo Would you like to run Dice Game.py (y/n)
set /p Input5=Enter Yes or No:
If /I "%Input5%"=="y" goto yes
goto no
:yes
python 'Dice Game.py'
:no
pause