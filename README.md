# controller-ev3
This is a script to use EV3 robots and raspberrys on remo.tv!
## **Getting started:**
# Installing remo
You need to install Remo.TV controller on a raspberry (I used Pi 4 4GB)
Also, screen is used for the BT connection.
  ```
  sudo apt-get install screen
  ```
  ```
  https://github.com/remotv/controller
  ```
# Copying my code
  ```
  cd ~/remotv/hardware
  ```
  Paste there only .py files. Eg. ` EV3BT.py ` and ` ev3.py `
# Editing remo's config
Edit ~remotv/controller.conf with your favorite editor.(nano in my case)
  ```
  nano ~/remotv/controller.conf
  ```
# Bluetooth time!
Make sure it's enabled. And turned on.
```
screen -S bluetooth  sudo rfcomm watch hci0
```
Now it's searching for a connection, Start the EV3's code and if your PI's name is ` raspberrypi ` it should connect automatically.
