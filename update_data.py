import os
import json
from datetime import datetime

def generate_quant_data():
    print(f"Iniciando Kernel Cuantitativo KHIPU PRO - {datetime.now()}")
    
    league_data = {
        "teams": [
            {"name": "Argentina", "logo": "https://media.api-sports.io/football/teams/26.png"},
            {"name": "Francia", "logo": "https://media.api-sports.io/football/teams/17.png"},
            {"name": "Brasil", "logo": "https://media.api-sports.io/football/teams/6.png"},
            {"name": "Inglaterra", "logo": "https://media.api-sports.io/football/teams/10.png"},
            {"name": "España", "logo": "https://media.api-sports.io/football/teams/9.png"},
            {"name": "Alemania", "logo": "https://media.api-sports.io/football/teams/25.png"},
            {"name": "Portugal", "logo": "https://media.api-sports.io/football/teams/27.png"},
            {"name": "Uruguay", "logo": "https://media.api-sports.io/football/teams/7.png"},
            {"name": "Colombia", "logo": "https://media.api-sports.io/football/teams/8.png"},
            {"name": "México", "logo": "https://media.api-sports.io/football/teams/16.png"},
            {"name": "Estados Unidos", "logo": "https://media.api-sports.io/football/teams/24.png"},
            {"name": "Perú", "logo": "https://media.api-sports.io/football/teams/30.png"}
        ]
    }

    referees_data = {
        "Szymon Marciniak": {"fouls_per_game": 22.5, "yellows_per_game": 4.1, "reds_per_game": 0.2},
        "Daniele Orsato": {"fouls_per_game": 24.1, "yellows_per_game": 5.2, "reds_per_game": 0.3},
        "Wilton Sampaio": {"fouls_per_game": 28.5, "yellows_per_game": 6.1, "reds_per_game": 0.4}
    }

    os.makedirs('ARCHIVOS JSON/MUNDIAL 2026', exist_ok=True)

    with open('ARCHIVOS JSON/MUNDIAL 2026/league.json', 'w', encoding='utf-8') as f:
        json.dump(league_data, f, indent=4)
        
    with open('ARCHIVOS JSON/MUNDIAL 2026/referees.json', 'w', encoding='utf-8') as f:
        json.dump(referees_data, f, indent=4)
        
    print("✓ Pipeline ejecutado con éxito.")

if __name__ == "__main__":
    generate_quant_data()
