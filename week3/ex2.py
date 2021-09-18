############################################
#                                          #
#               Coding Kit                 #
#                                          #
# (c) Copyright Sisodream Inc.             #
# All Rights Reserved.                     #
#                                          #
# www.codingkit.net / www.sisodream.com    #
# ck@sisodream.com                         #
#                                          #
############################################

import RPi.GPIO as GPIO        ## GPIO 모듈 선언
GPIO.setmode(GPIO.BCM)         ## GPIO BCM 모드 선언

LED_0 = 22                     ## LED[0:3] 핀 번호 선언
LED_1 = 23  
LED_2 = 24  
LED_3 = 25

BUTTON_0 = 4                   ## BUTTON [0:3] 핀 번호 선언
BUTTON_1 = 5
BUTTON_2 = 6
BUTTON_3 = 16

ON = 1                         ## 상수 ON을 1로 선언
OFF = 0                        ## 상수 OFF를 0으로 선언

 ## BUTTON이 눌리는 경우 0이 출력되고 누르지 않은 경우 1로 출력되어 LED가 항상 켜져있어 원하는 동작을 구현하기 위해 inverter 함수 사용
def inverter(input_gpio):      ## GPIO.input으로 나온 출력이 0인 경우 1로 바꾸고 1인 경우 0으로 바꿈
    if input_gpio == 1:       
        return 0

    else:
        return 1


GPIO.setup(LED_0, GPIO.OUT)    ## LED[0:3] 출력모드 선언
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)

GPIO.setup(BUTTON_0, GPIO.IN)  ## BUTTON [0:3] 입력모드 선언
GPIO.setup(BUTTON_1, GPIO.IN)
GPIO.setup(BUTTON_2, GPIO.IN)
GPIO.setup(BUTTON_3, GPIO.IN)

try:

    while 1 :                   ## 루프 무한반복
        GPIO.output(LED_0, inverter(GPIO.input(BUTTON_0)))  ##BUTTON_0이 눌릴 떄 LED_0이 켜짐
        GPIO.output(LED_1, inverter(GPIO.input(BUTTON_1)))  ##BUTTON_1이 눌릴 떄 LED_1이 켜짐
        GPIO.output(LED_2, inverter(GPIO.input(BUTTON_2)))  ##BUTTON_2이 눌릴 떄 LED_2이 켜짐
        GPIO.output(LED_3, inverter(GPIO.input(BUTTON_3)))  ##BUTTON_3이 눌릴 떄 LED_3이 켜짐

except KeyboardInterrupt:  ## Ctrl+c 눌렀을 떄 동작 멈춤

    GPIO.output(LED_0, OFF) ##LED_0 꺼짐
    GPIO.output(LED_1, OFF) ##LED_1 꺼짐
    GPIO.output(LED_2, OFF) ##LED_2 꺼짐
    GPIO.output(LED_3, OFF) ##LED_3 꺼짐

    GPIO.cleanup() ##GPIO 초기화

    
