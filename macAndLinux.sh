#!/bin/bash

cd source
echo ------------------------------------------------------
echo Would you like to run Chatbot?
read input
if [[ "$input" == *"y"* ]]; then
	python3 Chatbot.py
	echo -------------------
fi
echo Would you like to run Calculator?
read input2
if [[ "$input2" == *"y"* ]] ; then
	python3 Calculator.py
	echo --------------------
fi
echo Would you like to run Creating Geometric Art?
read input3
if [[ "$input" == *"y"* ]]; then
	python3 'Creating Geometric Art.py'
	echo --------------------
fi
echo Would you like to run Adventure Game?
read input4
if [[ "$input" == *"y"* ]]; then
	python3 'Adventure Game.py'
	echo --------------------
fi
echo Would you like to run Dice Game?
read input5
if [[ "$input5" == *"y"* ]]; then
	python3 'Dice Game.py'
	echo --------------------
fi