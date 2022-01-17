#!/usr/bin/env python3
import os
import sys

def check_reboot():
    '''Returns True if the computer has a pending reboot.'''
    # Check if the path "/run/reboot-required" exists
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1) # The system is rebooting, EXIT_FAILUIRE
    if disk_full():
        print("Disk full.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)	# The system is NOT rebooting, EXIT_FAILUIRE

main()
