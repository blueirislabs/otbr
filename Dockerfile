FROM blueirislabs/otbr:zephyr

ADD otbr_setup.sh /app/otbr_setup.sh
RUN chmod +x /app/otbr_setup.sh 

ADD otbr-watchdog.py /app/otbr-watchdog.py
HEALTHCHECK --interval=30s --start-period=1m --timeout=10s CMD python3 /app/otbr-watchdog.py
