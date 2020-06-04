# turtlebot3_practice

### パッケージ概要
turtlebot3のパッケージを使用して色々実装していき、学んでいくためのパッケージ。

### パッケージ内容
こちらはワークスペースになっています。

src内のパッケージは私のリポジトリからクローンもしくは公式からクローンしてくる必要があります。

### 導入方法

```
sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy ros-melodic-teleop-twist-keyboard \ 
ros-melodic-laser-proc ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan \ 
ros-melodic-rosserial-arduino ros-melodic-rosserial-python ros-melodic-rosserial-server \ 
ros-melodic-rosserial-client ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server \ 
ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro ros-melodic-compressed-image-transport \ 
ros-melodic-rqt-image-view ros-melodic-navigation

```


```
~$ git clone https://github.com/uhobeike/turtlebot3_practice.git
~$ cd ~/turtlebot3_practice/src
~/turtlebot3_practice/src$ git clone https://github.com/uhobeike/turtlebot3.git && \
git clone https://github.com/uhobeike/turtlebot3_msgs.git && \
git clone https://github.com/uhobeike/turtlebot3_simulations.git && \
git clone https://github.com/uhobeike/turtlebot3_gazebo_plugin.git
~/turtlebot3_practice/src$ cd ..　&& catkin_make
```

cartgrapherのインストール下記のリンクより

https://beike.hatenablog.jp/entry/2020/04/30/224026

turtlebot3 e-manial

http://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#ros-1-simulation

