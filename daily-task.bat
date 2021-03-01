@echo off
schtasks /create /tn hoyolab-daily /tr "py %CD%\script.py" /sc daily /st 14:00
