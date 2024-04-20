#!/bin/bash
cd ~
wget https://github.com/Mirantis/cri-dockerd/releases/download/v0.3.10/cri-dockerd_0.3.10.3-0.ubuntu-jammy_amd64.deb
dpkg -i cri-dockerd_0.3.10.3-0.ubuntu-jammy_amd64.deb