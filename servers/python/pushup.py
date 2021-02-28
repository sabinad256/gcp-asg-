# Copyright 2016 Google Inc. All rights reserved.
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

"""Create nodejs template with the back-end and front-end templates."""


def GenerateConfig(context):
  """Generate configuration."""

  server = context.env['deployment'] + '-server'
  firewall = context.env['deployment'] + '-application-fw'
  #mysql = context.env['deployment'] + '-mysql'

  application_port = 80

  resources = [{
      'name': server,
      'type': 'server.py',
      'properties': {
          'zone': context.properties['zone'],
          'dockerImage': context.properties['image'],
          'port': application_port,
          'machineType': context.properties['machine'],
          # # Define the variables that are exposed to container as env variables.
          # 'dockerEnv': {
          #     'SEVEN_SERVICE_MYSQL_PORT': mysql_port,
          #     'SEVEN_SERVICE_PROXY_HOST': '$(ref.' + mysql
          #                                 + '.networkInterfaces[0].networkIP)'
          # },
          # If left out will default to 1
          'size': 2,
          # If left out will default to 1
          'maxSize': 20
      }
  }, {
      'name': firewall,
      'type': 'compute.v1.firewall',
      'properties': {
          'allowed': [{
              'IPProtocol': 'TCP',
              'ports': [application_port]
          }],
          'sourceRanges': ['0.0.0.0/0']
      }
  }]
  return {'resources': resources}
