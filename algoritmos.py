"""
==========================================================
  Pratica: Algoritmos
==========================================================
  Aluno:        Levi Cury
  Instituicao:  Faculdade de Tecnologia Rocketseat
  Disciplina:   Logica de Programacao
  Atividade:    Exercicios praticos - Algoritmos
                (Descricao Narrativa, Fluxograma e
                 Pseudocodigo)
  Data:         Fevereiro/2026
==========================================================
"""


# ============================================================
#  PARTE 1 - DESCRICAO NARRATIVA
# ============================================================

descricoes_narrativas = {
    1: {
        "titulo": "Fazer um cafe coado",
        "passos": [
            "Pegue uma chaleira e encha com 500ml de agua",
            "Coloque a chaleira no fogao e ligue o fogo",
            "Enquanto a agua aquece, pegue o suporte para filtro de papel",
            "Coloque um filtro de papel limpo no suporte",
            "Adicione 3 colheres de sopa de po de cafe dentro do filtro",
            "Pegue uma garrafa termica ou caneca e posicione o suporte sobre ela",
            "Quando a agua comecar a ferver, desligue o fogo com cuidado",
            "Despeje um pouco da agua quente sobre o po para umedecer",
            "Continue despejando lentamente o resto da agua sobre o cafe",
            "Aguarde toda a agua passar pelo po e terminar de coar",
            "Retire o suporte com o filtro e descarte o po",
            "Tampe a garrafa ou sirva na caneca",
            "Adicione acucar ou adocante, se desejar",
            "Aproveite seu cafe!",
        ],
    },
    2: {
        "titulo": "Configurar o despertador no celular",
        "passos": [
            "Pegue o celular e desbloqueie a tela",
            "Localize e abra o aplicativo de relogio ou despertador",
            "Toque na opcao para adicionar um novo alarme",
            "Ajuste a hora e os minutos que deseja para o alarme",
            "Se necessario, selecione os dias da semana em que o alarme deve repetir",
            "Escolha o toque do alarme",
            'De um nome ao alarme (ex: "Academia")',
            'Toque em "Salvar" ou "Concluir"',
        ],
    },
    3: {
        "titulo": "Ligar um computador",
        "passos": [
            "Verifique se o computador esta conectado a tomada ou fonte de energia",
            "Pressione o botao de ligar",
            "Aguarde alguns segundos ate o sistema carregar",
            "Quando a tela de login aparecer, digite seu usuario (se tiver)",
            "Digite a senha de acesso, se tiver, e pressione Enter",
            "Aguarde a area de trabalho ou tela inicial carregar completamente",
            "Confirme se tudo esta funcionando corretamente antes de iniciar o uso",
        ],
    },
    4: {
        "titulo": "Carregar o celular",
        "passos": [
            "Pegue o carregador compativel com o modelo do seu celular",
            "Verifique se o carregador esta conectado a tomada",
            "Insira o cabo na entrada de carregamento do celular",
            "Confirme se o celular esta carregando",
            "Deixe o celular carregando ate atingir a porcentagem desejada",
            "Quando terminar, retire o cabo com cuidado da entrada do celular",
            "Desconecte o carregador da tomada, se necessario, e guarde-o",
        ],
    },
    5: {
        "titulo": "Assistir a um filme em casa",
        "passos": [
            "Escolha a plataforma onde deseja assistir (ex: Netflix, Prime, YouTube)",
            "Ligue a TV, computador, tablet ou celular",
            "Acesse o aplicativo ou site da plataforma escolhida",
            "Faca login com seu usuario e senha, se necessario",
            "Use a barra de busca ou navegue pelas categorias para escolher um filme",
            'Clique em "Reproduzir" ou "Assistir agora"',
            "Ajuste o volume e, se desejar, ative as legendas ou mude o idioma",
            "Sente-se e aproveite o filme",
            "Ao terminar, feche o aplicativo ou desligue o dispositivo",
        ],
    },
    6: {
        "titulo": "Regar uma planta",
        "passos": [
            "Pegue um regador ou garrafa ou recipiente",
            "Encha o recipiente com agua",
            "Caminhe ate a planta que sera regada",
            "Posicione o regador sobre o vaso, proximo a base da planta",
            "Derrame a agua no solo",
            "Observe se o solo esta umido, sem encharcar",
            "Repita o processo com outras plantas, se houver",
            "Guarde o regador no local apropriado",
        ],
    },
    7: {
        "titulo": "Fazer uma pipoca",
        "passos": [
            "Pegue uma panela com tampa",
            "Coloque-a sobre a boca do fogao",
            "Adicione um fio de oleo no fundo da panela",
            "Acrescente o milho para pipoca",
            "Adicione sal ou outro tempero",
            "Tampe a panela",
            "Ligue o fogo",
            "Aguarde alguns minutos ate ouvir os primeiros estouros",
            "Quando os estouros ficarem mais frequentes, agite levemente a panela",
            "Quando os estouros diminuirem significativamente, desligue o fogo",
            "Com cuidado, destampe a panela para evitar vapor quente",
            "Transfira a pipoca para um recipiente",
            "Sirva!",
        ],
    },
    8: {
        "titulo": "Participar de uma reuniao online",
        "passos": [
            "Verifique o horario da reuniao na agenda ou calendario",
            "Confirme se voce recebeu o link de acesso",
            "Pouco antes do horario, encontre um local silencioso e com boa iluminacao",
            "Ligue e conecte seu dispositivo a internet",
            "Abra o aplicativo ou plataforma (Zoom, Google Meet, Teams, etc.)",
            "Clique no link da reuniao",
            "Ligue a camera e o microfone conforme necessario",
            "Entre na reuniao",
            "Durante a reuniao, ouca com atencao e participe quando solicitado",
            "Anote informacoes importantes, se necessario",
            'Ao final, clique em "Encerrar chamada" ou "Sair da reuniao"',
        ],
    },
    9: {
        "titulo": "Criar uma lista com as tarefas da semana",
        "passos": [
            "Escolha onde vai criar a lista (papel, planner ou app de notas)",
            "Pense em todos os compromissos e responsabilidades da semana",
            "Anote todas as tarefas que precisa realizar",
            "Classifique cada tarefa por categoria (ex: trabalho, casa, estudos)",
            "Organize as tarefas por dia da semana, conforme prazos e prioridades",
            "Revise a lista e ajuste conforme necessario",
            "Adicione lembretes ou horarios, se for util",
            "Salve ou guarde a lista em um local de facil acesso",
            "Consulte a lista diariamente e marque as tarefas concluidas",
        ],
    },
    10: {
        "titulo": "Assistir a um video do Diego no canal da Rocketseat",
        "passos": [
            "Pegue seu celular, tablet ou computador",
            "Conecte o dispositivo a internet",
            "Acesse o YouTube pelo aplicativo ou navegador",
            '"Rocketseat" na barra de busca',
            "Escolha um video do Diego Fernandes",
            "Clique para abrir o video",
            "Ajuste o volume",
            "Assista o conteudo",
            "Ao final, aplique o que aprendeu ou salve o video para rever depois",
        ],
    },
}


