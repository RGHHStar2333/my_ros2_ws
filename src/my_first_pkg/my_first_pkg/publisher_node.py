import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self):
        # 初始化节点，节点名为 'simple_publisher'
        super().__init__('simple_publisher')

        # 创建发布者：消息类型 String，话题名 'chatter'，队列大小 10
        self.publisher_ = self.create_publisher(String, 'chatter', 10)

        # 创建定时器，每 1 秒触发一次回调函数
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS2, 第 {self.count} 条消息'
        self.publisher_.publish(msg)
        self.get_logger().info(f'发布消息: "{msg.data}"')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)          # 初始化 ROS2 通信
    node = PublisherNode()         # 创建节点对象
    rclpy.spin(node)                # 让节点持续运行，等待回调触发
    node.destroy_node()             # 节点销毁
    rclpy.shutdown()                # 关闭 ROS2 通信


if __name__ == '__main__':
    main()