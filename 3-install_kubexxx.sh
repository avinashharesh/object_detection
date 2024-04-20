#!/bin/bash

apt update && apt install -y apt-transport-https ca-certificates curl

#Download the Google public signing key:
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
#turn off swap
swapoff -a
#Add K8s repository:
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | tee /etc/apt/sources.list.d/kubernetes.list
apt update && sudo apt-get install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl
kubeadm version

echo "If you can see the output of version numbers, Kubernetes utilities have been installed successfully."