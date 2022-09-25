import time
import usocket as socket
import os
import machine
led = machine.Pin(12, machine.Pin.OUT)

gpio_state = 'testtttttt'

def web_page():
    html = """<html><head> <title>UPDAWG</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #000000; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color:	#000000; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #808080 ;}</style></head><body> <h1>UPDAWG</h1> 
    <p><a href="/?led=on"><button class="button">WHATSUPDAWG</button></a></p>
    </body></html>"""
    #<p><a href="/?led=off"><button class="button button2">NOTHINMUCH</button></a></p>
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    while led_on == 6:
        led.value(1)
        time.sleep_ms(200)
        led.value(0)
        time.sleep_ms(200)
    response = web_page()
    conn.send(response)
    conn.close()