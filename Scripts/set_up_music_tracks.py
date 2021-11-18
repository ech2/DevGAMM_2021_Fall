from waapi import WaapiClient
from waapi_helpers import *

with WaapiClient() as client:
    for guid, in walk_wproj(client, '\\Interactive Music Hierarchy',
                            types=['MusicTrack'],
                            properties=['id']):
        set_property_value(client, guid, 'IsStreamingEnabled', True)
        set_property_value(client, guid, 'LookAheadTime', 150)
        set_property_value(client, guid, 'IsZeroLantency', False)
