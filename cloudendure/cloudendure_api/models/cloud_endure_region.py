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

from cloudendure.cloudendure_api.models.cloud_endure_compute_location import (  # noqa: F401,E501
    CloudEndureComputeLocation,
)
from cloudendure.cloudendure_api.models.cloud_endure_logical_location import (  # noqa: F401,E501
    CloudEndureLogicalLocation,
)
from cloudendure.cloudendure_api.models.cloud_endure_network_interface import (  # noqa: F401,E501
    CloudEndureNetworkInterface,
)
from cloudendure.cloudendure_api.models.cloud_endure_security_group import (
    CloudEndureSecurityGroup,
)  # noqa: F401,E501
from cloudendure.cloudendure_api.models.cloud_endure_storage_location import (  # noqa: F401,E501
    CloudEndureStorageLocation,
)
from cloudendure.cloudendure_api.models.cloud_endure_subnet import (
    CloudEndureSubnet,
)  # noqa: F401,E501


class CloudEndureRegion:
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
        "subnets": "list[CloudEndureSubnet]",
        "placement_groups": "list[str]",
        "scsi_adapter_types": "list[str]",
        "instance_types": "list[str]",
        "zones": "list[str]",
        "volume_encryption_keys": "list[str]",
        "cloud": "str",
        "security_groups": "list[CloudEndureSecurityGroup]",
        "logical_locations": "list[CloudEndureLogicalLocation]",
        "static_ips": "list[str]",
        "max_cpus_per_machine": "int",
        "network_interfaces": "list[CloudEndureNetworkInterface]",
        "compute_locations": "list[CloudEndureComputeLocation]",
        "name": "str",
        "storage_locations": "list[CloudEndureStorageLocation]",
        "iam_roles": "list[str]",
        "id": "str",
        "max_cores_per_machine_cpu": "int",
        "dedicated_hosts": "list[str]",
        "network_adapter_types": "list[str]",
        "max_mb_ram_per_machine": "int",
    }

    attribute_map = {
        "subnets": "subnets",
        "placement_groups": "placementGroups",
        "scsi_adapter_types": "scsiAdapterTypes",
        "instance_types": "instanceTypes",
        "zones": "zones",
        "volume_encryption_keys": "volumeEncryptionKeys",
        "cloud": "cloud",
        "security_groups": "securityGroups",
        "logical_locations": "logicalLocations",
        "static_ips": "staticIps",
        "max_cpus_per_machine": "maxCpusPerMachine",
        "network_interfaces": "networkInterfaces",
        "compute_locations": "computeLocations",
        "name": "name",
        "storage_locations": "storageLocations",
        "iam_roles": "iamRoles",
        "id": "id",
        "max_cores_per_machine_cpu": "maxCoresPerMachineCpu",
        "dedicated_hosts": "dedicatedHosts",
        "network_adapter_types": "networkAdapterTypes",
        "max_mb_ram_per_machine": "maxMbRamPerMachine",
    }

    def __init__(
        self,
        subnets=None,
        placement_groups=None,
        scsi_adapter_types=None,
        instance_types=None,
        zones=None,
        volume_encryption_keys=None,
        cloud=None,
        security_groups=None,
        logical_locations=None,
        static_ips=None,
        max_cpus_per_machine=None,
        network_interfaces=None,
        compute_locations=None,
        name=None,
        storage_locations=None,
        iam_roles=None,
        id=None,
        max_cores_per_machine_cpu=None,
        dedicated_hosts=None,
        network_adapter_types=None,
        max_mb_ram_per_machine=None,
    ):  # noqa: E501
        """CloudEndureRegion - a model defined in Swagger"""  # noqa: E501
        self._subnets = None
        self._placement_groups = None
        self._scsi_adapter_types = None
        self._instance_types = None
        self._zones = None
        self._volume_encryption_keys = None
        self._cloud = None
        self._security_groups = None
        self._logical_locations = None
        self._static_ips = None
        self._max_cpus_per_machine = None
        self._network_interfaces = None
        self._compute_locations = None
        self._name = None
        self._storage_locations = None
        self._iam_roles = None
        self._id = None
        self._max_cores_per_machine_cpu = None
        self._dedicated_hosts = None
        self._network_adapter_types = None
        self._max_mb_ram_per_machine = None
        self.discriminator = None
        if subnets is not None:
            self.subnets = subnets
        if placement_groups is not None:
            self.placement_groups = placement_groups
        if scsi_adapter_types is not None:
            self.scsi_adapter_types = scsi_adapter_types
        if instance_types is not None:
            self.instance_types = instance_types
        if zones is not None:
            self.zones = zones
        if volume_encryption_keys is not None:
            self.volume_encryption_keys = volume_encryption_keys
        if cloud is not None:
            self.cloud = cloud
        if security_groups is not None:
            self.security_groups = security_groups
        if logical_locations is not None:
            self.logical_locations = logical_locations
        if static_ips is not None:
            self.static_ips = static_ips
        if max_cpus_per_machine is not None:
            self.max_cpus_per_machine = max_cpus_per_machine
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if compute_locations is not None:
            self.compute_locations = compute_locations
        if name is not None:
            self.name = name
        if storage_locations is not None:
            self.storage_locations = storage_locations
        if iam_roles is not None:
            self.iam_roles = iam_roles
        if id is not None:
            self.id = id
        if max_cores_per_machine_cpu is not None:
            self.max_cores_per_machine_cpu = max_cores_per_machine_cpu
        if dedicated_hosts is not None:
            self.dedicated_hosts = dedicated_hosts
        if network_adapter_types is not None:
            self.network_adapter_types = network_adapter_types
        if max_mb_ram_per_machine is not None:
            self.max_mb_ram_per_machine = max_mb_ram_per_machine

    @property
    def subnets(self):
        """Gets the subnets of this CloudEndureRegion.  # noqa: E501


        :return: The subnets of this CloudEndureRegion.  # noqa: E501
        :rtype: list[CloudEndureSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this CloudEndureRegion.


        :param subnets: The subnets of this CloudEndureRegion.  # noqa: E501
        :type: list[CloudEndureSubnet]
        """

        self._subnets = subnets

    @property
    def placement_groups(self):
        """Gets the placement_groups of this CloudEndureRegion.  # noqa: E501


        :return: The placement_groups of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._placement_groups

    @placement_groups.setter
    def placement_groups(self, placement_groups):
        """Sets the placement_groups of this CloudEndureRegion.


        :param placement_groups: The placement_groups of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._placement_groups = placement_groups

    @property
    def scsi_adapter_types(self):
        """Gets the scsi_adapter_types of this CloudEndureRegion.  # noqa: E501

        todo  # noqa: E501

        :return: The scsi_adapter_types of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._scsi_adapter_types

    @scsi_adapter_types.setter
    def scsi_adapter_types(self, scsi_adapter_types):
        """Sets the scsi_adapter_types of this CloudEndureRegion.

        todo  # noqa: E501

        :param scsi_adapter_types: The scsi_adapter_types of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._scsi_adapter_types = scsi_adapter_types

    @property
    def instance_types(self):
        """Gets the instance_types of this CloudEndureRegion.  # noqa: E501


        :return: The instance_types of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_types

    @instance_types.setter
    def instance_types(self, instance_types):
        """Sets the instance_types of this CloudEndureRegion.


        :param instance_types: The instance_types of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._instance_types = instance_types

    @property
    def zones(self):
        """Gets the zones of this CloudEndureRegion.  # noqa: E501


        :return: The zones of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this CloudEndureRegion.


        :param zones: The zones of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._zones = zones

    @property
    def volume_encryption_keys(self):
        """Gets the volume_encryption_keys of this CloudEndureRegion.  # noqa: E501


        :return: The volume_encryption_keys of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_encryption_keys

    @volume_encryption_keys.setter
    def volume_encryption_keys(self, volume_encryption_keys):
        """Sets the volume_encryption_keys of this CloudEndureRegion.


        :param volume_encryption_keys: The volume_encryption_keys of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._volume_encryption_keys = volume_encryption_keys

    @property
    def cloud(self):
        """Gets the cloud of this CloudEndureRegion.  # noqa: E501


        :return: The cloud of this CloudEndureRegion.  # noqa: E501
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CloudEndureRegion.


        :param cloud: The cloud of this CloudEndureRegion.  # noqa: E501
        :type: str
        """

        self._cloud = cloud

    @property
    def security_groups(self):
        """Gets the security_groups of this CloudEndureRegion.  # noqa: E501


        :return: The security_groups of this CloudEndureRegion.  # noqa: E501
        :rtype: list[CloudEndureSecurityGroup]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CloudEndureRegion.


        :param security_groups: The security_groups of this CloudEndureRegion.  # noqa: E501
        :type: list[CloudEndureSecurityGroup]
        """

        self._security_groups = security_groups

    @property
    def logical_locations(self):
        """Gets the logical_locations of this CloudEndureRegion.  # noqa: E501


        :return: The logical_locations of this CloudEndureRegion.  # noqa: E501
        :rtype: list[CloudEndureLogicalLocation]
        """
        return self._logical_locations

    @logical_locations.setter
    def logical_locations(self, logical_locations):
        """Sets the logical_locations of this CloudEndureRegion.


        :param logical_locations: The logical_locations of this CloudEndureRegion.  # noqa: E501
        :type: list[CloudEndureLogicalLocation]
        """

        self._logical_locations = logical_locations

    @property
    def static_ips(self):
        """Gets the static_ips of this CloudEndureRegion.  # noqa: E501


        :return: The static_ips of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._static_ips

    @static_ips.setter
    def static_ips(self, static_ips):
        """Sets the static_ips of this CloudEndureRegion.


        :param static_ips: The static_ips of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._static_ips = static_ips

    @property
    def max_cpus_per_machine(self):
        """Gets the max_cpus_per_machine of this CloudEndureRegion.  # noqa: E501

        Maximum CPUs per per Target machine (currently relevant for vCenter cloud only)  # noqa: E501

        :return: The max_cpus_per_machine of this CloudEndureRegion.  # noqa: E501
        :rtype: int
        """
        return self._max_cpus_per_machine

    @max_cpus_per_machine.setter
    def max_cpus_per_machine(self, max_cpus_per_machine):
        """Sets the max_cpus_per_machine of this CloudEndureRegion.

        Maximum CPUs per per Target machine (currently relevant for vCenter cloud only)  # noqa: E501

        :param max_cpus_per_machine: The max_cpus_per_machine of this CloudEndureRegion.  # noqa: E501
        :type: int
        """

        self._max_cpus_per_machine = max_cpus_per_machine

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this CloudEndureRegion.  # noqa: E501


        :return: The network_interfaces of this CloudEndureRegion.  # noqa: E501
        :rtype: list[CloudEndureNetworkInterface]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this CloudEndureRegion.


        :param network_interfaces: The network_interfaces of this CloudEndureRegion.  # noqa: E501
        :type: list[CloudEndureNetworkInterface]
        """

        self._network_interfaces = network_interfaces

    @property
    def compute_locations(self):
        """Gets the compute_locations of this CloudEndureRegion.  # noqa: E501

        Compute location (e.g. vCenter Host)  # noqa: E501

        :return: The compute_locations of this CloudEndureRegion.  # noqa: E501
        :rtype: list[CloudEndureComputeLocation]
        """
        return self._compute_locations

    @compute_locations.setter
    def compute_locations(self, compute_locations):
        """Sets the compute_locations of this CloudEndureRegion.

        Compute location (e.g. vCenter Host)  # noqa: E501

        :param compute_locations: The compute_locations of this CloudEndureRegion.  # noqa: E501
        :type: list[CloudEndureComputeLocation]
        """

        self._compute_locations = compute_locations

    @property
    def name(self):
        """Gets the name of this CloudEndureRegion.  # noqa: E501


        :return: The name of this CloudEndureRegion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudEndureRegion.


        :param name: The name of this CloudEndureRegion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def storage_locations(self):
        """Gets the storage_locations of this CloudEndureRegion.  # noqa: E501

        Storage location (e.g. Azure Storage Account, vCenter Data Store)  # noqa: E501

        :return: The storage_locations of this CloudEndureRegion.  # noqa: E501
        :rtype: list[CloudEndureStorageLocation]
        """
        return self._storage_locations

    @storage_locations.setter
    def storage_locations(self, storage_locations):
        """Sets the storage_locations of this CloudEndureRegion.

        Storage location (e.g. Azure Storage Account, vCenter Data Store)  # noqa: E501

        :param storage_locations: The storage_locations of this CloudEndureRegion.  # noqa: E501
        :type: list[CloudEndureStorageLocation]
        """

        self._storage_locations = storage_locations

    @property
    def iam_roles(self):
        """Gets the iam_roles of this CloudEndureRegion.  # noqa: E501


        :return: The iam_roles of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._iam_roles

    @iam_roles.setter
    def iam_roles(self, iam_roles):
        """Sets the iam_roles of this CloudEndureRegion.


        :param iam_roles: The iam_roles of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._iam_roles = iam_roles

    @property
    def id(self):
        """Gets the id of this CloudEndureRegion.  # noqa: E501


        :return: The id of this CloudEndureRegion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEndureRegion.


        :param id: The id of this CloudEndureRegion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def max_cores_per_machine_cpu(self):
        """Gets the max_cores_per_machine_cpu of this CloudEndureRegion.  # noqa: E501

        Maximum CPU cores per CPU in Target machines (currently relevant for vCenter cloud only)  # noqa: E501

        :return: The max_cores_per_machine_cpu of this CloudEndureRegion.  # noqa: E501
        :rtype: int
        """
        return self._max_cores_per_machine_cpu

    @max_cores_per_machine_cpu.setter
    def max_cores_per_machine_cpu(self, max_cores_per_machine_cpu):
        """Sets the max_cores_per_machine_cpu of this CloudEndureRegion.

        Maximum CPU cores per CPU in Target machines (currently relevant for vCenter cloud only)  # noqa: E501

        :param max_cores_per_machine_cpu: The max_cores_per_machine_cpu of this CloudEndureRegion.  # noqa: E501
        :type: int
        """

        self._max_cores_per_machine_cpu = max_cores_per_machine_cpu

    @property
    def dedicated_hosts(self):
        """Gets the dedicated_hosts of this CloudEndureRegion.  # noqa: E501


        :return: The dedicated_hosts of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._dedicated_hosts

    @dedicated_hosts.setter
    def dedicated_hosts(self, dedicated_hosts):
        """Sets the dedicated_hosts of this CloudEndureRegion.


        :param dedicated_hosts: The dedicated_hosts of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._dedicated_hosts = dedicated_hosts

    @property
    def network_adapter_types(self):
        """Gets the network_adapter_types of this CloudEndureRegion.  # noqa: E501

        todo  # noqa: E501

        :return: The network_adapter_types of this CloudEndureRegion.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_adapter_types

    @network_adapter_types.setter
    def network_adapter_types(self, network_adapter_types):
        """Sets the network_adapter_types of this CloudEndureRegion.

        todo  # noqa: E501

        :param network_adapter_types: The network_adapter_types of this CloudEndureRegion.  # noqa: E501
        :type: list[str]
        """

        self._network_adapter_types = network_adapter_types

    @property
    def max_mb_ram_per_machine(self):
        """Gets the max_mb_ram_per_machine of this CloudEndureRegion.  # noqa: E501

        Maximum MB RAM per Target machine (currently relevant for vCenter cloud only)  # noqa: E501

        :return: The max_mb_ram_per_machine of this CloudEndureRegion.  # noqa: E501
        :rtype: int
        """
        return self._max_mb_ram_per_machine

    @max_mb_ram_per_machine.setter
    def max_mb_ram_per_machine(self, max_mb_ram_per_machine):
        """Sets the max_mb_ram_per_machine of this CloudEndureRegion.

        Maximum MB RAM per Target machine (currently relevant for vCenter cloud only)  # noqa: E501

        :param max_mb_ram_per_machine: The max_mb_ram_per_machine of this CloudEndureRegion.  # noqa: E501
        :type: int
        """

        self._max_mb_ram_per_machine = max_mb_ram_per_machine

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
        if issubclass(CloudEndureRegion, dict):
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
        if not isinstance(other, CloudEndureRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other