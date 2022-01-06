#!/usr/bin/env bash
echo "############################################################################################";
echo "
	     *****                      **              * ***          *******    
	  ******                     *****            *  ****        *       ***  
	 **   *  *    **            *  ***           *  *  ***      *         **  
	*    *  *   **** *             ***          *  **   ***     **        *   
	    *  *     ****             *  **        *  ***    ***     ***          
	   ** **    * **              *  **       **   **     **    ** ***        
	   ** **   *                 *    **      **   **     **     *** ***      
	   ** *****                  *    **      **   **     **       *** ***    
	   ** ** ***                *      **     **   **     **         *** ***  
	   ** **   ***              *********     **   **     **           ** *** 
	   *  **    ***            *        **     **  **     **            ** ** 
	      *       ***          *        **      ** *      *              * *  
	  ****         ***        *****      **      ***     *     ***        *   
	 *  *****        ***  *  *   ****    ** *     *******     *  *********    
	*    ***           ***  *     **      **        ***      *     *****      
	*                       *                                *                
	 **                      **                               **"
echo "                                                                                 by:  ";
echo "                                                                              73RM1N41";
echo "############################################################################################";
echo "                   Kaos Is Still In Development... Please Be Patient.    (:                ";
sleep 1;
printf "Starting Setup in 5...\r";
sleep 1;
printf "\033[2KStarting Setup in 4...\r";
sleep 1;
printf "\033[2KStarting Setup in 3...\r";
sleep 1;
printf "\033[2KStarting Setup in 2...\r";
sleep 1;
printf "\033[2KStarting Setup in 1...\r";
sleep 2;

printf "\033[2KSetting Up Kaos...\n";
sleep 2;

echo "Starting cleanup";

echo "Removing Old .pyc Files...";
rm -fv  => /media/$USER/*/Development/*.pyc;
rm -rfv  => /media/$USER/*/Development/__pycache__;
echo "Cleanup Complete!";

echo "Installing Neccessary Programs And Modules...";

#sudo apt-get update;
#yes | sudo apt-get install python3-pip secure-delete tix arp-scan python3-termcolor python3-tk python3-bs4 python3-stem haveged hostapd git util-linux procps iproute2 iw dnsmasq iptables python3-pil.imagetk;
#git clone https://github.com/oblique/create_ap;

dpkg -i  => /media/$USER/*/Depends/deb/*;
cd  => /media/$USER/*/Depends/create_ap;
make install;
#cd .. && rm -rf create_ap;
cd ..;
echo "Install Complete! :)";

# Firefox Will Not Run As Root In A Non-Root Account

############################################
### THIS IS PROBABLY A HORRIBLE SOLUTION ###
############################################

echo "Kaos Setup Is Complete!";
sleep 2;
echo "";
echo "";
echo "[!]   Please Enter The Following In Your Terminal From Non-Root Account To Complete Setup...";
echo "############################################################################################";
echo "sudo -i";
echo "test -f .Xauthority && mv .Xauthority .Xauthority.bak";
echo "cp -a /home/kali/.Xauthority .Xauthority";
echo "chown root: .Xauthority";
echo "XAUTHORITY=/root/.Xauthority";
echo "cd /media/kali/*/Development";
echo "############################################################################################";
echo "";
echo "Once Complete, Kaos Is Ready!";
echo "";
echo "############################################################################################";
echo "";
echo "Start Kaos With 'sudo ./kaotic.py'";
echo "";
exit 0;
