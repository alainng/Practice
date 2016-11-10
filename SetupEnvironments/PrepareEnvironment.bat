@echo off
SETLOCAL ENABLEEXTENSIONS

:bitnessselect
set /p bitness="Are you on on 32 or 64? (Type the number in or q to quit)"
if %bitness% == 32 goto 32bitvars
if %bitness% == 64 set 64bitvars
if %bitness% == q GOTO :EOF
if [%bitness%] == [] goto bitnessselect

:32bitvars
set pythonExe=python-2.7.12.msi
goto :payload

:64bitvars
set pythonExe=python-2.7.12.amd64.msi
goto :payload

:payload
::usage %defaultFolder%
set defaultFolder=%UserProfile%\Desktop\SetupEnvironments
set seleniumFolder=C:\tests\selenium_drivers

echo Creating required directories
::Directory will contain shared files with jenkins (tests archive, installer, junit tests result)
if not exist "C:\tests\shared" mkdir C:\tests\shared

::Directory will contain Selenium Drivers
if not exist "%seleniumFolder%" mkdir %seleniumFolder%

::Python
echo Installing Python 2.7.12
msiexec /i "%defaultFolder%\%pythonExe%" /qn

echo Adding Python and Selenium to PATH
set PATH=%PATH%;C:\Python27;%seleniumFolder%
C:\Python27\python.exe C:\Python27\Tools\Scripts\win_add2path.py

::Drivers
echo Transferring geckodriver
echo F|xcopy "%defaultFolder%\geckodriver.exe" "%seleniumFolder%\geckodriver.exe"

echo Transferring Ie Driver
echo F|xcopy "%defaultFolder%\IEDriverServer.exe" "%seleniumFolder%\IEDriverServer.exe"

echo Downloading Chrome Driver 2.25
echo F|xcopy "%defaultFolder%\chromedriver.exe" "%seleniumFolder%\chromedriver.exe"

echo Updating pip
python -m pip install --upgrade pip

echo Downloading packages
pip install selenium
pip install behave
pip install pyscreenshot

echo "Installing Notepad++"
%defaultFolder%\npp.7.2.Installer.exe /S

echo Setup complete. Reboot will be required to have access to Python in cmd.exe. Press any key to continue.
echo Reminder to update browsers Firefox >48, Chrome to latest version.
pause

set /p restartResult="Restart(y/n)?"
if %restartResult% == "yes" shutdown -r -t 5
exit