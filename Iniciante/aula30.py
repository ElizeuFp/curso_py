"""
50. Parte 1: Variáveis, constantes e complexidade de código
51. Parte 2: Variáveis, constantes e complexidade de código

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade_do_carro = 61 # Velocidade atual do carro
Km_até_local = 90 # Local em que o carro está na estrada

RADAR = 60 # Velocidade máxima do radar
LOCAL_DE_CHEGADA = 100 # local onde o loca1 está
RANGE_DO_RADAR = 1 # A distância onde o radar pega 

velocidade_car_pass_rad_1 = velocidade_do_carro > RADAR
carro_passou_radar_1 = Km_até_local >= (LOCAL_DE_CHEGADA - RANGE_DO_RADAR) and Km_até_local <= (LOCAL_DE_CHEGADA + RANGE_DO_RADAR) and velocidade_car_pass_rad_1

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_car_pass_rad_1

if velocidade_car_pass_rad_1:
    print('Velocidade do carro passou do Radar 1')

if carro_passou_radar_1:
    print('Carro passou no Radar')

if carro_passou_radar_1 and velocidade_car_pass_rad_1:
    print(f'Carro multado em Radar 1')
    
