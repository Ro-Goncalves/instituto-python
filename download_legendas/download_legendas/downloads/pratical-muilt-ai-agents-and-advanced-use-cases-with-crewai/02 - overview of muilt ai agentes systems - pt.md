Nesta aula, vamos fazer uma visão geral dos sistemas de agentes de IA múltiplos.

Vamos falar sobre os blocos de construção que compõem esses agentes de IA.

Vamos falar sobre os próprios agentes, mas também sobre tarefas, equipes e todas as diferentes coisas que fazem esses agentes funcionarem.

Coisas como cache, memória, guardrails e tudo mais.

Isso será ótimo para atualizar você sobre tudo o que você precisa saber para iniciar sua jornada com sistemas de agentes de IA.

Então, vamos mergulhar na aula.

O que você aprenderá neste curso:

Você aprenderá muito!

Vamos falar sobre automação multi-agente no mundo real.

Isso significa que você vai colocar a mão na massa e construir muitos projetos diferentes que vão permitir que você entenda como construir essas automações para qualquer caso de uso que você possa ter.

Você vai construir um planejamento de projeto automatizado usando equipes e agentes múltiplos.

Você também vai construir um caso de uso de monitoramento de projeto na qualificação e pontuação de leads.

E tem muito mais.

Vamos falar sobre análise e relatório de dados de suporte, criação de conteúdo personalizado e escala em muitos outros casos de uso.

Então fique por aí porque isso vai ser muito divertido.

Antes de começarmos a falar sobre isso, vamos verificar um exemplo rápido de quão poderosos esses sistemas podem ser e que tipo de automações você realmente pode obter deles.

Então, vamos começar assistindo a este rápido exemplo.

Aqui, você pode ver que estou prestes a entrar em uma chamada com o CEO da Zendesk.

Então eu quero ter alguns materiais de vendas.

Eu apenas coloquei o e-mail dele lá e começamos fazendo uma pesquisa sobre Tom.

Descobrimos que ele tem experiência em vendas, marketing e liderança.

E também aprendemos muito sobre a Zendesk.

Sabemos que a Zendesk foi fundada em 2007.

E todos esses dados foram pesquisados por agentes.

E agora esses agentes montaram esta página de destino/PDF que podemos exportar e enviar para Tom.

E este PDF está passando pelo CrewAI, mas da perspectiva da Zendesk.

Está falando tudo sobre a cultura da Zendesk e como eles estão tentando simplificar a complexidade.

É um caso de uso muito legal onde você pode ver esses agentes não apenas pesquisando, mas realmente produzindo um relatório completo que pode nos ajudar a sair de uma chamada, por exemplo.

E existem muitos outros casos de uso por aí.

Podemos ver muitas automações operacionais.

E também existem muitos casos de uso de vendas.

Também vemos muitos casos de uso de marketing, desenvolvimento de código, pesquisa, educação, suporte.

Existem muitos casos de uso diferentes abrangendo muitos verticais diferentes.

E a questão é que, independentemente do vertical para o qual você está construindo casos de uso, definitivamente vemos um padrão comum.

Existe uma espécie de distribuição de cauda longa do que esses agentes e essa automação estão tentando fazer.

Geralmente começa com você puxando dados de sistemas existentes.

Às vezes, esses sistemas serão ERP, CRM, banco de dados ou qualquer outro.

Depois de extrair esses dados, geralmente há uma etapa de pesquisa, e aqui você pode pesquisar em documentos, na internet ou em outros sistemas que possa ter.

Mas depois disso, você passa por um processo de análise.

E a análise pode ser comparar esses dados ou extrair dados específicos, ou mesmo inferir novos dados que você não tinha antes.

Depois de alguma análise, a maioria dos casos de uso passa por um processo de sumarização, onde você deseja extrair aprendizados e plotar gráficos, ou construir resumos executivos específicos, e então, no final, você pode ir para relatórios.

