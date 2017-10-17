xcopy /Y repo.ini %~dp0\itch.io-downloader\
cd itch.io-downloader
python "itchDownload.py" %*
python "cleanOld.py"
cd ..
python grabGame.py
