from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
Lgreen = Color (0x7CFC00, 0.95)
turqo = Color (0x40E0D0, 0.99)
Orange = Color (0xFF8600, 1)
black = Color(0x000000, 0.85)

thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(60, 25, thinline, Orange)

Sprite(rectangle)

myapp=App ()
myapp.run()