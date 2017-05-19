# coding=utf-8


def ver_pedidos(request):
    '''
    Essa view possibilita que o usuário (logado ou não) visualize os pedidos
     solicitados na plataforma.
     Provavelmente essa listagem irá representar a homepage do sistema.
    '''
    # 1. O sistema lissta os pedidos que estão solicitados e em
    # aberto (status APROVADO)

    # 2. O template da página deve ter filtros para que o usuário filtre
    # os pedidos:
    # 2.1 Filtros: por categoria de pedido, por data de inclusão,
    # por endereço da escola, por papel do solicitante (aluno/professor)
    pass


def ver_pedidos_proximos(request):
    '''
    Essa view possibilita que o usuário (logado ou não) busque por pedidos
    próximos a ele.
     Como este é um dos requisitos, pode ser interessante ter uma página
     específica que mostra os pedidos próximos ao usuário.
    Na verdade, essa view é bem similar à view "ver_pedidos", mas já com
    um filtro de localização aplicado
    '''
    # 1. O sistema lissta os pedidos que estão solicitados e em
    # aberto (status APROVADO), utilizando os dados de geolocalização para
    # filtrar os pedidos de escolas próximas (utilizando os atributos latitude
    # e longitude do model Escola)
    pass


def cadastrar_pessoa(request):
    '''
    É aqui que uma pessoa faz o cadastro no site e insere seus dados pessoais.
    Nessa tela, deve ter a opção do usuário se cadastrar como aluno ou professor.
    Se ele não escolher um desses papéis (aluno/professor), o sistema não
    cadastra um papel para ele e ele possui vínculo de voluntário.
    '''
    # 1. Usuário informa os dados pessoais e o tipo de vínculo que deseja
    # cadastrar [voluntário (default), professor ou aluno]

    # 2. Se o vínculo for de professor ou aluno, o sistema pode solicitar
    # documentos que comprovem o vínculo

    # 3. Se dados estiverem válidos, o sistema cadastra um objeto do tipo Pessoa,
    # e também os dados de login/senha do usuário. Se o usuário indicou ser
    # professor ou aluno, o sistema também cadastra um objeto do tipo Papel


def adicionar_papel(request):
    '''
    Essa view serve para adicionar um papel a um usuário já cadastrado.
    Por exemplo, no momento do cadatro, se a pessoa não selecionou um tipo de
    vínculo (aluno ou professor), ele não possui papel associado. Porém para
    ele criar algum pedido, precisa ter papel de Aluno ou Professor.
    '''
    # 1. Usuário logado indica que quer cadastrar-se como aluno ou professor

    # 2. Ele deve inserir o tipo de papel e a escola relacionada.

    # 3. O sistema pode solicitar também documentos que comprovem o vínculo.

    # 4. Se dados estiverem válidos, sistema cadastra um model do tipo Papel
    # associado com a pessoa logada.


def cadastrar_pedido(request):
    '''
    É aqui que um usuário logado cria um pedido. Se o usuário ainda não está
    logado, solicitar dados de login.
    Outro pré-requisito é que o usuário tenha um papel de Aluno ou Professor
    associado com ele. Caso não tenha, deve chamar a view adicionar_papel para
    cadastrar o papel.
    '''
    # 1. Solicitante informa os dados do pedido no template
    # 1.1 Se o usuário possui mais de um papel de Aluno/Professor (por exemplo,
    # é aluno de uma escola e professor de outra), o sistema deve pedir para ele
    # selecionar um papel apenas.

    # 2. Dados são validados

    # 3. Se dados válidos, insere pedido no banco, associado com o papel
    # previamente selecionado

    # 4. O sistema envia notificação para as pessoas que tem papel Colaborador
    # QNE, informando que um novo pedido precisa de análise

    # 5. O sistema busca todos os objetos do tipo Notificacao cuja escola
    # é a escola para qual o pedido foi feito.
    # 5.1 O sistema envia notificação para todos os usuários cadastrados
    pass


