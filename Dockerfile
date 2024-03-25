FROM blueirislabs/otbr:zephyr

ADD otbr_setup.sh /app/otbr_setup.sh
RUN chmod +x /app/otbr_setup.sh

ADD healthcheck.py /app/healthcheck.py
HEALTHCHECK --interval=30s --start-period=1m --timeout=10s CMD python3 /app/healthcheck.py
