#!/bin/sh
docker build --platform linux/amd64 -t rickysims/django-sba ./web/.
docker push rickysims/django-sba

docker build --platform linux/amd64 -t rickysims/api-sba ./api/.
docker push rickysims/api-sba

az container create --resource-group RG_RIQUARTS --file deploy.yaml
