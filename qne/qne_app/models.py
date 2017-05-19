# coding=utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Pessoa(models.Model):
    '''
    Representa uma pessoa que tem cadastro no sistema.
    Pode ser colaborador, voluntário, aluno e/ou professor
    '''

    # Nome completo da pessoa
    nome = models.CharField(max_length=200)

    # E-mail da pessoa
    email = models.EmailField()

    # Data de nascimento da pessoa
    nascimento = models.DateField()

    # Data que a pessoa fez cadastro no sistema
    data_cadastro = models.DateField()

    # Usuário relacionado com a pessoa (para logar no sistema)
    # Possui as configuraçoes de usuário/senha
    user = models.OneToOneField(User)


class Cidade(models.Model):
    '''
    Representa uma cidade do país
    '''

    # Incluir dados da cidade, como nome, ISO, DDD, etc
    pass


class Estado(models.Model):
    '''
    Representa um estado do país
    '''

    # Incluir dados de estado, como nome, ISO, etc
    pass


class Escola(models.Model):
    '''
    Representa uma escola cadastrada no sistema
    '''

    # Nome da escola
    nome = models.CharField(max_length=200)

    # Endereço da escola
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade)
    estado = models.ForeignKey(Estado)

    # Dados da geolocalização
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Data de cadastro da escola no site
    data_cadastro = models.DateField()


class Papel(models.Model):
    '''
    Representa um papel que uma pessoa cadastrada tem no sistema. Uma pessoa
    pode ter mais de um papel, pois ela pode ser aluna de uma escola e
    professora de outra, por exemplo
    '''
    TIPOS_PAPEIS = (
        # A pessoa é aluna de uma determinada escola
        ('ALU', 'Aluno'),

        # A pessoa é professora de uma determinada escola
        ('PRO', 'Professor'),

        # A pessoa é colaboradora QNE.
        # Só pode configurar uma pessoa como colaboradora através da página
        # de administração do sistema
        ('COL', 'Colaborador QNE'),

    )

    # Tipo do papel
    tipo = models.CharField(max_length=3, choices=TIPOS_PAPEIS)

    # Pessoa que tá relacionada com esse papel.
    # Uma pessoa pode ter mais de um papel, mas um papel está associado
    # com apenas uma pessoa.
    # Se uma pessoa não tem papel associado, ela tem vínculo de voluntário
    pessoa = models.ForeignKey(Pessoa)

    # Escola que o papel está relacionado,
    # caso o papel for de Aluno ou Professor.
    # Este atributo fica vazio, caso o papel seja de Voluntário ou Colaborador
    escola = models.ForeignKey(Escola, blank=True)

    # Data que a pessoa cadastrou o papel
    data_cadastro = models.DateField()

    # OBS: Caso seja necessário documentos que comprovem a relação da pessoa
    #(aluno ou professor) com a escola, estes documentos devem estar nesse model



class Categoria(models.Model):
    '''
    Representa uma categoria de pedido. Devem ser cadastradas pela área
    administrativa do sistema
    '''

    # Nome da categoria
    nome = models.CharField(max_length=200)

    # Data do cadastro da categoria
    data_cadastro = models.DateField()

    # Quem cadastrou a categoria (possui papel Colaborador QNE)
    cadastrado_por = models.ForeignKey(Pessoa)


class Pedido(models.Model):
    '''
    Representa um pedido solicitado por um aluno ou professor
    '''
    STATUS_PEDIDO = (
        # Usuário (aluno ou professor) solicitou o pedido
        ('SOL', 'Solicitado (para aprovação)'),

        # Colaborador do QNE analisou o pedido e o aprovou
        ('APR', 'Aprovado'),

        # O pedido está sendo atendido por algum voluntário
        ('AND', 'Em andamento'),

        # O pedido já foi atendido e foi finalizado
        ('FIN', 'Finalizado'),

        # Colaborador do QNE analisou o pedido e não aprovou
        ('NEG', 'Negado (não aprovado)'),
    )

    # Pessoa que solicitou o pedido. Está relacionado ao model Papel e não ao
    # model Pessoa para diferenciar se o pedido é de Aluno ou Professor
    # Antes de criar o pedido, o sistema deve verificar se o usuário logado
    # (Pessoa) tem um papel de Aluno ou Professor.
    # Através do objeto Papel, dá para saber a qual escola o pedido está
    # relacionado.
    solicitante = models.ForeignKey(Papel)

    # Categoria do pedido
    categoria = models.ForeignKey(Categoria)

    # Data que o pedido foi solicitado
    data_cadastro = models.DateField()

    # Data que o pedido foi analisado (aprovado ou não)
    data_analise = models.DateField(blank=True)

    # Justificativa se o pedido não foi aprovado
    motivo_nao_aprovacao = models.CharField(max_length=256, blank=True)

    # Pessoa que analisou o pedido (pré-requisito: possui papel Colaborador QNE)
    analisado_por = models.ForeignKey(Pessoa)

    # Status atual do pedido
    status = models.CharField(max_length=3, choices=STATUS_PEDIDO)

    # Descriçao do pedido. Solicitante pode explicar as razões do pedido
    descricao = models.CharField(max_length=1024, blank=True)

    # Informações adicionais. Solicitante pode adicionar informações adicionais,
    # como horário ou turno desejado, dias da semana, faixa etária dos alunos,
    # etc
    outras_informacoes = models.CharField(max_length=1024, blank=True)


class AtendimentoPedido(models.Model):
    '''
    Model criado quando um voluntário se oferece para atender um pedido
    '''

    # Pedido que está sendo solicitado
    pedido = models.ForeignKey(Pedido)

    # Pessoa (voluntário) que está se oferecendo para atender o pedido
    voluntario = models.ForeignKey(Pessoa)

    # Horários que o voluntario pode fazer a atividade
    horario = models.CharField(max_length=256)

    # Quantidade de visitas que o voluntario pode fazer para atender ao pedido
    qtd_visitas = models.IntegerField()

    # Informações adicionais que o voluntário pode colocar para o solicitante
    informacoes_extras = models.CharField(max_length=1024, blank=True)

    # Data de início da execução (qundo foi iniciado de fato)
    data_inicio = models.DateTimeField(blank=True)

    # Data de finalização da execução, quando ela for finalizada
    data_fim = models.DateTimeField(blank=True)

    # Nesse model também podem ter fotos, anexos e outros documentos
    # relacionados com a execução do pedido


class Notificacao(models.Model):
    '''
    Model que informa quem deseja receber notificações de pedidos
    de uma determinada escola.
    '''
    # Pessoa que quer receber notificação de pedidos
    # Uma pessoa pode ter mais de um objeto Notificacao associado (ou seja,
    # receber notificação de mais de uma escola)
    pessoa = models.ForeignKey(Pessoa)

    # Escola que a pessoa quer receber notificação
    escola = models.ForeignKey(Escola)


class Comentario(models.Model):
    '''
    Model que representa um comentário feito a algum pedido
    '''
    # Pessoa que fez o comentário
    # Possui papel Voluntário
    pessoa = models.ForeignKey(Pessoa)

    # Pedido alvo do comentário
    pedido = models.ForeignKey(Pedido)

    # Data de cadastro do comentário
    data_cadastro = models.DateTimeField(blank=True)
