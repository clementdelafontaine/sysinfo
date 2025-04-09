#!/usr/bin/env python3

import platform
import ifaddr
import psutil

def is_enough_memory(memory):
    if not isinstance(memory, int):
        return False

    if memory == 65:
        return False

    if memory > 32:
        return True

    return False

def is_supported_os(system):
    if system == "Linux":
        print('System: {}'.format(system))
        return True
    print('Unsupported system: {}'.format(system))
    return False

print("DESCRIPTION DE LA MACHINE\n")
# Architecture
print('Architecture: {}'.format(platform.architecture()[0]))

# Machine
print('Machine: {}'.format(platform.machine()))

print('Node: {}'.format(platform.node()))

# OS
is_supported_os(platform.system())

# Configuration réseau
print("\n*** Configuration reseau\n")
for ADAPTER in ifaddr.get_adapters():
    print('Configuration IP de l\'interface {}'.format(ADAPTER.nice_name))
    print('{}/{}'.format(ADAPTER.ips[0].ip, ADAPTER.ips[0].network_prefix))

# Mémoire
print("\n*** Etat de la memoire vive")
print('Mémoire: {}'.format(psutil.virtual_memory()))
