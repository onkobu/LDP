#/usr/bin/python
# 
# This file is part of the Lampadas Documentation System.
# 
# Copyright (c) 2000, 2001, 2002 David Merrill <david@lupercalia.net>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# 

from BaseClasses import *

# PubStatuses

class PubStatuses(DataCollection):
    """
    A collection object of all publication statuses.
    """
    
    def __init__(self):
        DataCollection.__init__(self, PubStatus,
                                 'pub_status',
                                 {'pub_status_code': 'code'},
                                 'sort_order',
                                 {'pub_status_name': 'name', 'pub_status_desc': 'description'})

class PubStatus(DataObject):
    """
    The Publication Status defines where in the publication process a
    document is.
    """
    pass

pub_statuses = PubStatuses()
pub_statuses.load()