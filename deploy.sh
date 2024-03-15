#!/bin/sh
docker build --platform linux/amd64 -t fabadi/django-sba ./web/.
docker push fabadi/django-sba

docker build --platform linux/amd64 -t fabadi/api-sba ./api/.
docker push fabadi/api-sba

az container create --resource-group RG_ABADIF --file deploy.yaml
