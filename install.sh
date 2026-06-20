#!/bin/bash

# ABHINAV - All-in-One Premium Tool Collection Installer
# Automated setup for Termux and Linux environments

echo "╔════════════════════════════════════════════════════════════╗"
echo "║                  ABHINAV PREMIUM EDITION                   ║"
echo "║            All-in-One Tool Collection Installer             ║"
echo "╚════════════════════════════════════════════════════════════╝"

echo ""
echo "[*] Detecting system environment..."

if [[ -d "$PREFIX" ]]; then
    echo "[✓] Termux environment detected"
    INSTALL_CMD="apt install"
else
    echo "[✓] Linux environment detected"
    INSTALL_CMD="apt-get install"
fi

echo ""
echo "[*] Updating package manager..."
$INSTALL_CMD update -y

echo ""
echo "[*] Installing Python and dependencies..."
$INSTALL_CMD install python3 python3-pip git -y

echo ""
echo "[*] Installing Python packages..."
pip install -r requirements.txt

echo ""
echo "[✓] Installation completed successfully!"
echo ""
echo "[*] To start ABHINAV, run:"
echo "    python3 main.py"
echo ""
echo "[*] Default password: abhi"
echo "[*] Features: 20 Premium Tools"
echo ""
echo "[✓] Setup complete! Enjoy ABHINAV Premium Edition"
