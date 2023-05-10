#!/bin/bash
pip install --target ./package requests
cd package
zip -r ../my-deployment-package.zip .
cd ..
zip my-deployment-package.zip lambda_function.py
