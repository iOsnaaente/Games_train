from dearpygui.simple import * 
from dearpygui.core import * 

import winsound
import time 
import math 
import sys


time_now = time.time() 

segundos = 0 
minutos  = 0
horas    = 0

names = ['Horas', 'Minutos', 'Segundos']
goal = [ 0, 0, 0 ]


for i in range(3):
    goal.append( int( input('Digite o número de %s de estudo: ' %names[i] ) ) )


pointer_Seg_pos = [ math.cos( math.pi/2), math.sin(math.pi/2)]
pointer_Min_pos = [ math.cos( math.pi/2), math.sin(math.pi/2)]
pointer_Seg_pos = [ math.cos( math.pi/2), math.sin(math.pi/2)]

def render(sender, data): 

    global time_now
    global minutos, segundos, horas
    global goal 

    raio_seg = 350
    raio_min = 350
    raio_hor = 200 
    
    center =  get_main_window_size() 

    configure_item( 'theClock', width = center[0], height = center[1] )

    center = [ round(val/2) for val in center ]

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
            
        modify_draw_command('theClock', 'Clock', center = center )
        modify_draw_command('theClock', 'pointerSeg', p1 = [ pointer_Seg_pos[0]*raio_seg + center[0], pointer_Seg_pos[1]*raio_seg + center[1]], p2 = center ,color = [255,60,50,200]   )
        modify_draw_command('theClock', 'pointerMin', p1 = [ pointer_Min_pos[0]*raio_min + center[0], pointer_Min_pos[1]*raio_min + center[1]], p2 = center ,color = [50,200,10,210] )
        modify_draw_command('theClock', 'pointerHor', p1 = [ pointer_Hor_pos[0]*raio_hor + center[0], pointer_Hor_pos[1]*raio_hor + center[1]], p2 = center ,color = [50,50,255,200] )
        

    if horas == goal[0] and minutos == goal[1] and segundos == goal[2]:
        for i in range(10): 
            winsound.Beep(i*1000, 1000)
            time.sleep(0.5)
        sys.exit(0)


with window('ClockisOnTheTable', width= 800, height= 800 ):
    center = [800/2, 800/2]

    add_drawing('theClock', width= 800, height= 800)
    draw_circle('theClock', center, 350, color= [0,0,0,200], thickness= 3, fill= [100,100,100,200], tag= 'Clock')
    draw_arrow('theClock', p1=[ 0,0 ], p2= center, color= [0,0,0,0], tag= 'pointerSeg', size= 15, thickness= 5 )
    draw_arrow('theClock', p1=[ 0,0 ], p2= center, color= [0,0,0,0], tag= 'pointerMin', size= 15, thickness= 5 )
    draw_arrow('theClock', p1=[ 0,0 ], p2= center, color= [0,0,0,0], tag= 'pointerHor', size= 15, thickness= 5 )


set_render_callback( render )
set_theme('Gray')
start_dearpygui(primary_window= 'ClockisOnTheTable') 