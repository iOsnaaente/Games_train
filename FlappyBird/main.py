import dearpygui.dearpygui as dpg 

dpg.draw_
IMG_SPRITES = [ ]

dpg.create_context()
dpg.create_viewport( title = 'Flappy Birds - The game', min_width = 800, min_height = 600 )
dpg.setup_dearpygui()

def load_image( img_path : str ): 
    w, h, c, d = dpg.load_image( img_path )
    with dpg.texture_registry( tag = img_path ): 
        return dpg.add_static_texture( w, h, d, parent = img_path )


with dpg.window( tag = 'mainWindow', autosize = True, no_close = True, no_move = True, no_resize = True ): 
    img_sprites = load_image( 'sprites/flappy-birds-sprites.png' )
    #dpg.add_image( img_sprites, tag = 'img-sprites', uv_min = [0,0], uv_max = [1,1] )
    dpg.draw_image_quad()
    
dpg.set_primary_window('mainWindow', True )

dpg.show_viewport()
while dpg.is_dearpygui_running(): 
    dpg.render_dearpygui_frame() 



dpg.stop_dearpygui() 
dpg.destroy_context()

