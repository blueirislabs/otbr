OTBR Docker image with Docker Compose
====================================

This setups up a border router using the otbr docker image and docker compose.

## Dependencies

To use this you need to [install](https://docs.docker.com/engine/install/) docker and docker compose

## Configure

You should set the values after the ot-ctl commands at the end of docker_entrypoint.sh
to configure your border router.

## Enable ipv6 filter kernel module
```shell
echo ip6table_filter | sudo tee -a /etc/modules
```

## Set up external otbr docker network
```shell
docker network create otbr-network --subnet 172.24.24.0/24
```

## Run with command

```shell
docker-compose up -d
```

