#!/bin/bash

# All-in-One Tool Installation Script for Termux

echo "[+] Installing All-in-One Tool Collection..."
echo ""

# Update packages
echo "[*] Updating package manager..."
apt-get update -y
apt-get upgrade -y

# Install Python3 and pip
echo "[*] Installing Python3 and pip..."
apt-get install -y python3 python3-pip

# Install git
echo "[*] Installing git..."
apt-get install -y git

# Install additional dependencies
echo "[*] Installing system dependencies..."
apt-get install -y libffi-dev libssl-dev python3-dev

# Install Python requirements
echo "[*] Installing Python requirements..."
pip install -r requirements.txt

echo ""
echo "[+] Installation complete!"
echo "[*] To run the tool, execute: python3 main.py"
echo ""
