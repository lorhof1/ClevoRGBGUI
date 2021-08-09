#!/bin/bash
if [ "$(stat -c '%U' /sys/devices/platform/clevo_xsm_wmi/kb_color)" != "$USER" ]; then
    sudo chown $USER /sys/devices/platform/clevo_xsm_wmi/kb_color
fi
python3 main.py