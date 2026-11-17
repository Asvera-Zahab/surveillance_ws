import rclpy
from rclpy.node import Node

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.get_logger().info('yolo_node started (Ayesha)')

def main():
    rclpy.init()
    rclpy.spin(YoloNode())
    rclpy.shutdown()
