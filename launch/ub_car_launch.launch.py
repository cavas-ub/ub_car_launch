# Copyright 2021 University of Buffalo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

"""

import launch
import os

from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def get_share_file_path(package_name, file_name):
    return os.path.join(get_package_share_directory(package_name), file_name)

def generate_launch_description():
    """Launch stuff for UB car"""

    dataspeed_dbw = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
            get_share_file_path('dbw_ford_can', 'launch/dbw.launch.xml')
        ),
        launch_arguments={
            "ulc": "false"
        }.items()
    )

    dataspeed_interface = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            get_share_file_path('dataspeed_ford_interface', 'launch/dataspeed_ford_interface.launch.py')
        ),
        launch_arguments={}.items()
    )

    return launch.LaunchDescription([dataspeed_dbw, dataspeed_interface])