E às vezes você quer esse relatório como um PDF ou como um json, para que você possa empurrá-lo para outro sistema ou como um markdown.

A questão é que, no final disso, você provavelmente vai querer empurrar isso para um sistema existente.

Então, independentemente do que seja o vertical, se é vendas, se é marketing, se é RH, seja lá o que for.

A maioria dos casos de uso geralmente gira em torno desse processo de pesquisa e análise, sumarização e relatório.

Nem necessariamente todos eles e nem necessariamente sempre nessa série de passos.

Mas esses são a maior parte dos casos de uso que vemos por aí.

Claro, há empresas que estão levando isso ao limite, tentando fazer coisas muito inovadoras usando modelos de vídeo, modelos de imagem e muito mais.

E vamos falar um pouco sobre isso também.

IMAGEM 1 

Então, uma rápida recapitulação.

Se esta é a primeira vez que você conhece sistemas de agentes múltiplos e CrewAI, quero falar sobre o que são e como construí-los.

Então, há uma diferença entre os aplicativos regulares que temos construindo como engenheiros ao longo dos anos e esse novo tipo de aplicativos de IA.

Se você pensar em aplicativos regulares, geralmente eles são fortemente tipados.

O que quero dizer com isso é que você tem um bom entendimento de quais são os dados que estão entrando em seu aplicativo, e você também tem um ótimo entendimento de quais são as transformações que esses dados vão passar para lhe dar sua saída esperada.

Então, um bom exemplo disso seria um sistema onde você está recebendo entradas de um formulário de lead, e você entenderá que você tem uma série de condições que dependendo dessas respostas, você terá uma série de automações ou saídas.

Mas então, se você olhar para esses novos aplicativos, o que estou chamando aqui de aplicativos de IA, eles são extremamente diferentes.

Porque agora eles são muito mais fuzzy.

Isso significa que você não tem um bom entendimento sobre quais são os dados que estão entrando nisso.

Por exemplo, se você pensar no ChatGPT, você não sabe se o texto que o usuário está colocando lá é uma receita ou uma tese de PhD ou qualquer outra coisa, é confuso.

E então esses dados passam por um modelo que é uma caixa preta, e isso então vai para uma saída fuzzy porque você não sabe qual será a saída.

Isso realmente depende muito da entrada e do modelo.

Então você pode pensar em agentes Multi-IA como um tipo de aplicativo de IA que é muito mais fuzzy.

Mas por causa disso, permite que você construa automações que simplesmente não eram possíveis antes, porque agora você não precisa tratar cada caso de borda.

Você pode basicamente deixar seus agentes decidirem em tempo real como vão reagir a dados específicos e decidir quais ferramentas usar para atingir a tarefa que você deseja que eles façam.

E quando você olha para esses agentes, qual é a anatomia deles? Bem, começa bem simples.

Você tem um LLM no centro, e esse LLM pode ter acesso a algumas ferramentas.

E uma vez que você dá a esse LLM uma tarefa, ele vai encontrar uma maneira de usar essas ferramentas para fornecer uma resposta final.

E quando você sobe um degrau, o que você vê são esses sistemas multi-agentes onde agora você não tem apenas um agente, mas sim dois, três ou muitos mais.

E agora esses agentes não só podem usar ferramentas eles mesmos, mas podem delegar trabalho uns aos outros e fazer perguntas uns aos outros para atingir o resultado final que você deseja.

E geralmente começa bem simples, mas uma vez que você começa a trazer essa automação para um ambiente de produção, o que você percebe é que há tantas necessidades que você vai precisar aprender que você vai precisar de uma camada de cache.

Então, quaisquer ferramentas que seus agentes estejam usando, elas não estão consumindo créditos necessários.

E usando essas ferramentas repetidamente.

Você também quer ter certeza de que eles tenham uma camada de memória, para que eles se lembrem do que fizeram no passado e compartilhem sua memória uns com os outros.

