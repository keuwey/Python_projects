def converter_tempo(tempo: int, unidade_origem: str, unidade_destino: str) -> int:
    """Converte uma unidade de tempo para outra."""
    # Converte as unidades de tempo para segundos
    if unidade_origem == 'horas':
        tempo_em_segundos = tempo * 3600
    elif unidade_origem == 'minutos':
        tempo_em_segundos = tempo * 60
    elif unidade_origem == 'segundos':
        tempo_em_segundos = tempo
    else:
        raise ValueError(f"Unidade de tempo inválida: {unidade_origem}")
    
    # Converte os segundos para a unidade de destino
    if unidade_destino == 'horas':
        tempo_convertido = tempo_em_segundos / 3600
    elif unidade_destino == 'minutos':
        tempo_convertido = tempo_em_segundos / 60
    elif unidade_destino == 'segundos':
        tempo_convertido = tempo_em_segundos
    else:
        raise ValueError(f"Unidade de tempo inválida: {unidade_destino}")
    
    return int(tempo_convertido)

# Exemplo: converte 2 horas para minutos
horas = 2
minutos = converter_tempo(horas, 'horas', 'minutos')
print(minutos)  # Imprime 120

# Exemplo: converte 90 minutos para segundos
minutos = 90
segundos = converter_tempo(minutos, 'minutos', 'segundos')
print(segundos)  # Imprime 5400

# Exemplo: converte 10 segundos para minutos
segundos = 10
minutos = converter_tempo(segundos, 'segundos', 'minutos')
print(minutos) # Imprime 0