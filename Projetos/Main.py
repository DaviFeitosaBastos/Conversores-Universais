from time import sleep
import Funcoes

def main():
    while True:
        Funcoes.main_menu()
        try:
            escolha = int(input(f"Digite uma opcao -> "))

            if escolha == 1:
                Funcoes.conversor_celsius_for_fahrenheit()
            elif escolha == 2:
                Funcoes.conversor_km_for_mile()
            elif escolha == 3:
                Funcoes.conversor_real_for_dolar()
            elif escolha == 4:
                Funcoes.conversor_minute_for_hours()
            elif escolha == 5:
                print(f"Ok saindo")
                break
        except ValueError:
            print(f"\nErro na escolha dos conversores, tente apenas numeros inteiros de 1 a 5")
main()