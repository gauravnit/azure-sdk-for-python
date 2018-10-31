# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualNetwork(Model):
    """A virtual network.

    :param allowed_subnets: The allowed subnets of the virtual network.
    :type allowed_subnets: list[~azure.mgmt.devtestlabs.models.Subnet]
    :param description: The description of the virtual network.
    :type description: str
    :param external_provider_resource_id: The Microsoft.Network resource
     identifier of the virtual network.
    :type external_provider_resource_id: str
    :param subnet_overrides: The subnet overrides of the virtual network.
    :type subnet_overrides:
     list[~azure.mgmt.devtestlabs.models.SubnetOverride]
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'allowed_subnets': {'key': 'properties.allowedSubnets', 'type': '[Subnet]'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'external_provider_resource_id': {'key': 'properties.externalProviderResourceId', 'type': 'str'},
        'subnet_overrides': {'key': 'properties.subnetOverrides', 'type': '[SubnetOverride]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetwork, self).__init__(**kwargs)
        self.allowed_subnets = kwargs.get('allowed_subnets', None)
        self.description = kwargs.get('description', None)
        self.external_provider_resource_id = kwargs.get('external_provider_resource_id', None)
        self.subnet_overrides = kwargs.get('subnet_overrides', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
