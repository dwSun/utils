# Start terminator at anywhere inside nautilus.

# Thanks nautilus-python for provide such kind of api since nautils-actions is not available on debian or ubuntu. 

# This file is based on /usr/share/doc/python-nautilus/examples/open-terminal.py by Martin Enlund
# modified by dwSun
# usage: 
#    1 put this file into ~/.local/share/nautilus-python/extensions, mkdir if it not exist,
#    2 execute "nautilus -q" to exit nautilus
#    3 start nautilus and enjoy.

import os
import urllib

from gi.repository import Nautilus, GObject, GConf

class OpenTerminatorExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        self.client = GConf.Client.get_default()
        
    def _open_terminator(self, file):
          
        filename = urllib.unquote(file.get_uri()[7:])
        if file.is_directory():
            os.chdir(filename)
        else:
            os.chdir(os.path.dirname(filename))
        
        os.system('/usr/bin/terminator &')
        
    def menu_activate_cb(self, menu, file):
        self._open_terminator(file)
        
    def menu_background_activate_cb(self, menu, file): 
        self._open_terminator(file)
       
    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        
        file = files[0]
        if file.get_uri_scheme() != 'file':
            return
        
        item = Nautilus.MenuItem(name='NautilusPython::openterminator_file_item',
                                 label='Terminator' ,
                                 tip='Open Terminator In %s' % file.get_name())
        item.connect('activate', self.menu_activate_cb, file)
        return item,

    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(name='NautilusPython::openterminator_item',
                                 label='Terminator',
                                 tip='Open Terminator In This Directory')
        item.connect('activate', self.menu_background_activate_cb, file)
        return item,
