# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Colorspace(str, Enum):
    """
    Colorspace
    """

    """
    allowed enum values
    """
    SRGB = 'srgb'
    P3 = 'p3'

    @classmethod
    def from_json(cls, json_str: str) -> Colorspace:
        """Create an instance of Colorspace from a JSON string"""
        return Colorspace(json.loads(json_str))

