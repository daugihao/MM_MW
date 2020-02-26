https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows

applepi.local (PUTTY)
pi
b3edef126p

pearpi.local (PUTTY)
pi
b3edef126p

cd ..
cd .. (repeated to get to root)

sudo apt install vim
sudo apt-get install git
sudo apt-get install python-pip
sudo apt-get install python-cwiid

mkdir repos
git clone https://github.com/daugihao/MM_MW.git
mv MM_MW magic-wand

sudo vim /etc/rc.local
Add in: sudo python home/pi/repos/magic-wand/wiimote-wand/main.py &

sudo apt-get install python-pygame
# sudo apt install libsdl1.2-dev
# sudo pip install -r requirements.txt
