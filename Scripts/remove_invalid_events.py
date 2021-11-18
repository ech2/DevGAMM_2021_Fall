from waapi import WaapiClient
from waapi_helpers import *

action_types_to_check = {1, 2, 7, 9, 34, 37, 41}


def should_check_ref(action_type):
    return action_type in action_types_to_check


with WaapiClient() as client:
    for event_guid, event_name in walk_wproj(client, '\\Events',
                                             types=['Event'],
                                             properties=['id', 'name']):
        num_valid_actions = 0
        for action_id, action_type, target in walk_wproj(client,
                                                         event_guid,
                                                         types=['Action'],
                                                         properties=['id', 'ActionType', 'Target']):
            if should_check_ref(action_type):
                ref_obj = get_object(client, target['id'])
                if ref_obj is not None:
                    num_valid_actions += 1
            else:
                num_valid_actions += 1

        if num_valid_actions == 0:
            delete_object(client, event_guid)
            print('delete', event_name)
