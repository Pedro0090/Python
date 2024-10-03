def notas(*nots, sit=False):
    """
    -> Função que pega as notas de alguns alunos e depois mostra alguns dados
    :param nots: Guarda as notas de um aluno
    :param sit: Caso queira mostrar ou não a siutação. (Opcional)
    :return: retorna o boletim(dicionário) com informações
    """
    boletim = {'total': len(nots), 'maior': max(nots), 'menor': min(nots)}
    media = sum(nots) / boletim['total']
    boletim['media'] = media
    if sit:
        if media <= 5:
            boletim['situacao'] = 'RUIM'
        elif media <= 7:
            boletim['situacao'] = 'RAZOÁVEL'
        else:
            boletim['situacao'] = 'BOA'
    return boletim


resp = notas(10, 9, 7.5, sit=True)
print(resp)
print('-' * 50)
help(notas)
