from tkinter import Tk, messagebox
from waapi import WaapiClient
from waapi_helpers import *

tk = Tk()
tk.withdraw()

events = []
with WaapiClient() as client:
    for guid, name in walk_wproj(client,
                                 start_guids_or_paths='\\Events',
                                 properties=['id', 'name'],
                                 types=['Event']):
        events.append(name)
messagebox.showinfo('Hi DevGAMM', '\n'.join(events))



tk.quit()
