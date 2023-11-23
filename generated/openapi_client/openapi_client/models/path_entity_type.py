# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PathEntityType(str, Enum):
    """
    PathEntityType
    """

    """
    allowed enum values
    """
    ASSET = 'asset'
    PERSON = 'person'
    USER = 'user'

    @classmethod
    def from_json(cls, json_str: str) -> PathEntityType:
        """Create an instance of PathEntityType from a JSON string"""
        return PathEntityType(json.loads(json_str))

