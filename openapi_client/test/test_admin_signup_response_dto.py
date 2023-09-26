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

from openapi_client.models.admin_signup_response_dto import AdminSignupResponseDto  # noqa: E501

class TestAdminSignupResponseDto(unittest.TestCase):
    """AdminSignupResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminSignupResponseDto:
        """Test AdminSignupResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdminSignupResponseDto`
        """
        model = AdminSignupResponseDto()  # noqa: E501
        if include_optional:
            return AdminSignupResponseDto(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '',
                first_name = '',
                id = '',
                last_name = ''
            )
        else:
            return AdminSignupResponseDto(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '',
                first_name = '',
                id = '',
                last_name = '',
        )
        """

    def testAdminSignupResponseDto(self):
        """Test AdminSignupResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()