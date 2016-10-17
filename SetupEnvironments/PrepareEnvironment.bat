@echo off
::Don't need admin cmd.exe

echo Setting up test environment

echo Creating required directories
::Directory will contain behave log file
if not exist "C:\temp" mkdir C:\temp

::Directory will contain installer exe
if not exist "C:\tests\installer" mkdir C:\tests\installer

::Directory will contain extracted tests archive
if not exist "C:\tests\src\release" mkdir C:\tests\src\release

::Directory will contain shared files with jenkins (tests archive, installer, junit tests result)
if not exist "C:\tests\shared" mkdir C:\tests\shared

::Directory will contain Selenium Drivers
if not exist "C:\selenium_drivers" mkdir C:\selenium_drivers

::Python
echo Downloading Python 2.7.11
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi', 'C:\temp\python.msi')"
echo Installing Python 2.7.11
msiexec /i "C:\temp\python.msi" /qn

echo Adding Python and Selenium to PATH
set PATH=%PATH%;C:\Python27;C:\selenium_drivers
C:\Python27\python.exe C:\Python27\Tools\Scripts\win_add2path.py

::Required to use easy_install and pip (I could have used absolute path for easy_install and pip)
chdir C:\Python27\Scripts

::PIL
echo Downloading PIL-1.1.7.win32-py2.7
powershell -Command "(New-Object Net.WebClient).DownloadFile('http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe', 'C:\temp\PIL.exe')"
easy_install C:\temp\PIL.exe

::pywin32
::find a way to get around the 5s install wait shit
echo Downloading pywin32-220.win32-py2.7.exe
easy_install Z:\Alain\Automation\HostedFiles\pywin32-220.win32-py2.7.exe

::Drivers
echo Downloading geckodriver
::TODO get 64bit on 64, 32bit on 32
powershell -Command "(New-Object Net.WebClient).DownloadFile('http://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-win64.zip', 'C:\temp\geckodriver.zip')"

echo Downloading Ie Driver
powershell -Command "(New-Object Net.WebClient).DownloadFile('http://selenium-release.storage.googleapis.com/2.53/IEDriverServer_Win32_2.53.0.zip', 'C:\temp\IEDriverServer.zip')"
echo Downloading Chrome Driver
::Determining Windows Version
for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j
if "%version%" == "10.0" powershell -Command "(New-Object Net.WebClient).DownloadFile('http://chromedriver.storage.googleapis.com/2.24/chromedriver_win32.zip', 'C:\temp\chromedriver.zip')"
if "%version%" == "6.3" powershell -Command "(New-Object Net.WebClient).DownloadFile('http://chromedriver.storage.googleapis.com/2.24/chromedriver_win32.zip', 'C:\temp\chromedriver.zip')"
if "%version%" == "6.2" powershell -Command "(New-Object Net.WebClient).DownloadFile('http://chromedriver.storage.googleapis.com/2.24/chromedriver_win32.zip', 'C:\temp\chromedriver.zip')"
if "%version%" == "6.1" powershell -Command "(New-Object Net.WebClient).DownloadFile('http://chromedriver.storage.googleapis.com/2.24/chromedriver_win32.zip', 'C:\temp\chromedriver.zip')"
if "%version%" == "6.0" powershell -Command "(New-Object Net.WebClient).DownloadFile('http://chromedriver.storage.googleapis.com/2.22/chromedriver_win32.zip', 'C:\temp\chromedriver.zip')"
if "%version%" == "5.2" powershell -Command "(New-Object Net.WebClient).DownloadFile('http://chromedriver.storage.googleapis.com/2.21/chromedriver_win32.zip', 'C:\temp\chromedriver.zip')"
if "%version%" == "5.1" powershell -Command "(New-Object Net.WebClient).DownloadFile('http://chromedriver.storage.googleapis.com/2.21/chromedriver_win32.zip', 'C:\temp\chromedriver.zip')"

echo Unzipping all drivers into C:\selenium_drivers
Call :UnZipFile "C:\selenium_drivers\" "C:\temp\chromedriver.zip"
Call :UnZipFile "C:\selenium_drivers\" "C:\temp\IEDriverServer.zip"
Call :UnZipFile "C:\selenium_drivers\" "C:\temp\geckodriver.zip"

echo Updating pip
python -m pip install --upgrade pip

echo Downloading packages
pip install pyscreenshot
pip install nose
pip install behave
pip install psutil
pip install flask
pip install wget
pip install selenium

echo Deleting temp files
chdir C:\temp\
del *.* /F /Q

echo Setup complete. Reboot will be required to have access to Python in cmd.exe. Press any key to continue.
echo Reminder to update browsers Firefox >48, Chrome to latest version.
pause
exit

::unzip only works on win10
:UnZipFile <ExtractTo> <newzipfile>
set vbs="%temp%\_.vbs"
if exist %vbs% del /f /q %vbs%
>%vbs%  echo Set fso = CreateObject("Scripting.FileSystemObject")
>>%vbs% echo If NOT fso.FolderExists(%1) Then
>>%vbs% echo fso.CreateFolder(%1)
>>%vbs% echo End If
>>%vbs% echo set objShell = CreateObject("Shell.Application")
>>%vbs% echo set FilesInZip=objShell.NameSpace(%2).items
>>%vbs% echo objShell.NameSpace(%1).CopyHere(FilesInZip)