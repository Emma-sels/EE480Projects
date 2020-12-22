#!/bin/sh
cd /sys/class/leds/led1
sudo sh -c "echo heartbeat > trigger" 
cd /sys/class/leds/led0
sudo sh -c "echo timer > trigger"
sudo sh -c "echo 500 > delay_on"
sudo sh -c "echo 500 > delay_off"
