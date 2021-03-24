#!/usr/bin/sh

GIT_PATH="../../.git"
[[ -e $GIT_PATH ]] && mv hooks/* $GIT_PATH/hooks