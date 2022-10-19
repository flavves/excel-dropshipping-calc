# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:45:01 2022

@author: okmen
"""

from setuptools import setup

APP=["macdeneme.py"]

OPTIONS = {
    "argv_emulation":True,
    }

setup(
      app=APP,
      options={"py2app":OPTIONS},
      setup_requries=["py2app"]
      )