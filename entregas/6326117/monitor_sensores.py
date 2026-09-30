leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]

def monitorar(lista):
    acumulador = 0.0
    contador = 0
    for leitura in lista:
        if leitura > 80.0:
            print(f"[DESCARTE] Leitura de {leitura}C fora da faixa, ignorada.")
            continue
        elif leitura == -999.0:
            print(f"[FALHA] Sensor corrompido com leitura de {leitura}C. Interrompendo monitoramento.")
            break
        else:
            print(f"[OK] Leitura de {leitura}C registrada.")
            acumulador += leitura
            contador += 1
    else:
        if contador > 0:
            media = acumulador / contador
            print(f"Quantidade de leituras validas: {contador}")
            print(f"Media das leituras validas: {media:.2f}C")
        else:
            print("Nenhuma leitura valida registrada.")



if __name__ == "__main__":
    monitorar(leituras)