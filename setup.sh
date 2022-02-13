pkg install figlet
pkg install lolcat

figlet -f big WAIT | lolcat
echo "All package installing"

pip2 install marshal
pip2 install zlib
pip2 install base64
pip2 install random
pkg install figlet
pkg install lolcat

mv nibase64 $PREFIX/bin
cd
cd $PREFIX/bin
chmod 777 nibase64
echo " All done.For Run This Tool Just Type nibase64"
