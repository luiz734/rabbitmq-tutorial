#! /usr/bin/env bash

CLIENT_NAME=$(gum input --placeholder "client name")
TIME_OF_DAY=$(gum choose "MORNING" "AFTERNOON" "EVENING")
SUBJECT=$(gum choose "MATH" "GRAMMAR" "PROGRAMMING")
LEVEL=$(gum choose "BASIC" "INTERMEDIATE" "ADVANCED")

python publisher/main.py $CLIENT_NAME $TIME_OF_DAY $SUBJECT $LEVEL
