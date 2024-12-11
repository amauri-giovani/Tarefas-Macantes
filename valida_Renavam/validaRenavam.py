#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Função para validar sequência de dígitos do Renavam.
# Adaptado por Fabricio Biazzotto, a partir do original, feito em java:
# http://blog.victorjabur.com/2010/05/28/renavam_veiculos_java


def validar_renavam(renavam):
    # Retorna falso caso o valor passado não seja um número inteiro
    if type(renavam) != int:
        return False

    # Converte renavam em string e completa com zeros à esquerda,
    # para que fique com 11 dígitos
    renavam = str(renavam).zfill(11)

    # Soma os dígitos do renavam multiplicados pelos dígitos de controle
    soma = 0  # Zera a variável soma
    controle = '3298765432'  # Valores fixos
    for i in range(10):
        algarismo = int(renavam[i])
        multiplicador = int(controle[i])
        soma += algarismo * multiplicador

    # Calcula a diferença entre 11 e o resto da divisão da soma por 11
    digito = 11 - (soma % 11)

    # Caso o digito seja maior que 9, passa a ser 0
    digito = (digito if digito < 10 else 0)

    # Compara o dígito calculado com o original
    return int(digito) == int(renavam[-1])


teste = 639884962
print('O renavam {} é {}.'.
      format(teste, 'válido' if validar_renavam(teste) else 'inválido'))
