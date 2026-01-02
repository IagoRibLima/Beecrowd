hi, mi, hf, mf = map(int, input().split())

inicio_minutos = hi * 60 + mi
fim_minutos = hf * 60 + mf

if fim_minutos <= inicio_minutos:
    fim_minutos += 24 * 60

duracao_total_minutos = fim_minutos - inicio_minutos

duracao_horas = duracao_total_minutos // 60
duracao_minutos = duracao_total_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")