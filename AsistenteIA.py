import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import time
import pyautogui
import keyboard as k

#engine = pyttsx3.init()
#for voz in engine.getProperty('voices'):
#    print(voz)


JP = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'  #JAPONÉS
MX = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'  #ESPAÑOL MEXICO
EN = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'    #INGLES 


#Escuchar nuestro microfono y devolver el audio como texto
def transformarAudio():
    r = sr.Recognizer();
    with sr.Microphone() as origen:         #Configurar el microfono  
        r.pause_threshold = 0.8            #Tiempo de espera
        print("Ya puedes hablar")
        audio = r.listen(origen)            #Guardar lo que escuche como audio
        try:
            pedido = r.recognize_google(audio, language = "es-mx")      #Buscar en google lo que ha escuchado
            print("Dijiste: "+pedido)
            return pedido
        except sr.UnknownValueError:
            print("Ups, no entendí")
            return "Sigo esperando"
        except sr.RequestError:           #No se pudo transformar el audio en string
            print("Ups, no hay servicio")
            return "Sigo esperando"
        except:
            print("Ups, algo ha salido mal")
            return "Sigo esperando" 
        
        
def hablar(mensaje):
    engine = pyttsx3.init()
    engine.setProperty('voice', MX)
    engine.say(mensaje)
    engine.runAndWait()

#Informar el dia de la semana
def pedir_dia():
    dia =  datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    print(dia_semana)
    calendario = {
                    0: 'Lunes',
                    1: 'Martes',
                    2: 'Miercoles',
                    3: 'Jueves',
                    4: 'Viernes',
                    5: 'Sabado',
                    6: 'Domingo'
    }
    hablar(f'Hoy es {calendario[dia_semana]}')    

def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    hablar(hora)

def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 18:
        momento = 'Buenas noches'
    elif hora.hour > 6 or hora.hour <13:
        momento = 'Buenos dias'
    else:
        momento = 'Buenas tardes'
    hablar(f'{momento} a todos , soy Dini, su asistente personal. Por favor, dime en que te puedo ayudar')

def pedir_cosas():
    #Activar el saludo inicial
    saludo_inicial()
    
    #Variable de corte
    comenzar = True
    
    #loop central
    while comenzar:
        #Activar el micrófono y guardar el pedido en un string
        pedido = transformarAudio().lower()
        
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'abrir whatsapp' in pedido:
            hablar('Claro, estoy abriendo Whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=2)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            break
            


pedir_cosas()
pedir_dia()
pedir_hora() 