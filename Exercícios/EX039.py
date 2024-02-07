# EX039
campeonato = ("Real Madrid", "Girona", "Atlético Madrid", "Barcelona", "Athletic Club", "Real Sociedad", "Real Betis", "Getafe", "Valencia", "Las Palmas", "Rayo Vallecano", "Osasuna", "Villarreal", "Mallorca", "Deportivo Alavés", "Sevilla", "Celta de Vigo", "Cádiz", "Granada", "Almería")

print(f"Os primeiros 5 classificados são:{campeonato[:5]}")
print(f"Os ultimos 4 classificados são:{campeonato[-4:]}")
print(sorted(campeonato))
print(f"A posição de Las Palmas é: {campeonato.index("Las Palmas")}")
