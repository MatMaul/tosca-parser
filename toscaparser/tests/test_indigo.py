#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
from toscaparser.tests.base import TestCase
from toscaparser.tosca_template import ToscaTemplate


class IndigoTest(TestCase):

    def test_galaxy(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/galaxy_tosca.yaml")
        ToscaTemplate(tosca_tpl)

    def test_web_mysql(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/web_mysql_tosca.yaml")
        ToscaTemplate(tosca_tpl)

    def test_elastic_cluster(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/elastic_cluster.yaml")
        ToscaTemplate(tosca_tpl)

    def test_cellar_webapp_mysql(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/cellar_webapp_mysql.yaml")
        ToscaTemplate(tosca_tpl)

    def test_mesos_cluster(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/mesos_cluster.yaml")
        ToscaTemplate(tosca_tpl)

    def test_galaxy_elastic_cluster(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/galaxy_elastic_cluster.yaml")
        ToscaTemplate(tosca_tpl)

    def test_indigo_jobs(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/indigo_jobs.yaml")
        ToscaTemplate(tosca_tpl)

    def test_indigo_node_with_image(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/node_with_image.yaml")
        ToscaTemplate(tosca_tpl)