def atender_pedido(request):
    '''
    View que serve para que um usuário logado indique que deseja atender à um
    pedido. Se o usuário ainda não está logado, solicitar dados de login.
    '''
    # 1. Usuário seleciona um pedido
    # 2. Usuário informa dados relativos ao atendimento do pedido
    # 3. Se dados válido, sistema cria um objeto do tipo AtendimentoPedido
    # 4. Sistema envia notificação para solicitando, informando que um
    # voluntário deseja atender ao seu pedido
    # 5. A partir daí, o sistema habilita comunicação entre solicitante e
    # voluntário para eles acertarem os detalhes


def iniciar_pedido(request):
    '''
    Após um voluntário indicar que deseja atender a um pedido e ele e o
    solicitante acertarem os detalhes, o pedido pode ser iniciado para que o
    sistema saiba que está em andamento.
    Essa view é acessada pelo solicitanto do pedido ou pelo voluntário que
    atendeu ao pedido
    '''
    # 1. O usuário informa que o pedido foi iniciado.
    # 2. O sistema atualiza o objeto AtendimentoPedido com a data de início
    # e também atualiza o status do pedido para Em Andamento
    pass


def finalizar_pedido(request):
    '''
    View usada para indicar que um pedido foi executado e finalizado.
    Essa view é acessada pelo solicitanto do pedido ou pelo voluntário que
    atendeu ao pedido
    '''
    # 1. O usuário informa que o pedido foi finalizado.
    #  1.1 Aqui o usuário pode fazer upload de fotos ou documentos
    # que foram gerados com a execução do pedido
    # 2. O sistema atualiza o objeto AtendimentoPedido com a data de fim
    # e também atualiza o status do pedido para Finalizado
    pass


def seguir_instituicao(request):
    '''
    View utilizada para que um usuário indique que deseja receber notificações
    de pedido.
    Se o usuário ainda não está logado, solicitar dados de login.
    '''
    # 1. O usuário logado seleciona uma ou mais escola para seguir pedidos.
    # 2. O sistema cria um objeto Notificacao para cada escola selecionada,
    # associada com a pessoa logada.
    pass


def cadastrar_comentario(request):
    '''
    View utilizada para que um usuário faça comentários sobre um pedido.
    Se o usuário ainda não está logado, solicitar dados de login.
    Essa view só é habilitada se a pessoa logada estiver cadastrada como
    voluntária da atividade (vide objeto do tipo AtendimentoPedido)
    '''
    # 1. O usuário logado cadastra o comentário
    # 2. O sistema cria um objeto Comentario para o pedido selecionado,
    # associada com a pessoa logada (voluntário).
    pass


def analisar_pedido(request):
    '''
    View restrista à pessoas com papel de Colaborador QNE. Serve para
    analisar os novos pedidos cadastrados e aprovar ou reprovar.
    '''
    #  1. Colaborador QNE vai indicar se o pedido foi aceito ou não.
    #   1.1 Caso não seja aceito, deve adicionar uma justificativa

    #  2. Envia notificação para solicitante informando sobre resultado
    # da análise
    pass


def categorias_mais_populares(request):
    '''
    View que possibilita ver quais categorias de pedidos mais populares
    '''
    # 1. Para visualizar isso, o sistema deve fazer uma busca no banco de dados
    # fazendo um join entre a tabela Pedido e Categoria, fazendo uma agregaçao
    # pela Categoria.
    # Com essa busca, dá para ordenar as categorias mais solicitadas
    pass


def escolas_com_mais_demandas(request):
    '''
    View que possibilita ver quais escolas possuem mais demandas
    '''
    # 1. Para visualizar isso, o sistema deve fazer uma busca no banco de dados
    # fazendo um join entre a tabela Pedido, Papel e Escola, fazendo uma
    # agregaçao pela Escola.
    # Com essa busca, dá para ordenar as escolas com mais pedidos
    pass
