:RESTART
tasklist /FI "username eq administrator" | find /C "py.exe" > temp.txt
set /p num= < temp.txt
del /F temp.txt
echo %num%
if "%num%" == "0"   start /D "E:\Yandere-crawler-master\Yandere\Yandere0.3" index.py 
ping -n 10 -w 2 0.0.0.1 > temp.txt
del /F temp.txt
goto RESTART 
