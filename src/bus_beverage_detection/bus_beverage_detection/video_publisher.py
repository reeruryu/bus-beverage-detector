import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile # QoS 설정을 위해
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

class ImagePublisher(Node): # Node 클래스를 상속
    def __init__(self):
        super().__init__('image_publisher') # 부모 클래스(Node)의 생성자를 호출하고 이름을 helloworld_publisher로 지정
        qos_profile = QoSProfile(depth=10) # 통신상태가 원활하지 못할 경우 퍼블리시 할 데이터를 버퍼에 10개까지 저장하라는 설정
        self.publisher = self.create_publisher(# create_publisher함수를 이용해 helloworld_publisher 설정
            Image, # 토픽 메시지 타입: Imqge,
            'image', #  토픽 이름: image
            qos_profile)#, QoS설정
        self.timer = self.create_timer(0.1, self.time_callback) # 콜백 함수를 실행. 0.1초마다 time_callback 함수 실행
        self.video_path = input("Video Absolute Path:")
        self.cap = cv2.VideoCapture(self.video_path)

    def time_callback(self) :
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, dsize=(800,450))
        cv2.imwrite('test.jpg', frame)
        if ret == True :
            fra = bridge.cv2_to_imgmsg(frame,"bgr8")
            self.publisher.publish(fra)
            # cv2.imshow('droidcamframe', frame)
            # cv2.waitKey(2)
        self.get_logger().info('Publishing Droidcam Image')
   


def main(args=None):
    rclpy.init(args=args) # 초기화
    node = ImagePublisher() # ImagePublisher를 node라는 이름으로 생성
    try:
        rclpy.spin(node) # rclpy에게 이 Node를 반복해서 실행 (=spin) 하라고 전달
    except KeyboardInterrupt: # `Ctrl + c`가 동작했을 때
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()  # 노드 소멸
        rclpy.shutdown() # rclpy.shutdown 함수로 노드 종료


if __name__ == '__main__':
    main()

