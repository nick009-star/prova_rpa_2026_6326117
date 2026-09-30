ENDPOINT_URL = "http://localhost"
PORTA = 8080
TAXA_AMOSTRAGEM = 0.5
USA_HTTPS = False


def main():
    parametros = {
        "ENDPOINT_URL": ENDPOINT_URL,
        "PORTA": PORTA,
        "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
        "USA_HTTPS": USA_HTTPS
    }

    for i in parametros:
        print(f"{i}: {parametros[i]} (tipo: {type(parametros[i])})")


if __name__ == "__main__":
    main()
