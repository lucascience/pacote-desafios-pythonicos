"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
from math import ceil


def front_back(a, b):
    #a_frente = a[:ceil(len(a) / 2)]
    #a_tras = a[len(a_frente):]
    #b_frente = b[:ceil(len(b) / 2)]
    #b_tras = b[len(b_frente):]
    #s = [a_frente, b_frente, a_tras, b_tras]
    #return ''.join(s)

    def separa(s):
        m = ceil(len(s) / 2)
        return (s[:m], s[m:])

    def fb(s1,s2):
        return s1[0], s2[0], s1[1], s2[1]

    return ''.join(fb(separa(a), separa(b)))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
