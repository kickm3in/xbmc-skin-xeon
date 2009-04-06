#
# coding: utf-8

import os, xbmc, xbmcgui, sys, string
HOME_DIR = os.getcwd().replace(";","")+"\\"
LANGUAGE = []
#result = xbmcgui.Dialog().browse(1,LANGUAGE[1],"files")

#if os.path.isfile('Q:\\changelog2.txt') == False: dialog = xbmcgui.Dialog()
												  #dialog.ok("Error", "Could not open file.")
result = 'Q:\\changelog.txt'	 
 
if (xbmc.getLanguage().lower() == 'english'):
  LANGUAGE = ['Open', 'Open file...', '']

if (xbmc.getLanguage().lower() == 'swedish'):
  LANGUAGE = [u'Öppna', u'Öppna fil...', '']

class GUI(xbmcgui.Window):
  def __init__(self):
    self.addControl(xbmcgui.ControlImage(0,0, 720,576, HOME_DIR+'gfx\\background.png'))
    self.theList = xbmcgui.ControlList(30, 35, 640, 500, "font12","0xFFFFFFFF",HOME_DIR+"gfx\\list-nofocus.png",HOME_DIR+"gfx\\list-focus.png",itemTextXOffset=4)
    self.theLabel = xbmcgui.ControlLabel(40,516, 300,35, '')
    self.theButton = xbmcgui.ControlButton(584, 512, 90, 30, LANGUAGE[0], HOME_DIR+"gfx\\button-focus.png", HOME_DIR+"gfx\\button-nofocus.png", 30, 2 , 0 , 'font12')
    self.addControl(self.theButton)
    self.addControl(self.theLabel)
    self.addControl(self.theList)
    self.setFocus(self.theButton)
    self.theButton.controlUp(self.theList)
    self.theButton.controlDown(self.theList)
    self.theButton.controlLeft(self.theList)
    self.theButton.controlRight(self.theList)	
    self.theList.controlUp(self.theButton)
    self.theList.controlDown(self.theButton)
    self.theList.controlLeft(self.theButton)
    self.theList.controlRight(self.theButton)	
    #result = 'Q:\\changelog.txt'
    self.theLabel.setLabel(result)
    f = open(result, 'r')
    for line in f.readlines():
      listitem = xbmcgui.ListItem()
    #  listitem.setLabel(str(line))
    #  self.theList.addItem(listitem)
	
	
  def onControl(self, control):
    if control == self.theButton:
      #result = 'Q:\\changelog.txt'
      self.theLabel.setLabel(result)
      #self.theList.reset()
      f = open(result, 'r')
      for line in f.readlines():
        listitem = xbmcgui.ListItem()
        listitem.setLabel(str(line))
        self.theList.addItem(listitem)

gui = GUI()
gui.doModal()
del gui