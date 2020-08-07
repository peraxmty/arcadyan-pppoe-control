# arcadyan-pppoe-control
Disconnect &amp; connect the pppoe session in the Arcadyan VRV9506JAC23 modem as installed by TELMEX.
It does it by editing the pppoe username and adding an 'x' at the end.

I use it to turn off internet access in my home at night, as the built-in feature in the modem isn't reliable.

I run it in a Raspberry PI 3b running Raspbian 10.4 & Python 2.7.16

You need to install chromium-chromedriver and selenium:
  
  wget http://launchpadlibrarian.net/452362975/chromium-chromedriver_78.0.3904.108-0ubuntu0.16.04.1_armhf.deb
  dpkg -i chromium-chromedriver_78.0.3904.108-0ubuntu0.16.04.1_armhf.deb
  pip install selenium
