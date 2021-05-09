#!/usr/bin/sh

GIT_PATH="../../.git"
[[ -e $GIT_PATH ]] && cp hooks/* $GIT_PATH/hooks