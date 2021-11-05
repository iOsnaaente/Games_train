from dearpygui.dearpygui import * 
import datetime as dt 
import winsound 
import time 
import math 
import sys

get_item_size = lambda id   : [ get_item_width( id )  , get_item_height( id )  ]
get_item_middle = lambda id : [ get_item_width( id )/2, get_item_height( id)/2 ]


setup_viewport ( )
set_viewport_min_height( height = 700                ) 
set_viewport_min_width ( width  = 800                ) 
set_viewport_title     ( title  = "O'Clock relógio"  )

with window( id = 1_0 ) as main_window: 
    pass 

set_primary_window( main_window, True )
maximize_viewport()


w, h = get_item_size( 1_0 )
with window( id = 2_0, pos = [10,10], width = w*0.65, height = h*0.98, no_title_bar = True, no_close = True, no_resize = True ) as clock_window:
    w, h = get_item_size(2_0)
    add_drawlist( id = 2_1_0, pos = [20,20], width = w*0.9, height = h*0.98 )
    center = get_item_middle( 2_1_0)
    draw_circle(parent = 2_1_0, id = 2_1_1, center = center, radius = 350, color = [0,0,0,200]      , thickness= 3, fill= [100,100,100,200])
    draw_arrow( parent = 2_1_0, id = 2_1_2, p1=[ 0,0 ]     , p2= center  , color = [255,60,50,200], size= 15, thickness= 5 )
    draw_arrow( parent = 2_1_0, id = 2_1_3, p1=[ 0,0 ]     , p2= center  , color = [50,200,10,210], size= 15, thickness= 5 )
    draw_arrow( parent = 2_1_0, id = 2_1_4, p1=[ 0,0 ]     , p2= center  , color = [50,50,255,200], size= 15, thickness= 5 )

with window( id = 3_0, pos = [10 + w*0.65,10], width = w*0.45, height = h*0.98, no_title_bar = True, no_close = True, no_resize = True  ) as config_window:
    pass


time_now : int = 0 
minutos  : int = 0 
segundos : int = 0 
horas    : int = 0
goal     : list = [0,0,10] 


while is_dearpygui_running():
    render_dearpygui_frame() 

    color_time = time.time() 

    if time.time() - time_now > 1:
        time_now = time.time()
        segundos += 1 
        if segundos > 60:
            minutos += 1 
            segundos = 0 
            if minutos > 60:
                horas += 1 
                minutos = 0
                if horas > 12: 
                    horas = 0 

        pointer_Seg_pos = [ math.cos( math.radians(segundos*6 -90)) , math.sin(math.radians(segundos*6 -90)) ]
        pointer_Min_pos = [ math.cos( math.radians(minutos*6  -90)) , math.sin(math.radians(minutos*6  -90)) ]
        pointer_Hor_pos = [ math.cos( math.radians(horas*30   -90)) , math.sin(math.radians(horas*30   -90)) ]
            

    size =  get_item_size(1_0)
    configure_item( 2_0 , width = size[0]*0.65  , height = size[1]*0.98 )
    configure_item( 3_0 , pos = [15 + size[0]*0.65, 10], width  = size[0]*0.35-20, height = size[1]*0.98 )

    size =  get_item_size(2_0)
    configure_item( 2_1_0, width = size[0]*0.95, height = size[1]*0.95 )

    center   = get_item_middle(2_1_0)
    raio_seg = min(center)
    raio_min = min(center)
    raio_hor = min(center)*0.75

    configure_item( 2_1_1, center = center, radius = min(center) )
    configure_item( 2_1_2, p1 = [ pointer_Seg_pos[0]*raio_seg + center[0], pointer_Seg_pos[1]*raio_seg + center[1]], p2 = center )
    configure_item( 2_1_3, p1 = [ pointer_Min_pos[0]*raio_min + center[0], pointer_Min_pos[1]*raio_min + center[1]], p2 = center )
    configure_item( 2_1_4, p1 = [ pointer_Hor_pos[0]*raio_hor + center[0], pointer_Hor_pos[1]*raio_hor + center[1]], p2 = center )
        
    

    if horas == goal[0] and minutos == goal[1] and segundos == goal[2]:
        for i in range(2): 
            winsound.Beep( 370, 1000)
            time.sleep(0.5)
        sys.exit(0)