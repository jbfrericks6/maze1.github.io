import PySimpleGUIWeb as sg
import PIL.Image
import io
import base64

def convert_to_bytes(file_or_bytes, resize=None):
  
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()
image = sg.Image(filename = ('player.png'), key = 'playerImage')
image.Position = (200,200)

graph = sg.Graph(canvas_size = (800, 800), graph_bottom_left = (0, 800), graph_top_right=(800, 0), background_color = 'blue',key = 'mazeGraph')
maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,
                     1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1, 
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,
                     1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

layout=[[graph, sg.Text('hello world'), image]]
win = sg.Window('hello', layout,
                web_port=80)
while True:
    event, values = win.Read()
    if event is None:
        break