import rclpy
from rclpy.node import Node

class PlannerNode(Node):
    def __init__(self):
        super().__init__('planner_node')
        self.get_logger().info('planner_node started (Ayela)')

def main():
    rclpy.init()
    rclpy.spin(PlannerNode())
    rclpy.shutdown()
