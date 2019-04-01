md build
cd build
rd cauldron_#0_1 /s /q
rd exe.win32-3.6
cd ..
python setup_cx_freeze.py build
cd build
rename exe.win32-3.6 cauldron_#0_1
cd ..

pause