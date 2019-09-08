# Usage

1. Clone this repo to your catkin workspace. We assume the workspace is `~/catkin_ws/`.

```bash
$ cd ~/catkin_ws/src/
$ git clone https://github.com/YOURNAME/gazebo_models.git # YOURNAME is your user name, if you fork this repo. Or JayeFu for my repo
```

2. Compile.

```bash
$ cd ~/catkin_ws/
$ catkin build
```
3. Then launch the respective **launch** files.

```bash
$ roslaunch gazebo_models field_with_robot.launch
```
* Note: It will be a bit slow and the **gazebo** will show a black window if it is the first time gazebo loads the models. Just wait for about 3-5 minutes, it will be fine. Do not worry.  

Then you will see a football court with one ball and two goals appearing on your **gazebo**.  

# TODO
- [ ] Publish image topic to ROS system.
- [ ] Control the movement of the car from the robot.
