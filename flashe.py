from flet import *

def main(page:Page):
    page.window.top=5
    page.title='Hammadi Mohammed'
    page.scroll=ScrollMode.AUTO
    page.window.left=850
    page.window.width=400
    page.window.height=900
    page.bgcolor=colors.RED_300
    page.theme_mode=ThemeMode.LIGHT
    
    flashe=Flashlight()
    page.overlay.append(flashe)

    ph=PermissionHandler()
    page.overlay.append(ph)

    def open_setting(e):
        ph.open_app_settings

    page.add(
        AppBar(
            title=Text('Flash 15'),
            bgcolor='yellow',
            color='green',
            actions=[
                IconButton(icons.SETTINGS, on_click=open_setting)                
            ]            
        ),
        Row(
            [
                Text('\n\n\nFlash Light App\n\n\n', size=30, color='blue'),
                Text('\n\n\nAppF\n\n\n', size=30, color='black'),
                Image(src="logof.png"),
            ],alignment=MainAxisAlignment.CENTER            
        ),
        Row(
            [
                ElevatedButton(
                    'ON',
                    width=200,
                    icon=icons.PLAY_ARROW,
                    color=colors.GREEN_600,
                    bgcolor=colors.YELLOW_200,
                    height=50,
                    on_click=lambda _: Flashlight.turn_on
                ),
                ElevatedButton(
                    'OFF',
                    width=200,
                    icon=icons.PLAY_DISABLED_ROUNDED,
                    color=colors.RED_600,
                    bgcolor=colors.YELLOW_200,
                    height=50,
                    on_click=lambda _:Flashlight.turn_off
                ),
            ],alignment=MainAxisAlignment.CENTER
        )     ,
        Row(
            [
                Text('\n\n\n\n\n\nFlash Light App\n\n\n', size=15, color='blue'),            
            ],alignment=MainAxisAlignment.CENTER            
        ),


    )



    page.update()

app(main)
