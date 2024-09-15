#!/usr/bin/bash

cd /mnt/h/MySVN/Projekty/OSM/git/las-osmapa-garmin

mv logs/OSMapaPL.log logs/OSMapaPL.log_OLD
python3 -u ProduceDistributionsPL.py > logs/OSMapaPL.log 2>&1

mv logs/OSMapaPLext.log logs/OSMapaPLext.log_OLD
python3 -u ProduceDistributionsPLext.py > logs/OSMapaPLext.log 2>&1

mv logs/LocalUpdateWWW.log logs/LocalUpdateWWW.log_OLD
python3 -u LocalUpdateWebPage.py > logs/LocalUpdateWWW.log 2>&1 