# ============================================================
#  PARTE 2 - FLUXOGRAMA (representacao textual)
# ============================================================

fluxogramas = {
    1: {
        "titulo": "Calcular o dobro de um numero",
        "passos": [
            "[INICIO]",
            "[ENTRADA] Leia numero",
            "[PROCESSO] dobro <- numero * 2",
            '[SAIDA] Escreva "O dobro eh:", dobro',
            "[FIM]",
        ],
    },
    2: {
        "titulo": "Verificar se o numero eh menor que 10",
        "passos": [
            "[INICIO]",
            "[ENTRADA] Leia numero",
            "[DECISAO] numero < 10 ?",
            '  |-- SIM --> [SAIDA] Escreva "Eh menor que 10"',
            '  |-- NAO --> [SAIDA] Escreva "Nao eh menor que 10"',
            "[FIM]",
        ],
    },
    3: {
        "titulo": "Contar ate 5",
        "passos": [
            "[INICIO]",
            "[PROCESSO] i <- 1",
            "[DECISAO] i <= 5 ?",
            "  |-- SIM --> [SAIDA] Escreva i",
            "             [PROCESSO] i <- i + 1",
            "             (volta para DECISAO)",
            "  |-- NAO --> [FIM]",
        ],
    },
}


# ============================================================
#  PARTE 3 - PSEUDOCODIGO (com implementacao em Python)
# ============================================================

