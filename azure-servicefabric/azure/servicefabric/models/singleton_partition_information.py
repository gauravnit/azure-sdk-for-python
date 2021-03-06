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

from .partition_information import PartitionInformation


class SingletonPartitionInformation(PartitionInformation):
    """Information about a partition that is singleton. The services with
    singleton partitioning scheme are effectively non-partitioned. They only
    have one partition.

    All required parameters must be populated in order to send to Azure.

    :param id: An internal ID used by Service Fabric to uniquely identify a
     partition. This is a randomly generated GUID when the service was created.
     The partition ID is unique and does not change for the lifetime of the
     service. If the same service was deleted and recreated the IDs of its
     partitions would be different.
    :type id: str
    :param service_partition_kind: Required. Constant filled by server.
    :type service_partition_kind: str
    """

    _validation = {
        'service_partition_kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'service_partition_kind': {'key': 'ServicePartitionKind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SingletonPartitionInformation, self).__init__(**kwargs)
        self.service_partition_kind = 'Singleton'
