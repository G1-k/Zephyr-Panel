# Zephyr-Panel
A Linux application to control fan speed and keyboard backlight of ASUS Zephyrus AMD-Series Laptops

[//]: # (Image Reference)

[image1]: ./img/Panel_logo.png
[image2]: ./img/Main_panel.png

![alt_text][image1]

## Installation

1. Requirement :
* Kernel version > 5.6

2. RogAuraCore 

* In home folder 
`git clone https://github.com/wroberts/rogauracore.git`

* Install
```
git clone https://github.com/qquique/rogauracore
cd rogauracore 
git checkout initialize_keyboard
autoreconf -i 
./configure
make 
```

3. Install Zephry-panel

* Download zephyr-panel.deb from this repository 

* Install package using dpkg
`sudo dpkg -i /path/to/zephyr-panel.deb`

4. Launch it 

![alt_text][image2]


## Tested Platforms

* Asus Zephyrus GA502 | Ubuntu 18.04 
