from django.contrib.staticfiles.testing import LiveServerTestCase

import os
import subprocess


class Demo(LiveServerTestCase):
    def build(self):
        this_directory = os.path.dirname(os.path.abspath(__file__))
        subprocess.call([
            "node",
            os.path.join(this_directory, "build.js"),
            self.live_server_url,
            os.path.abspath("docs/demo/")
        ])
