from os import path
from nicegui import ui

ui.page_title('Recyclarr GUI Setup')

##TODO: need to check OS to get default location ## https://recyclarr.dev/wiki/file-structure/#appdata-directory
installpath = '/usr/local/bin/recyclarr'
#Check if file exists"
if(path.isfile(installpath)):
    ui.label('Recyclarr Installation Found!')
    ##TODO Load Configuration page ##
else:
    ui.label('Recyclarr Installation Not Found!')
    #TODO Load Setup page ##

ui.run()