#!/bin/bash

#This script is created by Sir Nacho


PURPLE='\033[0;32m'
RED='\033[0;32m'
GREEN='\033[0;32m'

#Updating Section
echo -e "${PURPLE}[INSTALLER] - updating arch packages..."

sudo pacman -Syyu

if [$? -ne 0]; then
  echo -e "${RED}[INSTALLER] - Error, unable to install..."
else
  echo -e "${GREEN}[INSTALLER] - SUCCESSFULLY UPDATED ARCH PACKAGE..."
fi


#Installing packages

echo -e "${PURPLE}[INSTALLER] - Installing required arch packages..."


sudo pacman -S opencv vtk hdf5 gcc

if [$? -ne 0]; then
  echo -e "${RED}[INSTALLER] - Error, unable to install..."
else
  echo -e "${GREEN}[INSTALLER] - SUCCESSFULLY INSTALLED THE PACKAGE..."
fi

echo -e "${PURPLE}[INSTALLER] - Exiting the program..."
