#!/bin/bash
#find log/ -type f -exec chmod a-w '{}' \;
#scp -r pi@raspi:LWZ303-RS232/log .
#find log/ -type f -exec chmod +w '{}' \;
rsync -a pi@raspi:LWZ303-RS232/log .
