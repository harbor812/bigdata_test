# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:17:12 2019

@author: Brianzhu
"""
import xmind
from xmind.core.loader import WorkbookLoader
from xmind.core.workbook import WorkbookElement
import logging,os





def get_absolute_path(path):
    """
        Return the absolute path of a file

        If path contains a start point (eg Unix '/') then use the specified start point
        instead of the current working directory. The starting point of the file path is
        allowed to begin with a tilde "~", which will be replaced with the user's home directory.
    """
    fp, fn = os.path.split(path)
    if not fp:
        fp = os.getcwd()
    fp = os.path.abspath(os.path.expanduser(fp))
    return os.path.join(fp, fn)


#xmind_file = get_absolute_path("D:\\2\\")
#print xmind_file
#workbook = WorkbookLoader("D:\\2\\xq.xmind")  # Requires '.xmind' extension

workbook = xmind.load("D:\\2\\xq.xmind")  # Requires '.xmind' extension



xmind_content_dict = workbook.getPrimarySheet()
print xmind_content_dict.getData()
#logging.debug("loading XMind file(%s) dict data: %s", xmind_content_dict)