# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.shared_link_create_dto import SharedLinkCreateDto  # noqa: E501

class TestSharedLinkCreateDto(unittest.TestCase):
    """SharedLinkCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SharedLinkCreateDto:
        """Test SharedLinkCreateDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SharedLinkCreateDto`
        """
        model = SharedLinkCreateDto()  # noqa: E501
        if include_optional:
            return SharedLinkCreateDto(
                album_id = '',
                allow_download = True,
                allow_upload = True,
                asset_ids = [
                    ''
                    ],
                description = '',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                show_exif = True,
                type = 'ALBUM'
            )
        else:
            return SharedLinkCreateDto(
                type = 'ALBUM',
        )
        """

    def testSharedLinkCreateDto(self):
        """Test SharedLinkCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()