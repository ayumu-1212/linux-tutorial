# Use a Linux base image
FROM ubuntu:22.04

# Update the package lists
RUN apt update

# Install curl
# RUN apt install binutils build-essential golang sysstat python3-matplotlib python3-pil fonts-takao fio qemu-kvm virt-manager libvirt-clients virtinst jq docker.io containerd libvirt-daemon-system

# RUN adduser `id -un` libvirt
# RUN adduser `id -un` libvirt-qemu
# RUN adduser `id -un` kvm
