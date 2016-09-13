from ggame import  App, Color, LineStyle, Sprite
from ggame import  CircleAsset

#colors: <http://www.december.com/html/spec/color>

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
crimson = Color(0xA02422, 0.97000000000000000000000000000000000000000000000000000000000000000000000001)

thinline = LineStyle(.000001, black)
noline = Linestyle(0, blue)
mycircle = CircleAsset(5, thinline, blue)
urcircle = CircleAsset(8, noline, crimson)
xcoordinates = range(100, 600, 10)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (x, x*0.5 + 100)) for x in xcoordinates]

myapp = App()
myapp.run()
