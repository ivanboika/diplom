#!/bin/bash

# Создание виртуальной среды
python3 -m venv myenv

# Активация виртуальной среды для Windows
if [ -f myenv/Scripts/activate ]; then
    source myenv/Scripts/activate
fi

# Активация виртуальной среды для Unix или MacOS
if [ -f myenv/bin/activate ]; then
    source myenv/bin/activate
fi