from typing import Union
import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.create_viewport( title = 'Tic Tac Toe', min_width = 800, min_height = 600 )
dpg.setup_dearpygui()

THICKNESS = 5 

quadrants = []
jogadas = [] 
jogada = 1

def resize( sender, data, user ):
    global quadrants
    
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
    
    quadrants = []
    for y in h_p:
        for x in w_p:
            quadrants.append( [x-w/3, y-h/3] )
            quadrants.append( [x, y] )

def draw_X( parent : Union[str, int], p1 : list, p2 : list, jogada : int  ):
    dx = p1[1] - p1[0]
    dy = p2[1] - p2[1]
    off = min([dx, dy])*0.1
    line_m = dpg.draw_line( parent = parent, p1 = [p1[0]+off, p1[1]-off], p2 = [ p2[1]+off, p2[1]-off], thickness = THICKNESS, tag = dpg.generate_uuid() )
    line_p = dpg.draw_line( parent = parent, p1 = [p1[0]+off, p2[1]-off], p2 = [ p2[0]-off, p1[1]+off], thickness = THICKNESS, tag = dpg.generate_uuid() )
    jogadas.append( [ [line_m, line_p], 'X'] )
    print( 'draw X in %s %s' %(p1, p2))

def draw_O( parent : Union[str, int], p1 : list, p2 : list, jogada : int ):
    dx = p1[1] - p1[0]
    dy = p2[1] - p2[1]
    off = min([dx, dy])*0.45
    circle = dpg.draw_circle( parent = parent, center = [p1[0]+dx, p1[1]+dy], radius = off, thickness = THICKNESS, tag = dpg.generate_uuid() )
    jogadas.append( [circle, 'O'] )
    print( 'draw O in %s %s' %(p1, p2))

def make_play( sender, data, user ): 
    global quadrants, jogada
    x, y = dpg.get_drawing_mouse_pos( )
    print( 'Mouse Pos : ', x, y)
    for i in range(0,len(quadrants),2):
        if x > quadrants[i][0] and x < quadrants[i+1][0]:
            if y > quadrants[i][1] and x < quadrants[i+1][1]:
                if jogada%2 == 0: draw_O( user, quadrants[i], quadrants[i+1], jogada )
                else:               draw_X( user, quadrants[i], quadrants[i+1], jogada)
                jogada += 1
                print( jogada)
def new_game(sender, data, user):
    if jogada > 1:
        pass 

def pop_last_game(sender, data, user):
    pass

def pop_points(sender, data, user): 
    pass



with dpg.window( tag = 'mainWindow', autosize = True, no_close = True, no_move = True, no_resize = True ): 
    with dpg.menu_bar( ):
        dpg.add_menu_item( label = 'Novo jogo'     , callback= new_game )
        dpg.add_menu_item( label = 'Ultima vitória', callback= pop_last_game )
        dpg.add_menu_item( label = 'Pontuações'    , callback= pop_points )

        with dpg.drawlist( tag = 'draw_list', parent = 'mainWindow', width= 900, height= 600, pos=[10,25], ):
            dpg.draw_line( p1 = [0,0], p2 = [0,0], tag = 'line_h1', parent = 'draw_list', thickness = THICKNESS, color = [255,255,255,255] )
            dpg.draw_line( p1 = [0,0], p2 = [0,0], tag = 'line_h2', parent = 'draw_list', thickness = THICKNESS, color = [255,255,255,255] )
            dpg.draw_line( p1 = [0,0], p2 = [0,0], tag = 'line_w1', parent = 'draw_list', thickness = THICKNESS, color = [255,255,255,255] )
            dpg.draw_line( p1 = [0,0], p2 = [0,0], tag = 'line_w2', parent = 'draw_list', thickness = THICKNESS, color = [255,255,255,255] )

dpg.set_primary_window( 'mainWindow', True )
dpg.set_viewport_resize_callback( resize )

with dpg.handler_registry( tag = 'handler' ):
    dpg.add_mouse_click_handler( button = dpg.mvMouseButton_Left, callback = make_play, user_data = 'draw_list' )

dpg.maximize_viewport() 


dpg.show_viewport()
while dpg.is_dearpygui_running(): 
    dpg.render_dearpygui_frame() 

dpg.stop_dearpygui() 
dpg.destroy_context() 