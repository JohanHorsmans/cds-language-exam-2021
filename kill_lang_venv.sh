#!/usr/bin/env bash

VENVNAME=lang_venv
jupyter kernelspec uninstall $VENVNAME
rm -r $VENVNAME