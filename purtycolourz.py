from ggame import App
myapp = App()
myapp.run()

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
Lgreen = Color (0x00FF33, 0.95)
turqo = Color (0x40E0D0, 0.99)
Lgreen = Color (0xFF9900, 1)
black = Color(0x000000, 0.85)

thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(60, 25, thinline, Lgreen)

Sprite(rectangle)

myapp=App ()
myapp.run()