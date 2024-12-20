#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

PORT=8509
PIN_MAP_bg={
    3:2,
    5:3,
    7:4,
    29:5,
    31:6,
    26:7,
    24:8,
    21:9,
    19:10,
    23:11,
    32:12,
    33:13,
    8:14,
    10:15,
    36:16,
    11:17,
    12:18,
    35:19,
    38:20,
    40:21,
    15:22,
    16:23,
    18:24,
    22:25,
    37:26,
    13:27
}
evalAllowed=(type(None),int,str,float,bool,str)
