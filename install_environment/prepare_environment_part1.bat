:::::::::::::::::::::::::::::::::::::::::
:: Automatically check & get admin rights
:::::::::::::::::::::::::::::::::::::::::
@echo off
CLS 
ECHO.
ECHO =============================
ECHO Running Admin shell
ECHO =============================
 
:checkPrivileges 
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges ) 
 
:getPrivileges 
if '%1'=='ELEV' (shift & goto gotPrivileges)  
ECHO. 
ECHO **************************************
ECHO Invoking UAC for Privilege Escalation 
ECHO **************************************
 
setlocal DisableDelayedExpansion
set "batchPath=%~0"
setlocal EnableDelayedExpansion
ECHO Set UAC = CreateObject^("Shell.Application"^) > "%temp%\OEgetPrivileges.vbs" 
ECHO UAC.ShellExecute "!batchPath!", "ELEV", "", "runas", 1 >> "%temp%\OEgetPrivileges.vbs" 
"%temp%\OEgetPrivileges.vbs" 
exit /B 
 
:gotPrivileges 
::::::::::::::::::::::::::::
:START
::::::::::::::::::::::::::::
setlocal & pushd .
SETLOCAL ENABLEEXTENSIONS

set pythonExe=python-3.6.3.exe

:payload
::Assumes bat starts inside wherever SetupEnvironment is
set defaultFolder=%~dp0
set seleniumFolder=C:\AutomationPython\selenium_drivers

echo Creating required directories
::Directory will contain shared files with jenkins (tests archive, installer, junit tests result)
if not exist "C:\AutomationPython\shared" mkdir C:\AutomationPython\shared

::Directory will contain Selenium Drivers
if not exist "%seleniumFolder%" mkdir %seleniumFolder%

::Python
echo Installing %pythonExe%
msiexec /i "%defaultFolder%\%pythonExe%" /passive

echo Adding Python and Selenium to PATH
set PATH=%PATH%;%seleniumFolder%

::Drivers
echo Moving geckodriver 0.11.1
echo F|xcopy "%defaultFolder%\geckodriver.exe" "%seleniumFolder%\geckodriver.exe"

echo Moving Ie Driver 2.53.1
echo F|xcopy "%defaultFolder%\IEDriverServer.exe" "%seleniumFolder%\IEDriverServer.exe"

echo Moving Chrome Driver 2.25
echo F|xcopy "%defaultFolder%\chromedriver.exe" "%seleniumFolder%\chromedriver.exe"

echo Moving Edge Driver 3.14393
echo F|xcopy "%defaultFolder%\MicrosoftWebDriver.exe" "%seleniumFolder%\MicrosoftWebDriver.exe"

echo Setup complete. Reboot will be required to have access to Python in cmd.exe. Press any key to continue.
echo Reminder to update browsers Firefox >48, Chrome to latest version.

set /p restartResult="Restart(y/n)?"
if %restartResult% == "y" shutdown -r -f -t 1