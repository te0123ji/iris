#!/bin/bash

chmod +x help_script.sh

# ----------------------------------
#       Defined variables
# ----------------------------------
#EDITOR=vim
#PASSWD=/etc/passwd
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
STD='\033[0;0;39m'

# ----------------------------------
# Step #2: User defined function
# ----------------------------------
pause(){
  read -p "Press [Enter] key to continue..." fackEnterKey
}


linux(){
	echo -e "\n${GREEN} ----- Linux support script called ----- ${STD}\n"

    echo -e "\n Checking type of Linux distribution \n"
    if [[ $(lsb_release -si) == 'Ubuntu' ]]; then
        echo -e "${GREEN}  --->  Ubuntu distribution found. ${STD}\n"

         echo -e "\n Checking Ubuntu version \n"
        if [[ $(lsb_release -sr) == '16.04' ]]; then
            echo -e "${GREEN}  --->  Ubuntu is the correct version --> 16.04. ${STD}\n"
        else
            echo -e "\n${RED}  --->  Error... Ubuntu $(lsb_release -sr) is NOT fully supported yet. ${STD}\n"
        fi
    else
        echo -e "\n${RED}  --->  Error... $(lsb_release -si) linux distribution is NOT supported. ${STD}\n"
    fi

    echo -e "\n Checking screen resolution \n"
    # Check screen resolution
    if [[ $(xdpyinfo | grep dimensions | sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/') > '1280x800' ]]; then
        echo -e "${GREEN}  --->  Screen resolution is good. It is greater than 1280x800. ${STD}\n"
    else
        echo -e "\n${RED}  --->  Error... Screen resolution must be greater than 1280x800 ${STD}\n"
    fi


    echo -e "\n Checking if Python installed \n"
    if command -v python2 &>/dev/null; then
        echo -e "${GREEN}  --->  Python is installed. ${STD}\n"

        echo -e "\n Checking Python version \n"
        if $(python --version); then
            echo -e "${GREEN}  --->  Python 2.7 is installed. ${STD}\n"
        else
            echo -e "\n${RED}  --->  Error... Python version 2.7 not found. Default version is not the correct one. ${STD}\n"
        fi
    else
        echo -e "\n${RED}  --->  Error... Python is not installed. ${STD}\n"
    fi


    echo -e "\n Checking if Pip installed \n"
    if command -v pip &>/dev/null; then
        echo -e "${GREEN}  --->  Pip is installed. ${STD}\n"
    else
        echo -e "\n${RED}  --->  Error... Pip not found. ${STD}\n"
    fi


    echo -e "\n Checking if Virtualenv installed \n"
    if command -v virtualenv &>/dev/null; then
        echo -e "${GREEN}  --->  Virtualenv is installed. ${STD}\n"
    else
        echo -e "\n${RED}  --->  Error... Virtualenv not found. ${STD}\n"
    fi


    echo -e "\n Checking if 7zip installed \n"
    if command -v p7zip &>/dev/null; then
        echo -e "${GREEN}  --->  7zip is installed. ${STD}\n"
    else
        echo -e "\n${RED}  --->  Error... 7zip not found. ${STD}\n"
    fi


    echo -e "\n Checking if Tesseract installed \n"
    if command -v tesseract &>/dev/null; then
        echo -e "${GREEN}  --->  Tesseract is installed. ${STD}\n"
    else
        echo -e "\n${RED}  --->  Error... Tesseract not found. ${STD}\n"
    fi

    echo -e "\n Checking Firefox install \n"
    if [[ $(which firefox) == '/usr/bin/firefox' ]]; then
        echo -e "${GREEN}  --->  Firefox is installed. ${STD}\n"
    else
        echo -e "\n${RED}  --->  Error... Firefox not installed. ${STD}\n"
    fi

    echo -e "\n Checking Firefox install \n"
    if [[ $(which git) == '/usr/bin/git' ]]; then
        echo -e "${GREEN}  --->  Git is installed. ${STD}\n"
    else
        echo -e "\n${RED}  --->  Error... Git not installed. ${STD}\n"
    fi

    pause
}


mac(){
	echo "Mac support script is called"
        pause
}

# function to display menus
show_menus() {
	clear
	echo "~~~~~~~~~~~~~~~~~~~~~"
	echo " M A I N - M E N U "
	echo "~~~~~~~~~~~~~~~~~~~~~"
	echo "1. Check Linux"
	echo "2. Check Mac OS"
	echo "2. Check Windows"
	echo "3. Exit"
}

# read input from the keyboard and take a action
# invoke the linux() when the user select 1 from the menu option.
# invoke the mac() when the user select 2 from the menu option.
# Exit when user the user select 3 form the menu option.
read_options(){
	local choice
	read -p "Please select the option [ 1 - 3] " choice
	case $choice in
		1) linux ;;
		2) mac ;;
		3) exit 0;;
		*) echo -e "\n ${RED}Error... Invalid selection.${STD} \n" && exit 0;;
	esac
}

# ----------------------------------------------
# Step #3: Trap CTRL+C, CTRL+Z and quit singles
# ----------------------------------------------
trap '' SIGINT SIGQUIT SIGTSTP

# -----------------------------------
# Step #4: Main logic - infinite loop
# ------------------------------------
while true
do
	show_menus
	read_options
done
