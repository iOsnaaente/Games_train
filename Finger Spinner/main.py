import dearpygui.dearpygui as dpg 
import math 

ANGLE_SPINS = 0 
NUM_SPINS   = 3 

ROTATING    = True 

MAX_SPINS   = 15
MIN_SPINS   = 2 

SPINS_OFFSET    = 360 / NUM_SPINS 
SPINS_DISTANCE  = 300
SPINS_RADIUS    = 50 
SPINS_COLOR     = [200,10,50,255]
SPINS_FILL      = [200,200,200,255]
SPINS_THICKNESS = 20

VEL_ANGULAR     = 10
POS_REF         = 0
FRICTION        = 0.01 

SHOW_COLOR_PICKER  = False 

def show_or_hide_color_picker(sender, data, user ): 
    global SHOW_COLOR_PICKER
    if SHOW_COLOR_PICKER:
        dpg.show_item( 'Color_picker_color' )
        dpg.show_item( 'Color_picker_fill' )
    else:
        dpg.hide_item( 'Color_picker_color' )
        dpg.hide_item( 'Color_picker_fill' )
    
    SHOW_COLOR_PICKER = not SHOW_COLOR_PICKER
        
def get_force(sender, data, user ):
    global VEL_ANGULAR
    pos_i = dpg.get_mouse_pos()
    while dpg.is_mouse_button_down( dpg.mvMouseButton_Left ):
        pass 
    pos_f = dpg.get_mouse_pos()
    
    center = [ dpg.get_item_width('mainWindow')/2, dpg.get_item_height('mainWindow')/2 ]
    pos_i[0] -= center[0]
    pos_f[0] -= center[0]
    pos_i[1] = center[1] - pos_i[1]
    pos_f[1] = center[1] - pos_f[1]

    if pos_i[0]-pos_f[0] == 0  and pos_i[1]-pos_f[1] == 0 :
        pass 
    else: 
        ri =math.sqrt( pos_i[0]**2 + pos_i[1]**2 )
        rf = math.sqrt( pos_f[0]**2 + pos_f[1]**2 )
        oi = math.atan(pos_i[1]/pos_i[0] if pos_i[0] != 0 else 0 )
        of = math.atan(pos_f[1]/pos_f[0] if pos_f[0] != 0 else 0 )

        mod =   rf*of - ri*oi
        
        VEL_ANGULAR += mod 
        
        print( sender, data, user, pos_i, mod )

def make_spinner_spin(sender, data, user):
    global ROTATING
    ROTATING = True 

def stop_spinner(sender, data, user):
    global ROTATING
    ROTATING = False 

def change_spinner_color(sender, data, user):
    global SPINS_COLOR 
    SPINS_COLOR = [ color*255 for color in data  ]
    for spin in range(NUM_SPINS):
        dpg.configure_item('Spins{}'.format(spin), color = SPINS_COLOR )
    dpg.configure_item('centerSpinner', color = SPINS_COLOR )
    print( SPINS_COLOR )

def change_spinner_fill_color (sender, data, user):
    global SPINS_FILL
    SPINS_FILL = [ color*255 for color in data  ]
    for spin in range(NUM_SPINS):
        dpg.configure_item('Spins{}'.format(spin), fill = SPINS_FILL )
        dpg.configure_item('SpinArm{}'.format(spin), color = SPINS_FILL )
    dpg.configure_item('centerSpinner', fill = SPINS_FILL )
    print( SPINS_FILL )

def resize_windows( sender, data, user ): 
    global NUM_SPINS
    w, h = dpg.get_item_width('mainWindow'), dpg.get_item_height('mainWindow')
    dpg.configure_item( 'SpinnerDrawlist', width= w*0.95, height= h*0.95, pos=[w*0.025, h*0.025] )
    dpg.configure_item( 'centerSpinner', center= [w/2, h/2], radius= SPINS_RADIUS*2 )
    for spin in range(MAX_SPINS):
        center = [w/2 + SPINS_DISTANCE*math.cos( math.radians(spin*SPINS_OFFSET)) , h/2 + SPINS_DISTANCE*math.sin( math.radians(spin*SPINS_OFFSET)) ]
        dpg.configure_item('Spins{}'.format(spin)  , center = center, radius = SPINS_RADIUS, thickness = SPINS_THICKNESS, color=SPINS_COLOR, fill=SPINS_FILL )        
        dpg.configure_item('SpinArm{}'.format(spin), p1 = center    , p2 = [w/2, h/2]      , color = SPINS_FILL )
        if not( spin < NUM_SPINS ):
            dpg.hide_item('SpinArm{}'.format(spin))
            dpg.hide_item('Spins{}'.format(spin))
        else:
            dpg.show_item('SpinArm{}'.format(spin))
            dpg.show_item('Spins{}'.format(spin))

