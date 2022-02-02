FROM blueirislabs/otbr

ADD otbr-watchdog.py otbr-watchdog.py
HEALTHCHECK --interval=2m --start-period=2m --timeout=5s CMD python3 otbr-watchdog.py
