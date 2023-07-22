# bus-beverage-detector
버스에 음료를 반입하는 불법 행위 검출기

## description
https://github.com/reeruryu/bus-beverage-detector/assets/87798704/8148261f-55c7-4ef2-b8a9-bb7d60d4da93

## build and run
```
$ source /opt/ros/foxy/setup.bash
$ colcon build --symlink-install --packages-select bus_beverage_detection
$ source install/local_setup.bash
```

terminal 1
```
REM 1. 비디오 파일을 읽어서 ROS2 메시지로 변환하는 방법
$ ros2 run bus_beverage_detection video_publisher 

Video Absolute Path: {비디오_경로_입력하기}
```
```
REM 2. 카메라에서 영상을 획득하여 ROS2 이미지 메시지로 변환하는 방법
$ ros2 run image_tools cam2image
```

terminal 2
```
$ ros2 run bus_beverage_detection detection_example
```

## created by
<table>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/reeruryu" width=150 />
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/dmdwn99" width=150 />
    </td>
  </tr>
  <tr>
    <td align=center>
      <a href="https://github.com/reeruryu">@reeruryu</a>
    </td>
     <td align=center>
      <a href="https://github.com/dmdwn99">@dmdwn99</a>
    </td>
  </tr>
</table>
