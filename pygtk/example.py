#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class CLS1(object):
    def __init__(self):
        self.mywindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.mywindow.connect("delete_event", gtk.main_quit)

        self.btn = gtk.Button("Cls1|Btn")

        self.mywindow.add(self.btn)

        self.mywindow.show_all()

    def main(self):
        gtk.main()

class CLS2(object):
    def __init__(self):
        self.mywindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.mywindow.connect("delete_event", gtk.main_quit)

        self.btn = gtk.Button("Cls2|Btn")

        self.mywindow.add(self.btn)

        self.mywindow.show_all()

    def main(self):
        gtk.main()


class APP(object):
    def __init__(self):
        self.mywindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.mywindow.connect("delete_event", gtk.main_quit)

        self.hori = gtk.HBox()

        self.btn1 = gtk.Button("AppBtn1")
        self.btn2 = gtk.Button("AppBtn2")

        self.btn1.connect("clicked", self.show_me , "AppBtn1")

        self.btn2.connect("clicked", self.show_me , "AppBtn2")

        self.hori.pack_start(self.btn1)
        self.hori.pack_start(self.btn2)

        self.mywindow.add(self.hori)

        self.mywindow.show_all()


    def show_me(self, penar, data):
        if data=="AppBtn1" :
            CLS1().main()

        if data=="AppBtn2":
            CLS2().main()

        # gtk.main_quit()

    def main(self):
        gtk.main()
if __name__ == "__main__":
    APP().main()