#!/bin/bash

PYBABEL=pybabel-2

make_error_message() {
    PY_FILE=/root/git/3A/backend/app/core/error.py
    cp -a $PY_FILE .

    mkdir -p translations/ko/LC_MESSAGES translations/en/LC_MESSAGES

    python3 error_message.py
    $PYBABEL extract -F babel.cfg -k lazy_gettext -o messages.pot . || exit 1
    $PYBABEL update -i messages.pot -d translations || exit 1
    $PYBABEL compile -d translations || exit 1

    rm -fr error.py
}

make_error_message