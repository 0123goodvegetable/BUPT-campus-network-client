#! /bin/bash
#----------------------------
#|-----create by james------|
#|BUPT-campus-network-client|
#|------shell edition-------|
#----------------------------
login(){
    dialog --title "Login Box" --inputbox "Please enter your account: " 10 20 2> ~/Desktop/tmp.txt
    Name=$(cat ~/Desktop/tmp.txt)
    dialog --insecure --title "Login Box" --passwordbox "Please enter your password: " 10 20 2> ~/Desktop/tmp.txt
    PassWord=$(cat ~/Desktop/tmp.txt)
}

connecting(){
    ping bupt.edu.cn;


processing(){
    {
    for ((i = 0 ; i <= 100 ; i+=20)); do
        sleep 0.5
        echo $i
    done
    } | dialog --gauge "Please wait while accessing to the server" 6 60 0
}

menu(){
    dialog --menu "\n\n\n\n-------Choose a section-------" 20 40 \
        3 \
        1 "Classes" \
        2 "Calendar" \
        3 "Logout" \
        2> ~/Desktop/tmp.txt
    Choice=$(cat ~/Desktop/tmp.txt)
    #don't do this if ["$Choice" == "1"]; then
    if [ "$Choice" == "1" ]; then
     ./showin
     return 
    fi
    if [ "$Choice" == "2" ]; then 
     calendar 
     return 
    fi
    if [ "$Choice" == "3" ]; then 
        boolcess="0";
    fi
}

calendar(){
    year = $(date + %Y)
    month = $(date + %m)
    day = $(date + %d)
    dialog --title "Calendar" --calendar "Date" 5 50 $(day) $(month) $(year) 
}
testshow(){
    dialog --menu "this is a test" 10 20 2 1 "$Choice" 2 "$PassWord"
}
boolcess="1"
login 
processing
while [[ "$boolcess" == "1" ]]
do
menu
if [ $? = 1 ]; then
    boolcess="0"
fi
done
exit 0
