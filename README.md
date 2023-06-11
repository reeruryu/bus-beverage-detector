# bus-beverage-detector
버스에 음료를 반입하는 불법 행위 검출기

## Description
https://github.com/reeruryu/bus-beverage-detector/assets/87798704/8148261f-55c7-4ef2-b8a9-bb7d60d4da93

## Build and run

```
$ source /opt/ros/foxy/setup.bash
$ colcon build --symlink-install --packages-select bus_beverage_detection
$ source install/local_setup.bash
```

terminal 1
```
$ ros2 run bus_beverage_detection video_publisher 

Video Absolute Path: {비디오_경로_입력하기}
```

terminal 2
```
$ ros2 run bus_beverage_detection detection_example
```


