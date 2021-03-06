#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2014-09-15 20:49:22 +0100 (Mon, 15 Sep 2014)
#
#  https://github.com/harisekhon/pylib
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback
#  to help improve or steer this or other code I publish
#
#  https://www.linkedin.com/in/harisekhon
#

"""
# ============================================================================ #
#                   PyUnit Tests for HariSekhon.RestVersionNagiosPlugin
# ============================================================================ #
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import sys
import unittest
libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(libdir)
# pylint: disable=wrong-import-position
from harisekhon.utils import log
from harisekhon.nagiosplugin import RestVersionNagiosPlugin

class RestVersionNagiosPluginTester(unittest.TestCase):

    # must prefix with test_ in order for the tests to be called

    # Not using assertRaises >= 2.7 and maintaining compatibility with Python 2.6 servers

    class SubRestVersionNagiosPlugin(RestVersionNagiosPlugin):
        def parse(self, req):
            pass

    def setUp(self):
        self.plugin = self.SubRestVersionNagiosPlugin()

    def test_unknown_exit(self):
        try:
            self.plugin.main()
            raise Exception('RestVersionSub plugin failed to terminate')
        except SystemExit as _:
            if _.code != 3:
                raise Exception('RestVersionNagiosPlugin failed to exit UNKNOWN (3), got exit code {0} instead'
                                .format(_.code))

    def test_plugin_abstract(self):  # pylint: disable=no-self-use
        try:
            RestVersionNagiosPlugin()  # pylint: disable=abstract-class-instantiated
            #raise Exception('failed to raise a TypeError when attempting to instantiate abstract class ' +
            #                'RestVersionNagiosPlugin')
        #except TypeError:
        except SystemExit as _:
            if _.code != 0:
                raise Exception('RestVersionNagiosPlugin failed to exit UNKNOWN (3), got exit code {0} instead'
                                .format(_.code))


def main():
    # increase the verbosity
    # verbosity Python >= 2.7
    #unittest.main(verbosity=2)
    log.setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(RestVersionNagiosPluginTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