pseudocodigos = {
    1: {
        "titulo": "Imprimir um numero em tela",
        "pseudo": [
            "Inicio",
            '  Escreva("Digite um numero:")',
            "  Leia num",
            '  Escreva("Voce digitou:", num)',
            "Fim",
        ],
    },
    2: {
        "titulo": "Somar dois numeros",
        "pseudo": [
            "Inicio",
            "  Leia num1",
            "  Leia num2",
            "  soma <- num1 + num2",
            '  Escreva("Resultado:", soma)',
            "Fim",
        ],
    },
    3: {
        "titulo": "Contar de 1 ate 10 usando loop",
        "pseudo": [
            "Inicio",
            "  i <- 1",
            "  Enquanto i <= 10",
            "    Escreva(i)",
            "    i <- i + 1",
            "Fim",
        ],
    },
    4: {
        "titulo": "Verificar se o numero eh par ou impar",
        "pseudo": [
            "Inicio",
            "  Leia num",
            "  Se num % 2 = 0 entao",
            '    Escreva("Par")',
            "  Senao",
            '    Escreva("Impar")',
            "Fim",
        ],
    },
    5: {
        "titulo": "Verificar se numero eh positivo, negativo ou zero",
        "pseudo": [
            "Inicio",
            "  Leia num",
            "  Se num > 0 entao",
            '    Escreva("Positivo")',
            "  Senao Se num < 0 entao",
            '    Escreva("Negativo")',
            "  Senao",
            '    Escreva("Zero")',
            "Fim",
        ],
    },
    6: {
        "titulo": "Calcular media de 3 notas",
        "pseudo": [
            "Inicio",
            "  Leia n1, n2, n3",
            "  media <- (n1 + n2 + n3) / 3",
            '  Escreva("Media:", media)',
            "Fim",
        ],
    },
    7: {
        "titulo": "Verificar se aluno foi aprovado (media >= 5)",
        "pseudo": [
            "Inicio",
            "  Leia nota1, nota2",
            "  media <- (nota1 + nota2) / 2",
            "  Se media >= 5 entao",
            '    Escreva("Aprovado")',
            "  Senao",
            '    Escreva("Reprovado")',
            "Fim",
        ],
    },
    8: {
        "titulo": "Maior entre dois numeros",
        "pseudo": [
            "Inicio",
            "  Leia a, b",
            "  Se a > b entao",
            '    Escreva("Maior:", a)',
            "  Senao",
            '    Escreva("Maior:", b)',
            "Fim",
        ],
    },
    9: {
        "titulo": "Mostrar os multiplos de 3 ate 30",
        "pseudo": [
            "Inicio",
            "  i <- 1",
            "  Enquanto i <= 30",
            "    Se i % 3 = 0 entao",
            "      Escreva(i)",
            "    i <- i + 1",
            "Fim",
        ],
    },
    10: {
        "titulo": "Contagem regressiva de 10 ate 1",
        "pseudo": [
            "Inicio",
            "  i <- 10",
            "  Enquanto i >= 1",
            "    Escreva(i)",
            "    i <- i - 1",
            "Fim",
        ],
    },
}


def pseudo_imprimir_numero():
    num = 42
    print(f"    Numero digitado: {num}")


def pseudo_somar_dois():
    num1, num2 = 15, 27
    soma = num1 + num2
    print(f"    {num1} + {num2} = {soma}")


def pseudo_contar_1_a_10():
    i = 1
    numeros = []
    while i <= 10:
        numeros.append(str(i))
        i += 1
    print(f"    Contagem: {', '.join(numeros)}")


def pseudo_par_ou_impar():
    for num in [4, 7, 12, 3]:
        tipo = "Par" if num % 2 == 0 else "Impar"
        print(f"    {num} -> {tipo}")


def pseudo_positivo_negativo_zero():
    for num in [5, -3, 0, 10, -1]:
        if num > 0:
            resultado = "Positivo"
        elif num < 0:
            resultado = "Negativo"
        else:
            resultado = "Zero"
        print(f"    {num} -> {resultado}")


def pseudo_media_3_notas():
    n1, n2, n3 = 7.5, 8.0, 6.5
    media = (n1 + n2 + n3) / 3
    print(f"    Notas: {n1}, {n2}, {n3}")
    print(f"    Media: {media:.2f}")


def pseudo_aprovado():
    casos = [(7.0, 8.0), (3.0, 4.0), (5.0, 5.0)]
    for nota1, nota2 in casos:
        media = (nota1 + nota2) / 2
        status = "Aprovado" if media >= 5 else "Reprovado"
        print(f"    Notas: {nota1}, {nota2} -> Media: {media:.1f} -> {status}")


