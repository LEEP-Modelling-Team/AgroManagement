# -*- coding: utf-8 -*-
# Copyright (c) 2023 LEEP, University of Exeter (UK)
# Mattia Mancini (m.c.mancini@exeter.ac.uk), December 2023
# ========================================================
"""
agromanagement package initialisation file
"""

from agromanagement.core.config_parser import ConfigReader
from agromanagement.utility.paths import ROOT_DIR

config_path = ROOT_DIR + "\\config.ini"
# pylint: disable=E1101
app_config = ConfigReader(config_path)
# pylint: enable=E1101
