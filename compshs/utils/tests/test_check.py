#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests for check.py"""
import unittest

from compshs.utils.check import *


class TestChecks(unittest.TestCase):

    def test_check_is_zero(self):
        with self.assertRaises(TypeError):
            is_zero('toto')
        assert is_zero(0) is True
        assert is_zero(-1) is False
