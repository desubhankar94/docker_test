#!/usr/bin/env bash

sudo apt-get update
#sudo apt-get install git
#sudo git clone https://github.com/desubhankar94/gcp_test.git
sudo curl -sSL https://get.docker.com/ | sh
sudo docker build . -t py_app
sudo docker run --name=py_app --rm -d -p 80:80 py_app
#sudo docker exec -it py_app bash
#sudo docker container stop py_app