import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.create_viewport( title = 'Default DPG window', min_width = 800, min_height = 600 )
dpg.setup_dearpygui()

def resize( sender, data, user ):
    print( data ) 


with dpg.window( tag = 'mainWindow', autosize = True, no_close = True, no_move = True, no_resize = True ): 
    pass  
    




dpg.set_primary_window( 'mainWindow', True )
dpg.set_viewport_resize_callback( resize )

dpg.maximize_viewport() 

dpg.show_viewport()
while dpg.is_dearpygui_running(): 
    dpg.render_dearpygui_frame() 



dpg.stop_dearpygui() 
dpg.destroy_context() 