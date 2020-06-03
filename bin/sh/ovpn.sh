#!/bin/bash
sudo openvpn --dev tun --auth-nocache --script-security 2 .riseup.ovpn
