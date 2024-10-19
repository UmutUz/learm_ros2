import os
from glob import glob
from setuptools import setup

package_name = 'learm_ros2_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (os.path.join('share', package_name), glob('meshes/*.stl')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andrewda',
    maintainer_email='andrewda@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'follower = learm_ros2.follower:main'
        ],
    },
)
