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


class SmartGroupModificationProperties(Model):
    """Properties of the smartGroup modification item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar smart_group_id: Unique Id of the smartGroup for which the history is
     being retrieved
    :vartype smart_group_id: str
    :param modifications: Modification details
    :type modifications:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupModificationItem]
    :param next_link: URL to fetch the next set of results.
    :type next_link: str
    """

    _validation = {
        'smart_group_id': {'readonly': True},
    }

    _attribute_map = {
        'smart_group_id': {'key': 'smartGroupId', 'type': 'str'},
        'modifications': {'key': 'modifications', 'type': '[SmartGroupModificationItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SmartGroupModificationProperties, self).__init__(**kwargs)
        self.smart_group_id = None
        self.modifications = kwargs.get('modifications', None)
        self.next_link = kwargs.get('next_link', None)
