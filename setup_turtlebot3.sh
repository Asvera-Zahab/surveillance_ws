#!/bin/bash
cd "$(dirname "$0")/src"
for r in DynamixelSDK turtlebot3_msgs turtlebot3 turtlebot3_simulations; do
  git clone --depth 1 -b jazzy https://github.com/ROBOTIS-GIT/$r.git
done
