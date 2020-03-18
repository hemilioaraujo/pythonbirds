'''
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.direcao
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.direcao
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.direcao
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.direcao
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.direcao
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.direcao
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.direcao
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.direcao
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.direcao
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.velocidade()
    0
    >>> carro.acelerar()
    >>> carro.velocidade()
    1
    >>> carro.acelerar()
    >>> carro.velocidade()
    2
    >>> carro.frear()
    >>> carro.velocidade()
    0
    >>> carro.sentido
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.sentido
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.sentido
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.sentido
    'Oeste'
'''

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        elif self.velocidade == 1:
            self.velocidade -= 1
        else:
            ...

class Direcao:
    olhos = 1
    direcao_direita = {
        'Norte': 'Leste',
        'Leste': 'Sul',
        'Sul': 'Oeste',
        'Oeste': 'Norte'
    }

    direcao_esquerda = {
        'Norte': 'Oeste',
        'Leste': 'Norte',
        'Sul': 'Leste',
        'Oeste': 'Sul'
    }

    def __init__(self, direcao='Norte'):
        self.direcao = direcao

    def girar_a_esquerda(self):
        self.direcao = self.direcao_esquerda[self.direcao]

    def girar_a_direita(self):
        self.direcao = self.direcao_direita[self.direcao]

class Carro:
    def __init__(self, direcao=Direcao(), motor=Motor()):
        self.motor = motor
        self.direcao = direcao
        self.sentido = direcao.direcao

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
        self.sentido = self.direcao.direcao

    def girar_a_direita(self):
        self.direcao.girar_a_direita()
        self.sentido = self.direcao.direcao

    def acelerar(self):
    	self.motor.acelerar()

    def frear(self):
    	self.motor.frear()

    def velocidade(self):
    	return self.motor.velocidade


if __name__ == "__main__":
    a = Carro()
    print(a.sentido)
    a.girar_a_esquerda()
    print(a.sentido)
    a.girar_a_esquerda()
    print(a.sentido)
    a.girar_a_esquerda()
    print(a.sentido)
    a.girar_a_esquerda()
    print(a.sentido)
    print('########################')
    print(a.sentido)
    a.girar_a_direita()
    print(a.sentido)
    a.girar_a_direita()
    print(a.sentido)
    a.girar_a_direita()
    print(a.sentido)
    a.girar_a_direita()
    print(a.sentido)
    print('########################')
    a.velocidade()
    a.acelerar()
    a.velocidade()
    a.acelerar()
    a.velocidade()
    a.frear()
    a.velocidade()
    a.frear()
    a.velocidade()
    a.frear()
    a.velocidade()