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

import RPi.GPIO as GPIO         ## GPIO 모듈 선언
import time                     ## 시간 모듈 선언    

GPIO.setmode(GPIO.BCM)          ## GPIO BCM 모드 선언 

LED_0 = 22                      ## LED 핀 번호 선언
LED_1 = 23
LED_2 = 24
LED_3 = 25

ON = 1                          ## 상수 ON을 1로 선언
OFF = 0                         ## 상수 OFF를 0으로 선언

GPIO.setup(LED_0, GPIO.OUT)     ## LED[0:3]을 출력모드로 선언
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)

try:
    while 1 :                   ## 루프 무한반복

        for i in range(4):      ## 4번 반복 (루프 한바퀴 회전하면 i는 +1 증가하며 4번 반복시 i는 0으로 초기화)
            
            if i==0:            ## i가 0일때 LED_3만 켜짐
                GPIO.output(LED_0, OFF)
                GPIO.output(LED_1, OFF)
                GPIO.output(LED_2, OFF)
                GPIO.output(LED_3, ON)                

            elif i==1:            ## i가 1일때 LED_2만 켜짐
                GPIO.output(LED_0, OFF)
                GPIO.output(LED_1, OFF)
                GPIO.output(LED_2, ON)
                GPIO.output(LED_3, OFF)


            elif i==2:            ## i가 2일때 LED_1만 켜짐        
                GPIO.output(LED_0, OFF)
                GPIO.output(LED_1, ON)
                GPIO.output(LED_2, OFF)
                GPIO.output(LED_3, OFF)

            else:            ## i가 3일때(i가 0,1,2가 아닐 때) LED_0만 켜짐
                GPIO.output(LED_0, ON)
                GPIO.output(LED_1, OFF)
                GPIO.output(LED_2, OFF)
                GPIO.output(LED_3, OFF)

            time.sleep(1)   ## 1초 동안 딜레이

except KeyboardInterrupt: ## Ctrl+c 눌렀을 떄 동작 멈춤

    GPIO.output(LED_0, OFF) ##LED_0 꺼짐
    GPIO.output(LED_1, OFF) ##LED_1 꺼짐
    GPIO.output(LED_2, OFF) ##LED_2 꺼짐
    GPIO.output(LED_3, OFF) ##LED_3 꺼짐

    GPIO.cleanup() ##GPIO 초기화