def pseudo_maior_entre_dois():
    pares = [(10, 20), (50, 30), (7, 7)]
    for a, b in pares:
        maior = a if a > b else b
        print(f"    {a} vs {b} -> Maior: {maior}")


def pseudo_multiplos_de_3():
    multiplos = []
    i = 1
    while i <= 30:
        if i % 3 == 0:
            multiplos.append(str(i))
        i += 1
    print(f"    Multiplos de 3 ate 30: {', '.join(multiplos)}")


def pseudo_contagem_regressiva():
    numeros = []
    i = 10
    while i >= 1:
        numeros.append(str(i))
        i -= 1
    print(f"    Contagem: {', '.join(numeros)}")


implementacoes_pseudo = {
    1: pseudo_imprimir_numero,
    2: pseudo_somar_dois,
    3: pseudo_contar_1_a_10,
    4: pseudo_par_ou_impar,
    5: pseudo_positivo_negativo_zero,
    6: pseudo_media_3_notas,
    7: pseudo_aprovado,
    8: pseudo_maior_entre_dois,
    9: pseudo_multiplos_de_3,
    10: pseudo_contagem_regressiva,
}


# ============================================================
#  EXIBICAO
# ============================================================

def exibir_cabecalho():
    print("+------------------------------------------------------------+")
    print("|          PRATICA: ALGORITMOS - ROCKETSEAT                   |")
    print("+------------------------------------------------------------+")
    print("|  Aluno:        Levi Cury                                    |")
    print("|  Instituicao:  Faculdade de Tecnologia Rocketseat           |")
    print("|  Disciplina:   Logica de Programacao                        |")
    print("|  Data:         Fevereiro/2026                               |")
    print("+------------------------------------------------------------+")
    print("|  Secoes:                                                     |")
    print("|  1. Descricao Narrativa (10 exercicios)                     |")
    print("|  2. Fluxograma (3 exercicios)                               |")
    print("|  3. Pseudocodigo (10 exercicios)                            |")
    print("+------------------------------------------------------------+")


def exibir_secao(titulo):
    print(f"\n{'#'*62}")
    print(f"  {titulo}")
    print(f"{'#'*62}")


def exibir_descricoes_narrativas():
    exibir_secao("PARTE 1 - DESCRICAO NARRATIVA")

    for num, dados in descricoes_narrativas.items():
        print(f"\n{'='*62}")
        print(f"  Exercicio {num}: {dados['titulo']}")
        print(f"{'='*62}")
        for i, passo in enumerate(dados["passos"], 1):
            print(f"  {i:2d}. {passo}")


def exibir_fluxogramas():
    exibir_secao("PARTE 2 - FLUXOGRAMA (representacao textual)")
    print()
    print("  Legenda das formas:")
    print("  [INICIO] / [FIM]  = Terminal (inicio/fim)")
    print("  [ENTRADA]         = Entrada de dados (paralelogramo)")
    print("  [PROCESSO]        = Processamento (retangulo)")
    print("  [DECISAO]         = Decisao (losango)")
    print("  [SAIDA]           = Saida de dados (paralelogramo)")

    for num, dados in fluxogramas.items():
        print(f"\n{'='*62}")
        print(f"  Exercicio {num}: {dados['titulo']}")
        print(f"{'='*62}")
        for passo in dados["passos"]:
            print(f"  {passo}")


def exibir_pseudocodigos():
    exibir_secao("PARTE 3 - PSEUDOCODIGO (com demonstracao em Python)")

    for num, dados in pseudocodigos.items():
        print(f"\n{'='*62}")
        print(f"  Exercicio {num}: {dados['titulo']}")
        print(f"{'='*62}")

        print("\n  Pseudocodigo:")
        for linha in dados["pseudo"]:
            print(f"    {linha}")

        print("\n  Execucao em Python:")
        implementacoes_pseudo[num]()


def main():
    exibir_cabecalho()
    exibir_descricoes_narrativas()
    exibir_fluxogramas()
    exibir_pseudocodigos()

    print(f"\n{'='*62}")
    print("  Todos os exercicios resolvidos com sucesso!")
    print("  Atividade concluida por Levi Cury - Rocketseat")
    print(f"{'='*62}\n")


if __name__ == "__main__":
    main()
