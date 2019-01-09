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

from .cluster_event import ClusterEvent


class ClusterUpgradeDomainCompletedEvent(ClusterEvent):
    """Cluster Upgrade Domain Completed event.

    All required parameters must be populated in order to send to Azure.

    :param event_instance_id: Required. The identifier for the FabricEvent
     instance.
    :type event_instance_id: str
    :param category: The category of event.
    :type category: str
    :param time_stamp: Required. The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param target_cluster_version: Required. Target Cluster version.
    :type target_cluster_version: str
    :param upgrade_state: Required. State of upgrade.
    :type upgrade_state: str
    :param upgrade_domains: Required. Upgrade domains.
    :type upgrade_domains: str
    :param upgrade_domain_elapsed_time_in_ms: Required. Duration of domain
     upgrade in milli-seconds.
    :type upgrade_domain_elapsed_time_in_ms: float
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'target_cluster_version': {'required': True},
        'upgrade_state': {'required': True},
        'upgrade_domains': {'required': True},
        'upgrade_domain_elapsed_time_in_ms': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'target_cluster_version': {'key': 'TargetClusterVersion', 'type': 'str'},
        'upgrade_state': {'key': 'UpgradeState', 'type': 'str'},
        'upgrade_domains': {'key': 'UpgradeDomains', 'type': 'str'},
        'upgrade_domain_elapsed_time_in_ms': {'key': 'UpgradeDomainElapsedTimeInMs', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(ClusterUpgradeDomainCompletedEvent, self).__init__(**kwargs)
        self.target_cluster_version = kwargs.get('target_cluster_version', None)
        self.upgrade_state = kwargs.get('upgrade_state', None)
        self.upgrade_domains = kwargs.get('upgrade_domains', None)
        self.upgrade_domain_elapsed_time_in_ms = kwargs.get('upgrade_domain_elapsed_time_in_ms', None)
        self.kind = 'ClusterUpgradeDomainCompleted'