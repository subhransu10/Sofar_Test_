from setuptools import setup

package_name = 'multirobots_gazebo'

data_files = []
data_files.append(('share/' + package_name + '/launch', ['launch/multirobot_spawn.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/spawn_bot_box_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/rviz_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/bot_simulation.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/localization_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/navigation_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/slam_launch.py']))


data_files.append(('share/' + package_name + '/resource', [
     'resource/nav2_default_view.rviz',
     'resource/nav2_multirobot_params_1.yaml',
     'resource/nav2_namespaced_view.rviz',
     'resource/nav2_params.yaml',
     'resource/turtlebot3_waffle.urdf',
     'resource/turtlebot3_world.yaml',
     'resource/small_house_map.pgm',
]))

data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/world', ['world/aws_house.world']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files= data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='aayush',
    maintainer_email='5160727@studenti.unige.it',
    description='TODO: Package description',
    license='TODO: License declaration',
    keywords=['ROS2', 'Gazebo', 'Robot', 'Simulation', 'box_bot'],
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],
        'console_scripts': [
            'spawn_bot = multirobots_gazebo.spawn_bot:main',
        ],
    },
)
