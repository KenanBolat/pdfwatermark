# -*- coding: utf-8 -*-
"""
Author      : Kenan Bolat
Purpose     : Insert Watermark to a pdf document
Date        : 170724
Version     : 0.0.1
License    : GNU GPLv3
"""

import os
import datetime
import time
import reportlab




class watermark:
    """ A watermark class customized with the reportlab module.
     Attributes:
        checkpage_type
        watermark_it
    """
    _papertype = {"A4":[210,297], "A0": [841, 1189], "A1": [594, 841], "A2": [420, 594], "A3": [297, 420], "A5": [148,210]}

    def __init__(self, fname, pagetype="A4"):
        self.fname = fname
        self.pagetype = pagetype

    def checkpage_type(self):
        if self.pagetype != "A4":
            raise RuntimeError('Page size must be A4 for this version of watermarking.')
        else:
            return True
    def getPageExtend(self):
        py

    def watermark_it(self,word):
        self.checkpage_type()
        self.watermarktext = word
        return True

