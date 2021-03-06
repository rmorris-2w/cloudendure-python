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


class CloudEndureProject:
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
        "target_cloud_id": "str",
        "agent_installation_token": "str",
        "name": "str",
        "users_i_ds": "list[str]",
        "type": "str",
        "replication_reversed": "bool",
        "source_cloud_credentials_id": "str",
        "cloud_credentials_i_ds": "list[str]",
        "source_region": "str",
        "licenses_i_ds": "list[str]",
        "ce_admin_properties": "object",
        "replication_configuration": "str",
        "source_cloud_id": "str",
        "id": "str",
        "features": "object",
    }

    attribute_map = {
        "target_cloud_id": "targetCloudId",
        "agent_installation_token": "agentInstallationToken",
        "name": "name",
        "users_i_ds": "usersIDs",
        "type": "type",
        "replication_reversed": "replicationReversed",
        "source_cloud_credentials_id": "sourceCloudCredentialsId",
        "cloud_credentials_i_ds": "cloudCredentialsIDs",
        "source_region": "sourceRegion",
        "licenses_i_ds": "licensesIDs",
        "ce_admin_properties": "ceAdminProperties",
        "replication_configuration": "replicationConfiguration",
        "source_cloud_id": "sourceCloudId",
        "id": "id",
        "features": "features",
    }

    def __init__(
        self,
        target_cloud_id=None,
        agent_installation_token=None,
        name=None,
        users_i_ds=None,
        type=None,
        replication_reversed=None,
        source_cloud_credentials_id=None,
        cloud_credentials_i_ds=None,
        source_region=None,
        licenses_i_ds=None,
        ce_admin_properties=None,
        replication_configuration=None,
        source_cloud_id=None,
        id=None,
        features=None,
    ):  # noqa: E501
        """CloudEndureProject - a model defined in Swagger"""  # noqa: E501
        self._target_cloud_id = None
        self._agent_installation_token = None
        self._name = None
        self._users_i_ds = None
        self._type = None
        self._replication_reversed = None
        self._source_cloud_credentials_id = None
        self._cloud_credentials_i_ds = None
        self._source_region = None
        self._licenses_i_ds = None
        self._ce_admin_properties = None
        self._replication_configuration = None
        self._source_cloud_id = None
        self._id = None
        self._features = None
        self.discriminator = None
        if target_cloud_id is not None:
            self.target_cloud_id = target_cloud_id
        if agent_installation_token is not None:
            self.agent_installation_token = agent_installation_token
        if name is not None:
            self.name = name
        if users_i_ds is not None:
            self.users_i_ds = users_i_ds
        if type is not None:
            self.type = type
        if replication_reversed is not None:
            self.replication_reversed = replication_reversed
        if source_cloud_credentials_id is not None:
            self.source_cloud_credentials_id = source_cloud_credentials_id
        if cloud_credentials_i_ds is not None:
            self.cloud_credentials_i_ds = cloud_credentials_i_ds
        if source_region is not None:
            self.source_region = source_region
        if licenses_i_ds is not None:
            self.licenses_i_ds = licenses_i_ds
        if ce_admin_properties is not None:
            self.ce_admin_properties = ce_admin_properties
        if replication_configuration is not None:
            self.replication_configuration = replication_configuration
        if source_cloud_id is not None:
            self.source_cloud_id = source_cloud_id
        if id is not None:
            self.id = id
        if features is not None:
            self.features = features

    @property
    def target_cloud_id(self):
        """Gets the target_cloud_id of this CloudEndureProject.  # noqa: E501


        :return: The target_cloud_id of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._target_cloud_id

    @target_cloud_id.setter
    def target_cloud_id(self, target_cloud_id):
        """Sets the target_cloud_id of this CloudEndureProject.


        :param target_cloud_id: The target_cloud_id of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._target_cloud_id = target_cloud_id

    @property
    def agent_installation_token(self):
        """Gets the agent_installation_token of this CloudEndureProject.  # noqa: E501


        :return: The agent_installation_token of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._agent_installation_token

    @agent_installation_token.setter
    def agent_installation_token(self, agent_installation_token):
        """Sets the agent_installation_token of this CloudEndureProject.


        :param agent_installation_token: The agent_installation_token of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._agent_installation_token = agent_installation_token

    @property
    def name(self):
        """Gets the name of this CloudEndureProject.  # noqa: E501

        :return: The name of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudEndureProject.


        :param name: The name of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def users_i_ds(self):
        """Gets the users_i_ds of this CloudEndureProject.  # noqa: E501

        todo empty array unless AO or ce admin  # noqa: E501

        :return: The users_i_ds of this CloudEndureProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._users_i_ds

    @users_i_ds.setter
    def users_i_ds(self, users_i_ds):
        """Sets the users_i_ds of this CloudEndureProject.

        todo empty array unless AO or ce admin  # noqa: E501

        :param users_i_ds: The users_i_ds of this CloudEndureProject.  # noqa: E501
        :type: list[str]
        """

        self._users_i_ds = users_i_ds

    @property
    def type(self):
        """Gets the type of this CloudEndureProject.  # noqa: E501


        :return: The type of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudEndureProject.


        :param type: The type of this CloudEndureProject.  # noqa: E501
        :type: str
        """
        allowed_values = ["MIGRATION", "DR", "BACKUP"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def replication_reversed(self):
        """Gets the replication_reversed of this CloudEndureProject.  # noqa: E501


        :return: The replication_reversed of this CloudEndureProject.  # noqa: E501
        :rtype: bool
        """
        return self._replication_reversed

    @replication_reversed.setter
    def replication_reversed(self, replication_reversed):
        """Sets the replication_reversed of this CloudEndureProject.


        :param replication_reversed: The replication_reversed of this CloudEndureProject.  # noqa: E501
        :type: bool
        """

        self._replication_reversed = replication_reversed

    @property
    def source_cloud_credentials_id(self):
        """Gets the source_cloud_credentials_id of this CloudEndureProject.  # noqa: E501


        :return: The source_cloud_credentials_id of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._source_cloud_credentials_id

    @source_cloud_credentials_id.setter
    def source_cloud_credentials_id(self, source_cloud_credentials_id):
        """Sets the source_cloud_credentials_id of this CloudEndureProject.


        :param source_cloud_credentials_id: The source_cloud_credentials_id of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._source_cloud_credentials_id = source_cloud_credentials_id

    @property
    def cloud_credentials_i_ds(self):
        """Gets the cloud_credentials_i_ds of this CloudEndureProject.  # noqa: E501

        The IDs of the cloud credentials to use (array of one).  # noqa: E501

        :return: The cloud_credentials_i_ds of this CloudEndureProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._cloud_credentials_i_ds

    @cloud_credentials_i_ds.setter
    def cloud_credentials_i_ds(self, cloud_credentials_i_ds):
        """Sets the cloud_credentials_i_ds of this CloudEndureProject.

        The IDs of the cloud credentials to use (array of one).  # noqa: E501

        :param cloud_credentials_i_ds: The cloud_credentials_i_ds of this CloudEndureProject.  # noqa: E501
        :type: list[str]
        """

        self._cloud_credentials_i_ds = cloud_credentials_i_ds

    @property
    def source_region(self):
        """Gets the source_region of this CloudEndureProject.  # noqa: E501

        The ID of the region to use as source.  # noqa: E501

        :return: The source_region of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this CloudEndureProject.

        The ID of the region to use as source.  # noqa: E501

        :param source_region: The source_region of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._source_region = source_region

    @property
    def licenses_i_ds(self):
        """Gets the licenses_i_ds of this CloudEndureProject.  # noqa: E501

        The IDs of the licenses associated with this project (array of one).  # noqa: E501

        :return: The licenses_i_ds of this CloudEndureProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._licenses_i_ds

    @licenses_i_ds.setter
    def licenses_i_ds(self, licenses_i_ds):
        """Sets the licenses_i_ds of this CloudEndureProject.

        The IDs of the licenses associated with this project (array of one).  # noqa: E501

        :param licenses_i_ds: The licenses_i_ds of this CloudEndureProject.  # noqa: E501
        :type: list[str]
        """

        self._licenses_i_ds = licenses_i_ds

    @property
    def ce_admin_properties(self):
        """Gets the ce_admin_properties of this CloudEndureProject.  # noqa: E501

        For internal use.  # noqa: E501

        :return: The ce_admin_properties of this CloudEndureProject.  # noqa: E501
        :rtype: object
        """
        return self._ce_admin_properties

    @ce_admin_properties.setter
    def ce_admin_properties(self, ce_admin_properties):
        """Sets the ce_admin_properties of this CloudEndureProject.

        For internal use.  # noqa: E501

        :param ce_admin_properties: The ce_admin_properties of this CloudEndureProject.  # noqa: E501
        :type: object
        """

        self._ce_admin_properties = ce_admin_properties

    @property
    def replication_configuration(self):
        """Gets the replication_configuration of this CloudEndureProject.  # noqa: E501

        The ID of the replication configuration object to use (corresponding to the ones available in /projects/{projectId}/replicationConfigurations).  # noqa: E501

        :return: The replication_configuration of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._replication_configuration

    @replication_configuration.setter
    def replication_configuration(self, replication_configuration):
        """Sets the replication_configuration of this CloudEndureProject.

        The ID of the replication configuration object to use (corresponding to the ones available in /projects/{projectId}/replicationConfigurations).  # noqa: E501

        :param replication_configuration: The replication_configuration of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._replication_configuration = replication_configuration

    @property
    def source_cloud_id(self):
        """Gets the source_cloud_id of this CloudEndureProject.  # noqa: E501


        :return: The source_cloud_id of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._source_cloud_id

    @source_cloud_id.setter
    def source_cloud_id(self, source_cloud_id):
        """Sets the source_cloud_id of this CloudEndureProject.


        :param source_cloud_id: The source_cloud_id of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._source_cloud_id = source_cloud_id

    @property
    def id(self):
        """Gets the id of this CloudEndureProject.  # noqa: E501


        :return: The id of this CloudEndureProject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEndureProject.


        :param id: The id of this CloudEndureProject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def features(self):
        """Gets the features of this CloudEndureProject.  # noqa: E501


        :return: The features of this CloudEndureProject.  # noqa: E501
        :rtype: object
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this CloudEndureProject.


        :param features: The features of this CloudEndureProject.  # noqa: E501
        :type: object
        """

        self._features = features

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
        if issubclass(CloudEndureProject, dict):
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
        if not isinstance(other, CloudEndureProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
