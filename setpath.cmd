@echo off
@title Portable Jekyll

SET PATH=%~dp0ruby\bin;%~dp0devkit\bin;%~dp0git\bin;%~dp0devkit\mingw\bin;%~dp0curl\bin;%~dp0winscp;%PATH%;
SET SSL_CERT_FILE=%~dp0curl\bin\cacert.pem

:: Header
echo Welcome to Portable Jekyll
echo.

:: now bring current sessions to cmd with /k args (stay)
call cmd /k
