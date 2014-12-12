#!/bin/bash

# Set the volume to max
volume=${2-100}
echo $volume

amixer -c 0 sset PCM,0 $volume%
amixer -c 0 sset Master,0 $volume%

# Then moo.
aplay $1
