#!/usr/bin/env bash

ln -s -F ../node_modules/.bin/gulp  bin/gulp
ln -s -F ../node_modules/.bin/bower bin/bower

ln -s -F ../scripts/build  bin/build
ln -s -F ../scripts/django bin/django
ln -s -F ../scripts/runsp  bin/runsp
ln -s -F ../scripts/sh     bin/sh
ln -s -F ../scripts/up     bin/up
ln -s -F ../scripts/stop   bin/stop
ln -s -F ../scripts/djsh   bin/djsh

chmod +x bin/build
chmod +x bin/django
chmod +x bin/runsp
chmod +x bin/sh
chmod +x bin/up
chmod +x bin/stop
chmod +x bin/djsh