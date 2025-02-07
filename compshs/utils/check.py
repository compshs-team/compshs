#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2025
@author: Simon Delarue <simon.delarue@telecom-paris.fr>
"""
import warnings


def is_zero(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError(f'Expected an integer but got {type(value).__name__}.')
    else:
        return value == 0
