FROM blueirislabs/otbr

ADD otbr-watchdog.py otbr-watchdog.py
HEALTHCHECK --interval=30s --start-period=1m --timeout=10s CMD python3 otbr-watchdog.py
