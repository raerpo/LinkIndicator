#!/usr/bin/python

# minimal sample showing how to write GTK3 indicator for Ubuntu Unity
# copyright 2012 Charl P. Botha <info@charlbotha.com>
# hereby released under the BSD license.

# use the PyGObject GObject introspection to use GTK+ 3 
# also see
# http://readthedocs.org/docs/python-gtk-3-tutorial/en/latest/index.html
# http://developer.gnome.org/gtk3/stable/ (API reference)

from gi.repository import Gtk, GLib

try: 
       from gi.repository import AppIndicator3 as AppIndicator  
except:  
       from gi.repository import AppIndicator


class LinkIndicator:
       def __init__(self):
              # param1: identifier of this indicator
              # param2: name of icon. this will be searched for in the standard them
              # dirs
              # finally, the category. We're monitoring CPUs, so HARDWARE.
              self.ind = AppIndicator.Indicator.new(
                                  "Link-Indicator", 
                                  "stock_attach",
                                  AppIndicator.IndicatorCategory.OTHER)
              
              # some more information about the AppIndicator:
              # http://developer.ubuntu.com/api/ubuntu-12.04/python/AppIndicator3-0.1.html
              # http://developer.ubuntu.com/resources/technologies/application-indicators/
              
              # need to set this for indicator to be shown
              self.ind.set_status (AppIndicator.IndicatorStatus.ACTIVE)
              
              # have to give indicator a menu
              self.menu = Gtk.Menu()
              
              # you can use this menu item for experimenting
              item = Gtk.MenuItem()
              item.set_label("Buscar link")
              item.connect("activate", self.handler_menu_search)
              item.show()
              self.menu.append(item)
       
              item = Gtk.MenuItem()
              item.set_label("Insertar link")
              item.connect("activate", self.handler_menu_insert)
              item.show()
              self.menu.append(item)               
              
              # this is for exiting the app
              item = Gtk.MenuItem()
              item.set_label("Salir")
              item.connect("activate", self.handler_menu_exit)
              item.show()
              self.menu.append(item)
              
              self.menu.show()
              self.ind.set_menu(self.menu)

              
       def handler_menu_exit(self, evt):
              Gtk.main_quit()
              
       def handler_menu_search(self, evt):
              # we can change the icon at any time
              print "Iniciar busqueda de links!!"
              #self.ind.set_icon("indicator-messages-new")
       
       def handler_menu_insert(self, evt):
              window = InsertWindow()
              window.connect("delete-event", Gtk.main_quit)
              window.show_all()
              Gtk.main()
              
       def main(self):
              Gtk.main()

class InsertWindow(Gtk.Window):
       def __init__(self):
              Gtk.Window.__init__(self, title="Insertar Link")
              self.set_size_request(300,100)
              self.button = Gtk.Button(label = "Insertar")
              self.button.connect("clicked",self.handler_button_insert)
              self.add(self.button)
       def handler_button_insert(self, widget):
              print 'Insertar link...'
       

if __name__ == "__main__":
       ind = LinkIndicator()
       ind.main()


