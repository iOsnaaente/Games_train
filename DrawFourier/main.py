import dearpygui.dearpygui as dpg 
import matplotlib.pyplot as plt 
import numpy as np 
import math 

dpg.create_context()
dpg.create_viewport( title = 'FFT draw DPG Fourier', min_width = 800, min_height = 600 )
dpg.setup_dearpygui()

with dpg.value_registry( id = 'valueRegistry' ):
    x_mouse_drag = dpg.add_int_value( parent = 'valueRegistry', default_value = 0, tag = dpg.generate_uuid()  )
    y_mouse_drag = dpg.add_int_value( parent = 'valueRegistry', default_value = 0, tag = dpg.generate_uuid()  )
    center_x  = dpg.add_int_value( parent = 'valueRegistry', default_value = 0, tag = dpg.generate_uuid() ) 
    center_y  = dpg.add_int_value( parent = 'valueRegistry', default_value = 0, tag = dpg.generate_uuid() ) 
    d_time    = dpg.add_float_value( parent = 'valueRegistry', default_value = 0, tag = dpg.generate_uuid() ) 
    frequency = dpg.add_float_value( parent = 'valueRegistry', default_value = 0, tag = dpg.generate_uuid() ) 

def resize( sender, data, user ):
    dpg.configure_item( 'drawListFourier', width = data[2]-15, height = data[3]*0.98 - 155 )
    dpg.configure_item( 'magicButton', width = data[2]-15 )
    dpg.set_value( center_x, (data[2]-15      )/2 )
    dpg.set_value( center_y, (data[3]*0.98-155)/2 )


drag_draw_pos = [ ]
def drawFourierLine( sender, data, user ) :
    global drag_draw_pos
    data   = dpg.get_mouse_pos( )
    if dpg.get_value(x_mouse_drag) != data[0] and dpg.get_value(y_mouse_drag) != data[1]:
        dpg.set_value( x_mouse_drag, value = data[0] )
        dpg.set_value( y_mouse_drag, value = data[1] )
        drag_draw_pos.append( data )
        dpg.configure_item( 'polyline', points = drag_draw_pos )
        dpg.set_value( d_time, data[1] )


def realeaseDragMouse(sender, data, user ):
    global drag_draw_pos
    N = len( drag_draw_pos )

    dpg.set_value( frequency, 2*math.pi / dpg.get_value( d_time ) ) 
    dpg.set_value( d_time   , 0 ) 

    center     = [ dpg.get_value(center_x), dpg.get_value(center_y) ]
    drag_draw_pos   = [ [data[n] - center[n] for n in range(2)] for data in drag_draw_pos ]
    drag_draw_pos = np.fft.fft2( drag_draw_pos )*2/N

    plt.plot( drag_draw_pos )
    plt.show()

    drag_draw_pos = []  


def make_the_magic_happen( sender, data, user ):
    print( sender, data, user ) 


with dpg.window( tag = 'mainWindow', autosize = True, no_close = True, no_move = True, no_resize = True ): 
    with dpg.drawlist( tag = 'drawListFourier', width = 0, height = 0, pos = [0, 0] ):
        dpg.draw_polyline( parent = 'drawListFourier', tag = 'polyline', closed = False, points = [] )  

    dpg.add_button( parent = 'mainWindow', tag = 'magicButton', label = 'Make the magic happen', width = 1200, height = 150, callback = make_the_magic_happen )

dpg.set_primary_window( 'mainWindow', True )
dpg.set_viewport_resize_callback( resize )

with dpg.handler_registry( id = 'handlerRegistry'): 
    dpg.add_mouse_down_handler( parent = 'handlerRegistry', button = dpg.mvMouseButton_Right, callback = drawFourierLine )
    dpg.add_mouse_release_handler( parent = 'handlerRegistry', button = dpg.mvMouseButton_Right, callback = realeaseDragMouse )


dpg.maximize_viewport() 

dpg.show_viewport()
while dpg.is_dearpygui_running(): 
    dpg.render_dearpygui_frame() 



dpg.stop_dearpygui() 
dpg.destroy_context() 