def increase_spinner_pins( sender, data, user ): 
    global NUM_SPINS
    global SPINS_OFFSET
    global FRICTION
    NUM_SPINS = NUM_SPINS+1 if NUM_SPINS+1 <= MAX_SPINS else MAX_SPINS  
    SPINS_OFFSET = 360/NUM_SPINS
    FRICTION += NUM_SPINS*0.005
    resize_windows(None, None, None) 

def decrease_spinner_pins( sender, data, user ): 
    global NUM_SPINS
    global SPINS_OFFSET
    global FRICTION
    NUM_SPINS = NUM_SPINS - 1 if NUM_SPINS -1 >= MIN_SPINS  else MIN_SPINS 
    SPINS_OFFSET = 360/NUM_SPINS
    FRICTION -= NUM_SPINS*0.005
    resize_windows(None, None, None) 

with dpg.window( id = 'mainWindow', width= 800, height= 500 ): 
    with dpg.menu_bar():
        dpg.add_menu_item( label = 'Spin spinner', callback = make_spinner_spin )
        dpg.add_menu_item( label = 'Stop spinner', callback = stop_spinner )
        dpg.add_menu_item( label = 'Increase pins', callback = increase_spinner_pins )
        dpg.add_menu_item( label = 'Decrease pins', callback = decrease_spinner_pins )
        dpg.add_menu_item( label = 'Spinner color', callback = show_or_hide_color_picker )

    w, h = dpg.get_item_width('mainWindow'), dpg.get_item_height('mainWindow')
    dpg.add_color_edit( id = 'Color_picker_color', callback=change_spinner_color)
    dpg.add_color_edit( id = 'Color_picker_fill', callback=change_spinner_fill_color)
    dpg.hide_item('Color_picker_color')
    dpg.hide_item('Color_picker_fill')
    with dpg.drawlist( id='SpinnerDrawlist', width= w*0.95, height= h*0.95, pos=[w*0.025, h*0.025] ):
        for spin in range(MAX_SPINS):
            center = [w/2 + SPINS_RADIUS*math.cos( math.radians(spin*SPINS_OFFSET)) , h/2 + SPINS_RADIUS*math.sin( math.radians(spin*SPINS_OFFSET)) ]
            dpg.draw_line( id = 'SpinArm{}'.format(spin), p1=center, p2=[w/2, h/2], color=SPINS_COLOR, thickness=2*SPINS_RADIUS )
            dpg.draw_circle( id = 'Spins{}'.format(spin), center = center, radius = SPINS_RADIUS, thickness=20, segments=100, color=SPINS_COLOR, fill=SPINS_FILL )        
            if not(spin < NUM_SPINS): 
                dpg.hide_item('SpinArm{}'.format(spin))
                dpg.hide_item('Spins{}'.format(spin))
        dpg.draw_circle( id = 'centerSpinner', center = [w/2, h/2], radius = SPINS_RADIUS*5, thickness=20, segments=100, fill=SPINS_FILL, color=[200,10,50,255])

dpg.setup_viewport()
#dpg.set_viewport_large_icon( PATH + 'ico\\large_ico.ico'              )
#dpg.set_viewport_small_icon( PATH + 'ico\\small_ico.ico'              ) 
dpg.set_viewport_min_height( height = 900                             ) 
dpg.set_viewport_min_width ( width  = 1000                            ) 
dpg.set_viewport_title     ( title  = 'Finger Spinner - Kata Train'   )
dpg.maximize_viewport() 

dpg.set_primary_window( 'mainWindow', True )
dpg.add_resize_handler( 'mainWindow', callback = resize_windows )

with dpg.handler_registry() as mouse_handler:
    dpg.add_mouse_down_handler( button = dpg.mvMouseButton_Left, callback = get_force )

while dpg.is_dearpygui_running():
    w, h = dpg.get_item_width('mainWindow'), dpg.get_item_height('mainWindow')
    if ROTATING:
        if abs(VEL_ANGULAR) > 0.001:
            VEL_ANGULAR *= (math.exp(-FRICTION))
            D_TIME = dpg.get_delta_time() 
            POS_REF += math.radians( VEL_ANGULAR*D_TIME )
            for spin in range(NUM_SPINS):
                center = [w/2 + SPINS_DISTANCE*math.cos( math.radians(spin*SPINS_OFFSET) + POS_REF) , h/2 + SPINS_DISTANCE*math.sin( math.radians(spin*SPINS_OFFSET) + POS_REF) ]
                dpg.configure_item('Spins{}'.format(spin)  , center = center )        
                dpg.configure_item('SpinArm{}'.format(spin), p1     = center )
        else: 
            ROTATING = False 

    dpg.render_dearpygui_frame()
dpg.stop_dearpygui()