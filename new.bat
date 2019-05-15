@echo off
set current=%cd%
pushd ..
set parent=%cd%
popd

echo current %current%
echo parent %parent%
start C:\Users\hmesquita\OneDrive\Programas\AtomPortable\AtomPortable.exe %current% 
set "PATH=C:\Users\hmesquita\OneDrive\Programas\MinGW\bin;%PATH%"
set "PATH=C:\Hugo\GitPortable\App\Git\bin;%PATH%"
set "PATH=C:\Users\hmesquita\OneDrive\Programas\NodeJsPortable;%PATH%"
set "PATH=C:\Users\hmesquita\OneDrive\Programas\ruby-2.4.2\bin;%PATH%"
set "PATH=C:\Users\hmesquita\OneDrive\Programas\gettext-runtime-0.17-1\bin;%PATH%"
set "PATH=C:\Users\hmesquita\OneDrive\Programas\gettext-tools-0.17\bin;%PATH%"

cmd.exe /k