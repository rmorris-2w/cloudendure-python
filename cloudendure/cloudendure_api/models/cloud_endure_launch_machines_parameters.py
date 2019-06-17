# coding: utf-8

"""
    CloudEndure API documentation

    © 2017 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    OpenAPI spec version: 5
    Contact: https://bit.ly/2T54hSc
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from cloudendure.cloudendure_api.models.cloud_endure_machine_and_point_in_time import (  # noqa: F401,E501
    CloudEndureMachineAndPointInTime
)


class CloudEndureLaunchMachinesParameters:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "items": "list[CloudEndureMachineAndPointInTime]",
        "launch_type": "str",
        "debug_scripts": "object",
    }

    attribute_map = {
        "items": "items",
        "launch_type": "launchType",
        "debug_scripts": "debugScripts",
    }

    def __init__(self, items=None, launch_type=None, debug_scripts=None):  # noqa: E501
        """CloudEndureLaunchMachinesParameters - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self._launch_type = None
        self._debug_scripts = None
        self.discriminator = None
        if items is not None:
            self.items = items
        self.launch_type = launch_type
        if debug_scripts is not None:
            self.debug_scripts = debug_scripts

    @property
    def items(self):
        """Gets the items of this CloudEndureLaunchMachinesParameters.  # noqa: E501


        :return: The items of this CloudEndureLaunchMachinesParameters.  # noqa: E501
        :rtype: list[CloudEndureMachineAndPointInTime]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CloudEndureLaunchMachinesParameters.


        :param items: The items of this CloudEndureLaunchMachinesParameters.  # noqa: E501
        :type: list[CloudEndureMachineAndPointInTime]
        """

        self._items = items

    @property
    def launch_type(self):
        """Gets the launch_type of this CloudEndureLaunchMachinesParameters.  # noqa: E501


        :return: The launch_type of this CloudEndureLaunchMachinesParameters.  # noqa: E501
        :rtype: str
        """
        return self._launch_type

    @launch_type.setter
    def launch_type(self, launch_type):
        """Sets the launch_type of this CloudEndureLaunchMachinesParameters.


        :param launch_type: The launch_type of this CloudEndureLaunchMachinesParameters.  # noqa: E501
        :type: str
        """
        if launch_type is None:
            raise ValueError(
                "Invalid value for `launch_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["TEST", "RECOVERY", "CUTOVER", "DEBUG"]  # noqa: E501
        if launch_type not in allowed_values:
            raise ValueError(
                "Invalid value for `launch_type` ({0}), must be one of {1}".format(  # noqa: E501
                    launch_type, allowed_values
                )
            )

        self._launch_type = launch_type

    @property
    def debug_scripts(self):
        """Gets the debug_scripts of this CloudEndureLaunchMachinesParameters.  # noqa: E501


        :return: The debug_scripts of this CloudEndureLaunchMachinesParameters.  # noqa: E501
        :rtype: object
        """
        return self._debug_scripts

    @debug_scripts.setter
    def debug_scripts(self, debug_scripts):
        """Sets the debug_scripts of this CloudEndureLaunchMachinesParameters.


        :param debug_scripts: The debug_scripts of this CloudEndureLaunchMachinesParameters.  # noqa: E501
        :type: object
        """

        self._debug_scripts = debug_scripts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CloudEndureLaunchMachinesParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudEndureLaunchMachinesParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
