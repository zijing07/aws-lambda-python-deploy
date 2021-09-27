#!/bin/bash

pipenv install
cd `pipenv --venv`/lib/python3.8/site-packages/
zip -r /var/task/my-deployment-package.zip .
cd -
zip -r -g my-deployment-package.zip src/
aws lambda update-function-code --function-name amplifypylambda7935db62-dev --zip-file fileb://my-deployment-package.zip