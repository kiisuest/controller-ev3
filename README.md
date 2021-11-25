# controller-ev3
This is a script to use EV3 robots and raspberrys on remo.tv!
## **Getting started:**
1. You need to install Remo.TV controller on a raspberry (I used Pi 4 4GB)
Also, screen is used for the BT connection.
  ```
  sudo apt-get install screen
  ```
  ```
  https://github.com/remotv/controller
  ```
2.
  ```
  cd ~/remotv/hardware
  ```
  Paste there only .py files. Eg. ` EV3BT.py ` and ` ev3.py `
3. Edit ~remotv/controller.conf with your favorite editor.(nano in my case)
  ```
  nano ~/remotv/controller.conf
  ```

