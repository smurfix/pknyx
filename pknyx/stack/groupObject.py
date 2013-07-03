# -*- coding: utf-8 -*-

""" Python KNX framework

License
=======

 - B{pKNyX} (U{http://www.pknyx.org}) is Copyright:
  - (C) 2013 Frédéric Mantegazza

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
or see:

 - U{http://www.gnu.org/licenses/gpl.html}

Module purpose
==============

Group data service management

Implements
==========

 - B{GroupObject}

Documentation
=============

B{GroupObject} are used by L{Datapoint<pknyx.core.datapoint>} to communicate over the bus using group data service.

Usage
=====

@author: Frédéric Mantegazza
@copyright: (C) 2013 Frédéric Mantegazza
@license: GPL
"""

__revision__ = "$Id$"

from pknyx.common.exception import PKNyXValueError
from pknyx.logging.loggingServices import Logger


class GroupObjectValueError(PKNyXValueError):
    """
    """


class GroupObject(object):
    """ GroupObject class

    @ivar _group: group where this group object belongs
    @type _group: L{Group<pknyx.core.group>}
    """
    def __init__(self, group):
        """

        @param group: group to add this group object to
        @type group: L{Group<pknyx.core.group>}

        raise GroupObjectValueError:
        """
        super(GroupObject, self).__init__()

        self._group = group

    def groupValueWrite(self, src, data, priority):
        """ Write data request on the GAD associated with this group
        """
        self._group.groupValueWrite(src, data, priority)

    def groupValueRead(self, src, priority):
        """ Read data request on the GAD associated with this group
        """
        self._group.groupValueRead(src, priority)

    def groupValueResponse(self, src, data, priority):
        """ Response data request on the GAD associated with this group
        """
        self._group.groupValueResponse(src, data, priority)


if __name__ == '__main__':
    import unittest

    # Mute logger
    Logger().setLevel('error')


    class GroupObjectTestCase(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_constructor(self):
            pass


    unittest.main()