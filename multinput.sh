#!/bin/bash

#Usage: run_commands_multiple_inputs.sh <command name> <args>"
#Get the options for command
array=${@:1:$#-1}
echo "Command:" $array


#Get last parameter, which is the file with the targets
for input in $@;do :;done
echo "Input:" $input


#Execute command on each target in sequence
while read -r line
do
       $array $line
done < $input