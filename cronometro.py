from time import sleep
import flet as ft
from datetime import timedelta

def main(page: ft.Page):
    page.title = 'Cronômetro'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    tempo = ft.Text(timedelta(seconds=0), size=36)  
    page.window_width = 300
    page.window_height = 300


    
    def iniciar(e):
        page.contando = True
        while page.contando:
            tempo.value = timedelta(seconds=int(tempo.value.seconds) + 1)
            page.update()
            sleep(1)
           
    def reset(e):
        page.contando = False
        tempo.value = timedelta(seconds=0)
        page.update()

    def pause(e):
        page.contando = False      

    page.add(
        ft.Container(
            ft.Column(
            [
                
                tempo,
                ft.FilledButton('iniciar',icon='play_arrow', on_click=iniciar),
                ft.FilledButton('pausar', icon='pause', on_click=pause),
                ft.FilledButton('resetar', icon='stop', on_click=reset),
                
            ], horizontal_alignment=ft.MainAxisAlignment.CENTER
        ),alignment=ft.alignment.center
        )
        
    )

ft.app(target=main)
    
    
    
    




