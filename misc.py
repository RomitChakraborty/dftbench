#! /usr/bin/env python

import subprocess, re, os, time, random

def my_range(start, stop, step):
    while start < stop:
        yield start
        start += step

        
