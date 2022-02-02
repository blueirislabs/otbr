FROM blueirislabs/otbr

RUN apt install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.7 -y
ADD otbr-watchdog.py otbr-watchdog.py
HEALTHCHECK --interval=2m --timeout=5s CMD python3 otbr-watchdog.py
