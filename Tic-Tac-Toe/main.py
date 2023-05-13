import dearpygui.dearpygui as dpg 

from typing import Union


dpg.create_context()
dpg.create_viewport( title = 'Tic Tac Toe', min_width = 800, min_height = 600 )
dpg.setup_dearpygui()


# RESIZE CALLBACK 
def resize( sender, data, user ):
    w     = data[2]*0.99
    h     = data[3]*0.99

    w_p   = [ w/3, w*2/3, w ]
    h_p   = [ h/3, h*2/3, h ]
    
    w_off = w*0.05
    h_off = h*0.05

    w_len = w*0.9
    h_len = h*0.9
    
    dpg.configure_item( 'draw_list', width = w, height = h )

    dpg.configure_item( 'line_h1', p1 = [w_off, h_p[0]], p2 = [w_len , h_p[0] ] )
    dpg.configure_item( 'line_h2', p1 = [w_off, h_p[1]], p2 = [w_len , h_p[1] ] )
    dpg.configure_item( 'line_w1', p1 = [w_p[0], h_off], p2 = [w_p[0], h_len  ] )
    dpg.configure_item( 'line_w2', p1 = [w_p[1], h_off], p2 = [w_p[1], h_len  ] )
    
# RENDER CALLBACK 
def render(): 
    pass 



# MENUS            
def new_game(sender, data, user):
    pass
def pop_last_game(sender, data, user):
    pass
def pop_points(sender, data, user): 
    pass


# MAIN WINDOW 
with dpg.window( tag = 'mainWindow', autosize = True, no_close = True, no_move = True, no_resize = True ): 
    with dpg.menu_bar( ):
        dpg.add_menu_item( label = 'Novo jogo'     , callback = new_game      )
        dpg.add_menu_item( label = 'Ultima vitória', callback = pop_last_game )
        dpg.add_menu_item( label = 'Pontuações'    , callback = pop_points    )



# CONFIGURATIONS
dpg.set_primary_window( 'mainWindow', True )
dpg.set_viewport_resize_callback( resize )


# HANDLERS 
with dpg.handler_registry( tag = 'handler' ):
    dpg.add_mouse_click_handler( button = dpg.mvMouseButton_Left, callback = lambda s, d, u : print( dpg.get_mouse_pos() ) )



dpg.maximize_viewport() 

dpg.show_viewport()

while dpg.is_dearpygui_running(): 
    dpg.render_dearpygui_frame() 
    render() 

dpg.stop_dearpygui() 
dpg.destroy_context() 