from sys import argv
from waapi import WaapiClient
from waapi_helpers import *

selected_guid = argv[1]


with WaapiClient() as client:
    for guid, obj_type, notes in walk_wproj(client, selected_guid,
                                            properties=['id', 'type', 'notes']):
        if '@ignore' in notes:
            continue

        prop_name = 'Volume'
        if obj_type == 'Bus' or obj_type == 'AuxBus':
            prop_name = 'BusVolume'

        cur_volume = get_property_value(client, guid, prop_name)
        if cur_volume is not None:
            set_property_value(client, guid, prop_name, 0)
