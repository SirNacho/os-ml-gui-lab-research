#!/bin/bash

#This script is created by Sir Nacho


PURPLE='\033[0;32m'
RED='\033[0;32m'
GREEN='\033[0;32m'

#Updating Section...

echo -e "${PURPLE}[INSTALLER] - Updating system...\n"

sudo apt update -y && sudo apt upgrade -y

if [$? -ne 0]; then
  echo -e "${RED}[INSTALLER] - Error, unable to update...\n"
else
  echo -e "${GREEN}[INSTALLER] - SUCCESSFULLY UPDATED THE PACKAGE...\n"
fi


echo -e "${PURPLE}[INSTALLER] - Installing required deb packages...\n"

sudo apt install opencv vtk hdf5 gcc -y

if [$? -ne 0]; then
  echo -e "${RED}[INSTALLER] - Error, unable to install...\n"
else
  echo -e "${GREEN}[INSTALLER] - SUCCESSFULLY INSTALLED THE PACKAGE...\n"
fi

echo -e "${PURPLE}[INSTALLER] - Exiting the program...\n"
