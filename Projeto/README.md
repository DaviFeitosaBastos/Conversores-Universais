# 🔄 Conversor Universal em Python

Bem-vindo ao **Conversor Universal**, um projeto simples em Python que realiza conversões de unidades diretamente pelo terminal. Com uma interface interativa e suporte ao formato brasileiro de moeda, você pode converter:

- 🌡️ Temperatura: Celsius → Fahrenheit  
- 🚗 Velocidade: Km/h → Mph  
- 💰 Moeda: Reais (R$) → Dólares (USD)  
- ⏱️ Tempo: Minutos → Horas  

---

## 📌 Funcionalidades

✔️ Conversão de unidades com entrada do usuário  
✔️ Repetição automática com prompt de "Deseja converter outro valor?"  
✔️ Formatação de valores em reais com `locale`  
✔️ Compatível com Windows, macOS e Linux  

---

## ▶️ Como executar

> Requisitos: Python 3.13.5 instalado
> Requisitos: pip install request (Caso não tenha!)

1. Clone este repositório:
```bash
git clone https://github.com/DaviFeitosaBastos/Conversores-Universais.git
cd Conversores-Universais
```
## Estrutura do Projeto
conversor.py           # Código principal com os 4 conversores
README.md              # Instruções e documentação do projeto

## Observação sobre o locale

O projeto utiliza o módulo locale para formatar corretamente valores em reais:

🐧 Linux/macOS: 'pt_BR.UTF-8'

🪟 Windows: 'Portuguese_Brazil.1252'


## 💱 Taxa de câmbio

real / 5.4759           # Fique a vontade para alterar para o ptax manualmente, 

## 👨‍💻 Autor
Davi Feitosa Bastos (Dave)
