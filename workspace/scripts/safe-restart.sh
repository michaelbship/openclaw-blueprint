#!/bin/bash
# Safe Gateway Restart
# Run this detached: nohup scripts/safe-restart.sh &
#
# Waits 3 seconds before restarting, giving the agent time to
# send its final message before the connection drops.

sleep 3
systemctl --user restart openclaw-gateway
