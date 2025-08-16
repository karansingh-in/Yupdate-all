@echo off          
echo(   _                      
echo(  ^| ^|                     
echo(  ^| ^|__  _   _ _ __  _ __ 
echo(  ^| '_ \^| ^| ^| ^| '_ \^| '__^|
echo(  ^| ^| ^| ^| ^|_^| ^| ^|_) ^| ^|   
echo(  ^|_^| ^|_^|\__, ^| .__/^|_^|   
echo(          __/ ^| ^|         
echo(         ^|___/^|_^|         
title karansingh-in
prompt hypr$G
echo.
echo If the cursor is blinking, it indicates the program is actively searching for updates, not frozen.
echo.
echo NOTE : microsoft edge and a few system apps are updated via windows update only or externally via microsoft store.
echo.
winget upgrade --all --silent --accept-source-agreements --accept-package-agreements
pause