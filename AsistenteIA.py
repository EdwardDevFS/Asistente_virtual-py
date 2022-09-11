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

class Asistente:
    def __init__(self):
        self.JP = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'  #JAPONÉS
        self.MX = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'  #ESPAÑOL MEXICO
        self.EN = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'    #INGLES 

        #Escuchar nuestro microfono y devolver el audio como texto
    def transformarAudio(self):
        self.r = sr.Recognizer();
        with sr.Microphone() as self.origen:         #Configurar el microfono  
            self.r.pause_threshold = 1            #Tiempo de espera
            self.audio = self.r.listen(self.origen)            #Guardar lo que escuche como audio
            
            try:
                self.pedido = self.r.recognize_google(self.audio, language = "es-mx")      #Buscar en google lo que ha escuchado
                return self.pedido
            except sr.UnknownValueError:
                self.mensaje = "Ups, no entendí"
                self.hablar(self.mensaje)
                return "Sigo esperando"
                
            except sr.RequestError:           #No se pudo transformar el audio en string
                print("Ups, no hay servicio")
                return "Sigo esperando"
            except ValueError:
                print("No es el valor que espero")
            except:
                print("Ups, algo ha salido mal")
                return "Sigo esperando" 
            
    def hablar(self, mensaje):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.MX)
        self.engine.say(self.mensaje)
        self.engine.runAndWait()

    #Informar el dia de la semana

    def pedir_dia(self):
        self.dia =  datetime.date.today()
        print(self.dia)
        self.dia_semana = self.dia.weekday()
        print(self.dia_semana)
        self.calendario = {
                        0: 'Lunes',
                        1: 'Martes',
                        2: 'Miercoles',
                        3: 'Jueves',
                        4: 'Viernes',
                        5: 'Sabado',
                        6: 'Domingo'
        }
        self.mensaje = f'Hoy es {self.calendario[self.dia_semana]}'
        self.hablar(self.mensaje)    

    def pedir_hora(self):
        self.hora = datetime.datetime.now()
        self.mensaje = f'En este momento son las {self.hora.hour} horas con {self.hora.minute} minutos.'
        self.hablar(self.mensaje)

    def saludo_inicial(self):
        self.hora = datetime.datetime.now()
        if self.hora.hour > 17 and self.hora.minute < 59:
            self.momento = 'Buenas noches'
        elif self.hora.hour < 12:
            self.momento = 'Buenos dias'
        else:
            self.momento = 'Buenas tardes'
        self.mensaje = f'{self.momento} a todos , soy Dini, su asistente personal. Por favor, dime en que te puedo ayudar'
        self.hablar(self.mensaje)

    # CALCULADORA
    def calculadora(self):
        self.mensaje = '¿Qué operación desea hacer?' 
        self.hablar(self.mensaje)
        self.op = self.transformarAudio().lower()
        #SUMAR NUMEROS
        if 'suma' in self.op:
            self.mensaje = 'Que numeros quiere sumar'
            self.hablar(self.mensaje)
            num = self.transformarAudio()
            num = num.replace("y",",")
            num = num.replace(":",",")
            separador=(",")
            num = num.split(separador)
            sum = int(num[0]) + int(num[1])
            self.mensaje = 'El resultado de la suma de {} y {} es {}'.format(num[0],num[1],str(sum))
            self.hablar(self.mensaje)
            self.mensaje = '¿Desea hacer otra operación?' 
            self.hablar(self.mensaje)
            self.confirmar = self.transformarAudio().lower()
            if 'sí' or 'si' in self.confirmar:
                self.calculadora()
                return 
            else:
                self.mensaje = "Okey, Que tengas un buen día!"
                self.hablar(self.mensaje)
                quit()
    #RESTA NUMEROS    
        elif 'resta' in self.op:
            self.mensaje = 'Que numeros quiere restar'
            self.hablar(self.mensaje)
            num = self.transformarAudio()
            num = num.replace("y",",")
            num = num.replace(":",",")
            separador=(",")
            num = num.split(separador)
            res = int(num[0]) - int(num[1])
            self.mensaje = 'El resultado de la resta de {} y {} es {}'.format(num[0],num[1],str(res))
            self.hablar(self.mensaje)
                
    #MULTIPLICAR NUMEROS
        elif 'multiplicación' in self.op or 'multiplicar' in self.op:
            self.mensaje = 'Que numeros quiere multiplicar'
            self.hablar(self.mensaje)
            num = self.transformarAudio()
            num = num.replace("y",",")
            num = num.replace(":",",")
            separador=(",")
            num = num.split(separador)
            mul = int(num[0]) * int(num[1])
            self.mensaje = 'El resultado de la multiplicacion de {} y {} es {}'.format(num[0],num[1],str(mul))
            self.hablar(self.mensaje)
                
    #DIVIDIR NUMEROS
        elif 'dividir' in self.op:
            self.mensaje = 'Que numeros quiere dividir'
            self.hablar(self.mensaje)
            num = self.transformarAudio()
            num = num.replace("y",",")
            num = num.replace(":",",")
            separador=(",")
            num = num.split(separador)
            div = int(num[0]) / int(num[1])
            self.mensaje = 'El resultado de la division de {} y {} es {}'.format(num[0],num[1],str(div))
            self.hablar(self.mensaje)
        else:
            self.mensaje = 'Parece que no te entendí, vamos otra vez.'
            self.hablar(self.mensaje)
            self.calculadora()

    def prueba():
        asistente.pedir_cosas()
    def pedir_cosas(self):
        self.saludo_inicial()    #Activar el saludo inicial
        self.comenzar = True     #Variable de corte
        
        #loop central
        while self.comenzar:
            #Activar el micrófono y guardar el pedido en un string
            self.pedido = self.transformarAudio().lower()
            if 'abrir youtube' in self.pedido:
                self.mensaje = 'Con gusto, estoy abriendo Youtube'
                self.hablar(self.mensaje)
                webbrowser.open('https://www.youtube.com/')
                continue
            elif 'abrir el navegador' in self.pedido:
                self.mensaje = 'Claro, estoy en eso'
                self.hablar(self.mensaje)
                webbrowser.open('https://www.google.com/')
                continue
            elif 'qué día es hoy' in self.pedido:
                self.pedir_dia()
                continue
            elif 'qué hora es' in self.pedido:
                self.pedir_hora()
                continue
            elif 'abrir whatsapp' in self.pedido:
                self.mensaje='Claro, estoy abriendo Whatsapp'
                self.hablar(self.mensaje)
                webbrowser.open('https://web.whatsapp.com/')
                continue
            elif 'busca en wikipedia' in self.pedido:
                self.mensaje = "Buscando eso en wikipedia"
                self.hablar(self.mensaje)
                self.pedido = self.pedido.replace('busca en wikipedia','')
                wikipedia.set_lang('es')
                self.resultado = wikipedia.summary(self.pedido, sentences=2)
                self.mensaje = f'Wikipedia dice lo siguiente: {self.resultado}'
                self.hablar(self.mensaje)
                continue
            elif 'busca en internet' in self.pedido:
                self.mensaje = 'Ya mismo estoy en eso'
                self.hablar(self.mensaje)
                self.pedido = self.pedido.replace('busca en internet','')
                pywhatkit.search(self.pedido)
                self.mensaje = 'Esto es lo que he encontrado'
                self.hablar(self.mensaje)
                continue
            elif 'reproduce' in self.pedido:
                self.mensaje = 'Buena idea, ya comienzo a reproducirlo'
                self.hablar(self.mensaje)
                pywhatkit.playonyt(self.pedido)
                continue
            elif 'broma' or 'chiste' in self.pedido:
                self.mensaje = pyjokes.get_joke('es')
                self.hablar(self.mensaje)
                break
            elif 'operar' or 'operacion' or 'operación' in self.pedido:
                self.calculadora()
                continue
                

asistente = Asistente()

