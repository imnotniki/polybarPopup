## Example
![](https://raw.githubusercontent.com/imnotniki/polybarPopup/main/example.gif)

## Requirements

- python-xlib
- pyautogui
- requests
- python3

### **Arch**
**Install python libs:**
```bash
sudo pacman -S python-xlib python-requests
```
```bash
yay -S pyautogui
```
**Install polybar:**
```bash
sudo pacman -S polybar
```
**Polybar module in your polybar config.ini:**
```bash
[module/custompy]
type = custom/text
content = " "
click-left = python3 ~/PycharmProjects/polybarAddon/main.py
```


### How to draw text for now

Change foreground pixelcolor using the graphicscomponent and then use drawText passing overlay, gc, x, y and the string:
```python
gc = overlay.create_gc(foreground=d.screen().black_pixel)
drawText(overlay, gc, 10, 10, "Shananiki:")
```
