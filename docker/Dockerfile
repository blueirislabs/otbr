FROM blueirislabs/otbr

ADD otbr-watchdog.py otbr-watchdog.py
HEALTHCHECK --interval=60s --start-period=1m --timeout=10s CMD python3 otbr-watchdog.py