Então, se eles já encontraram esse mesmo ponto de dados novamente, eles se lembrarão e como lidaram com isso da última vez.

Há também dados de treinamento, algo sobre o que vamos falar nesta aula específica.

E estou muito animado com isso.

Existem também guardrails e como você vai proteger esses agentes de entrar em alucinações loucas e muito mais.

IMAGEM 02 - 02

E não apenas todos esses recursos, mas uma vez que você tem esses agentes trabalhando juntos, você realmente precisa pensar em como deseja orquestrá-los.

Às vezes, você só quer que eles façam seu trabalho sequencialmente.

Outras vezes, você quer ter um agente gerente que vai delegar trabalho e revisar a saída, mas você pode enlouquecer com isso.

Então você pode ter uma abordagem híbrida onde algumas tarefas serão executadas em paralelo e outras tarefas vão esperar várias tarefas terminarem antes de seguir em frente.

E você vai criar um exemplo como esse também.

Outros serão concluídos em paralelo e outros podem ser completamente assíncronos.

Então há muitos casos de uso diferentes.

E também, você pode ficar ainda mais complexo se quiser, fazendo multi-equipes.

E você vai usar um recurso que chamamos de fluxos.

Onde você pode conectar o resultado de uma equipe com outra.

Tudo bem.

Então você acabou de aprender sobre agentes de IA, como eles funcionam, qual é a anatomia deles e como você pode colocá-los para trabalhar juntos.

Bem, quais são os principais blocos de construção para construir esses sistemas de agentes de IA múltiplos? Bem, tudo começa com agentes.

Mas você também precisa ter certeza de que tem as tarefas.

Neste caso de uso, você pode ver que temos mais tarefas do que agentes.

E isso não é um problema porque um agente pode estar fazendo várias tarefas.

..E vamos ver alguns exemplos disso.

Para que esses agentes possam realizar essas tarefas, precisamos fornecer ferramentas a eles.

Você pode fornecer ferramentas aos seus agentes, para que eles possam usar dados ao executar qualquer tarefa, ou você pode fornecer ferramentas às suas tarefas, para que seus agentes saibam quais ferramentas usar para realizar essa tarefa.

Uma vez que você tem isso, você basicamente tem uma equipe.

Uma equipe é uma combinação de vários agentes e suas tarefas.

E uma vez que você tem todos esses agentes e tarefas, o CrewAI entra em ação e fornece todos os recursos de que você precisa para executar essas coisas em produção, adicionando guardrails para evitar que seus agentes alucinem, mas também testando para que você possa medir a qualidade de seus agentes e tarefas.

Também permite delegações onde seus agentes podem delegar automaticamente e fazer perguntas uns aos outros, e então dados de treinamento para que você possa treinar esses agentes ainda mais na memória.

Então esses agentes ficam melhores com o tempo.

Tem muito mais que vamos falar, então fique por aí.

IMAGEM 04

Então, vamos olhar para esses agentes e tarefas.

Todo agente e CrewAI precisa ter um papel, um objetivo e uma história de fundo.

E toda tarefa precisa ter uma descrição, uma saída esperada e um agente.

Então agora esses agentes são realmente definidos como arquivos YAML.

Você vai revisar isso em nossas aulas, onde você pode facilmente ver como esses agentes têm seu papel, sua história de fundo e suas tarefas, também com suas descrições e saídas esperadas.

Isso torna mais fácil para pessoas não técnicas contribuírem com esses agentes e tarefas, simplesmente atualizando arquivos YAML em vez de ter que atualizar qualquer código.

Tudo bem.

IMAGEM 05

Agora que sabemos que podemos criar agentes e tarefas usando arquivos YAML, por que não sujamos as mãos? E construímos nossa primeira equipe.

Isso vai ser tão emocionante.

Vamos para o nosso próximo passo, onde vamos mergulhar em um notebook Jupyter.

E vamos montar nossa primeira equipe juntos.

Nos vemos lá em um segundo.