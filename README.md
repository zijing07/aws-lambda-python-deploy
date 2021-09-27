# Amplify PyLambda Deploy Demo

This packge showcases how to deploy a Amplify-created PyLambda from your MacOS.

## Manual

If you are interested to know more, please check out [this article](https://zijing.medium.com/deploy-aws-amplify-python-lambda-from-macos-with-docker-68212e889a38).

## Issue

If we directly build and deploy a python lambda from MacOS, we will see errors like:

```shell
{
  "errorMessage": "Unable to import module 'index': No module named 'regex._regex'",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}
```

This is because pipenv is downloading the MacOS binaries, which are not compatible with AWS Lambda runtime: Linux.

## Fix

By using Docker, we could conveniently create a Linux build and deploy environment. Then developers can quickly deploy and test their code before pushing them to CI/CD.

## How To Use

Please go to the [PyLambda folder](./amplify/backend/function/amplifypylambda7935db62), and checkout the following two files:

- Dockerfile
- dockerCmd.sh

Then run the following command at the [PyLambda folder](./amplify/backend/function/amplifypylambda7935db62):

```shell
docker build -t tmp-awslambda . && docker run --rm tmp-awslambda
```

