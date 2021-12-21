import sys
import xbmcaddon
import xbmc

Addon = xbmcaddon.Addon('script.screensaver.quit')

__scriptname__ = Addon.getAddonInfo('name')
__path__ = Addon.getAddonInfo('path')

if __name__ == '__main__':
    xbmc.executebuiltin('Quit')
