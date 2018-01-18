#!/usr/bin/env python3

import cv2
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0),
                                              self._windowManager, True)
        self._sharpenFilter = filters.SharpenFilter()
        self._findedgesFilter = filters.FindEdgesFilter()
        self._blurFilter = filters.BlurFilter()
        self._embossFilter = filters.EmbossFilter()

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            #filters.strokeEdges(frame, frame)
            #self._sharpenFilter.apply(frame, frame)
            #self._findedgesFilter.apply(frame, frame)
            #self._blurFilter.apply(frame, frame)
            #self._embossFilter.apply(frame, frame)
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """Handle a keypress.

        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit

        """
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingvideo(
                    'screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()
