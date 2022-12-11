#!bin/bash

cd ExampleService/ 
docker build -t myimage .
docker run -d -p 80:20500 myimage
cd ../
cd ClientServer/
pip install -r requirements.txt
python src/ClientService.py
