#!/usr/bin/python

import sys
import time
from Xlib import X, display, Xutil
from Xlib.ext import randr
from Xlib import Xatom
import pyautogui
import requests

def drawText(overlay, gc, x, y, text):
    overlay.draw_text(gc, x, y, text)


def check_website_status(url):
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return "ONLINE"
        else:
            return "OFFLINE"
    except requests.RequestException:
        return "OFFLINE"

def draw_on_desktop():
    # Connect to the X server
    d = display.Display()

    root = d.screen().root


    #popup_x = 2720
    #popup_y = 0
    popup_width = 200
    popup_height = 100
    popup_x, popup_y = pyautogui.position()
    popup_y += 20
    popup_x -= 100




    # 50% opacity initially
    initial_opacity = 0xA0000000

    overlay = root.create_window(
        popup_x, popup_y, popup_width, popup_height, 0,
        d.screen().root_depth, X.InputOutput, X.CopyFromParent,
        override_redirect=True,
        background_pixel=d.screen().white_pixel,
        event_mask=X.ExposureMask
    )

    # Window settings
    overlay.set_wm_name("Overlay")
    overlay.set_wm_class("Overlay", "Overlay")

    # Set initial opacity
    opacity_atom = d.intern_atom('_NET_WM_WINDOW_OPACITY')
    overlay.change_property(opacity_atom, Xatom.CARDINAL, 32, [initial_opacity])

    overlay.map()


    shananiki = check_website_status("https://shananiki.org")
    gc = overlay.create_gc(foreground=d.screen().black_pixel)

    gc_red = overlay.create_gc(foreground=d.screen().default_colormap.alloc_color(red=65535, green=0, blue=0).pixel)
    gc_green = overlay.create_gc(foreground=d.screen().default_colormap.alloc_color(red=0, green=65535, blue=0).pixel)

    drawText(overlay, gc, 10, 10, "Shananiki:")
    if shananiki == "ONLINE":
        drawText(overlay, gc_green, 80, 10, shananiki)
    else:
        drawText(overlay, gc_red, 80, 10, shananiki)
    d.flush()

    time.sleep(2)

    # fade window out
    steps = 50
    sleep_time = 1 / steps
    for i in range(steps):
        new_opacity = int(initial_opacity * (steps - i - 1) / steps)
        overlay.change_property(opacity_atom, Xatom.CARDINAL, 32, [new_opacity])
        d.flush()
        time.sleep(sleep_time)

    overlay.unmap()
    d.flush()

if __name__ == '__main__':
    draw_on_desktop()
