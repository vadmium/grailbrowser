# Copyright (c) CNRI 1996, licensed under terms and conditions of license
# agreement obtained from handle "hdl:CNRI.License/Grail-Version-0.3",
# URL "http://grail.cnri.reston.va.us/LICENSE-0.3/", or file "LICENSE".

"""grail: URI scheme handler."""

import grailutil
from nullAPI import null_access

class grail_access(null_access):

    def __init__(self, url, method, params):
	null_access.__init__(self, url, method, params)
	file = grailutil.which(url)
	if not file: raise IOError, "Grail file %s not found" % `url`
	self.url = "file:" + file

    def getmeta(self):
	null_access.getmeta(self)	# assert, state change
	return 301, "Redirected", {'location': self.url}