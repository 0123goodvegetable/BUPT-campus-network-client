#!/bin/bash 
git_not_installed(){
    git --version 2>&1 >/dev/null 
    GIT_IS_AVAILABLE=$?
    return $GIT_IS_AVAILABLE 
}

if [ "$OS" = "Ubuntu" ]; then
    apt-get install git -y
fi

if [ "$OS" = "Debian" ]; then 
    apt-get install git -y 
fi

if [ "$OS" = "CentOS" ]; then 
    yum install git 
fi

if [ "$OS" = "Manjaro" ]; then 
    pacman -S git 
fi

confirm_os(){
    PLATFORM=$(uname)
    case $PLATFORM in 
        Darwin)
            OS=macOS ;;
        Linux)
            if [ -f /etc/centos-release ]; then 
                OS=CentOS
            elif [ -s /etc/redhat-release ]; then 
                OS=RedHat
            elif [ -f /etc/debian_version ]; then 
                OS=Debian
            elif [ -f /etc/ubuntu-release ]; then 
                OS=Ubuntu
            elif [ -f /etc/manjaro-release ]; then 
                OS=Manjaro
            #elif [ -r /etc/os-release ]; then 
            #    grep 'NAME="Ubuntu"' /etc/os-release > /dev/null 2>&1
            #    if [ $? == 0 ]; then 
            #        OS=Ubuntu
            #    fi 
            else 
                OS="Unknown Linux"
            fi ;;
        *)
            OS="Unknown UNIX/Linux" ;;
    esac
    return $OS
}

