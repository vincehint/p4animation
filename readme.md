# Using Python in Blender

## Why?
I've always had an interest in animation and am a creative type so I tried to find my way through Blender Animation Studio using Python. Blender has it's own Python formatting and keywords that are automatically loaded in, but because it's Python you can import all of the regular libraries that you would use outside of Blender.

## How this all went down
I went in to this project hoping to create a simple animation using Python scripting inside of Blender. This did not go as well as planned. I quickly learned that animation using Python is not easy and requires a lot of knowledge of geometry. What I did find Python to be most useful for was creating tools to use inside the interface that made animating easier. You are able to create new nodes using Python and you can either install them directly to the interface or keep them locally to run only when needed.

## Pros of Using Python
While it is next level code that brings your animations to life using motion, it is very possible to make a more user friendly interface for those of us that don't want to memorize hotkeys. It is mildly simple to create new menus, brushes, and textures. It is possible to create new meshes or figures and render them directly to your scene using Python, and it is possible to make them move. 

## Cons of Using Python
As I said before, it is possible to animate objects using Python but it requires extensive lines of code, and an intimate knowledge of both geometry and physics (yes, physics Blender is not playing). I did get a very short two movement animation to render but that is where it stops. More research and learning will eventually give me the ability to do this but until then, that's where we're at.

Another con of using Python in Blender 2.9 is a lack of resources. While Blender does have a small guide written on the resource site, there are not a lot of people with the know-how to make things happen. 

## Ok so, what did you create then?
What is here is my start at adding my own nodes. I created a shader library feature, which will show a list of shaders that I created. I built out one shader, the diamond shader, which will make the selected object transparent and reflective like a diamond. I also but an addon called Add Tetrahedron which renders a small pyramid in the middle of the page. I then created a small animation of a ball in which it moves back and forth on the page. Then, for my own sanity, I created a short explosion animation (not using python), just to say I animated something.

## How Do I Use Them?
Well, first you need to for and clone this repo. You will need to use VSCode. Once you have cloned the repo and saved it in your VSCode you will need to download Blender 2.9. In Blender 2.9 go to the scripting tab and then open the file of your choosing.

### For addObject.py
Open the addObject.py file in your scripting area and click the triangle to run. Once finished a menu will pop up on the right side of your layout view which you can get to using the small triangle pointing left. At the bottom will be "shapes". From there you can click a shape and it will populate in the middle of your layout.

### For anim.py
Open the anim.py in your scripting area of blender and click the triangle to run. Once the code has run go to you animation panel and click play.

### For ShaderLibrary.py
Open this in your scripting tab and run it. A menu will appear on the upper right side of your layout tab called Misc. This will have the shader menu. To use it, select the object you want to modify and then click the shader that you'd like to apply.

### makeObjects.py
Open this file in your scripting tab and run it. Go into your layout tab and click f3. A search menu will appear start to type tetrahedron and an Add Tetrahedron button will appear. Click that and a small pyramid will render in the middle of your scene.

### minecraftanimation.blender
This one you can just open in Blender normally. Go to file, click Open, and then select the file. Once it's rendered click play.

## MVP And StretchGoals
My MVP started as creating a short animation in blender. It was later ammended to be able to manipulate objects and create new nodes in Blender. 

Stretch goals were to actually stylize the animation so it wasn't just grey. 

## Helpful Stuff

Make sure you save often when running Python in Blender as Python has a tendancy to crash the program.

Here is a link to the blender documentation for using Python: https://docs.blender.org/api/current/info_quickstart.html

Here is a link to the github repository: https://github.com/vincehint/p4animation

