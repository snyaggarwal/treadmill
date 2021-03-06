"""Unit test for zknamespace.
"""

import unittest

# Disable W0611: Unused import
import tests.treadmill_test_deps  # pylint: disable=W0611

from treadmill import zknamespace as z


class ZknamespaceTest(unittest.TestCase):
    """Mock test for treadmill.zknamespace."""

    def test_join_zookeeper_path(self):
        """Checks zookeeper path construction."""

        path = z.join_zookeeper_path('/root', 'node')
        self.assertEquals('/root/node', path)

        path = z.join_zookeeper_path('/root', 'node1', 'node2')
        self.assertEquals('/root/node1/node2', path)


if __name__ == "__main__":
    unittest.main()
