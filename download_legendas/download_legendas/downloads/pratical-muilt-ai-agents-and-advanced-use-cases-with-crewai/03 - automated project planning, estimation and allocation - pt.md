Vamos mergulhar em um planejamento automatizado de projeto.

O objetivo aqui é usar uma equipe para nos ajudar a dividir um projeto em tarefas, estimá-las e fazer alguma alocação.

Esse é um caso de uso comum para consultorias e agências web, que estão tentando oferecer o máximo de propostas possível.

Assim, quando as pessoas procuram essas empresas para construir projetos, elas podem rapidamente estimar e planejar o projeto.

Para essa equipe, vamos trabalhar com três agentes.

Usaremos um planejador de projeto, um analista de estimativa e um estrategista de alocação.

E para cada um desses agentes, teremos uma tarefa.

Teremos a divisão das tarefas, a estimativa de tempo e a alocação de recursos.

Este é um conjunto de equipe bem simples, onde temos apenas três agentes e três tarefas, com cada agente executando uma única tarefa.

A ideia aqui é que, ao fornecer entradas iniciais sobre o que estamos tentando alcançar, qual é o projeto, qual o critério de aceitação para o projeto e quem são as pessoas disponíveis para trabalhar nele, possamos rapidamente criar um plano de projeto.

E este plano de projeto deve incluir tarefas, suas alocações e também os principais marcos de como iremos acompanhar o progresso do projeto.

A ideia é usar esses agentes para gerar um formato estruturado em JSON, que podemos inserir em qualquer ferramenta de gerenciamento de projetos.

Se estivermos usando o Jira ou Trello, por exemplo, poderemos enviar essas tarefas e suas alocações para essas ferramentas.

IMAGEM 01 

Vamos olhar o código.

A primeira coisa que faremos é importar as bibliotecas iniciais.

Vamos garantir que carregamos as variáveis de ambiente.

Agora, todas as bibliotecas de que precisaremos.

Neste caso, vamos usar a biblioteca OS, a biblioteca Yaml para carregar nossos arquivos Yaml de agentes e tarefas.

E então, do CrewAI, vamos trazer nossas três principais classes: a classe de agente, a classe de tarefa e a classe de equipe.

Isso deve ser tudo o que precisamos para iniciar esta equipe.

Agora vamos configurar o modelo que vamos usar.

Por padrão, o CrewAI usa modelos da OpenAI.

Mas lembre-se de que você pode usar qualquer modelo que preferir.

Pode usar qualquer provedor disponível, incluindo HuggingFace, Azure, Anthropic e outros.

Para este caso, vamos configurar o modelo da OpenAI para ser o GPT-4o-mini.

Dessa forma, conseguimos manter os custos baixos e ter uma boa execução.

Agora, vamos carregar nosso arquivo Yaml de agentes e tarefas.

Isso deve ser bem direto, mas vamos dar uma olhada rápida no código.

Aqui, o snippet de código carrega os arquivos Yaml de agentes e de tarefas, atribuindo-os a duas variáveis: agents_config e tasks_config.

Antes de continuar, vamos dar uma breve olhada em como esses arquivos de agentes e tarefas se parecem.

No arquivo Yaml de agentes, temos três agentes: o agente de planejamento de projeto, o agente de estimativa e o agente de alocação de recursos.

Cada agente tem um papel, um objetivo, uma história de fundo e algumas configurações extras.

Neste caso, não permitimos que nossos agentes deleguem trabalho entre si, para garantir que a execução seja o mais simplificada possível, e também ativamos o modo verboso, permitindo ver o comportamento dos agentes, as ferramentas que usam e o processo de execução de cada tarefa.

Você pode explorar os papéis e objetivos dos agentes e até brincar com a história de fundo se quiser, mas o interessante é que algumas variáveis estão sendo interpoladas nas descrições dos agentes.

É possível ver a interpolação de variáveis como tipo de projeto, objetivos do projeto e indústria em toda a definição dos agentes.

Agora vamos ver a definição das tarefas no Yaml.

No arquivo de tarefas, temos três tarefas: a divisão de tarefas, a alocação de tempo e a alocação de recursos.

Novamente, você verá as mesmas variáveis interpoladas nas tarefas, onde também se nota o tipo de projeto, além de novas variáveis como requisitos do projeto e membros da equipe.

Sinta-se à vontade para ajustar as descrições das tarefas e agentes, caso queira ver resultados diferentes ao executar o notebook.

Voltando ao código, agora que temos os arquivos de configuração dos agentes e das tarefas carregados, podemos criar um modelo Pydantic para nossa saída estruturada.

Lembre-se de que, neste caso, o que queremos é ter um planejamento completo de projeto ao final da execução da equipe.

Isso significa que queremos poder enviar essa saída para sistemas externos, se necessário.

E, para isso, precisamos de uma saída estruturada.

Aqui, estamos criando três classes: uma estimativa de tarefa, um marco e um plano de projeto.

O plano de projeto conterá basicamente uma lista de tarefas e marcos.

O marco terá um nome e uma lista de tarefas.

A estimativa de tarefa é o modelo mais simples que temos, contendo um nome de tarefa, o número estimado de horas necessárias e os recursos requeridos, incluindo o nome das pessoas que vão realizar a tarefa.

Ao final da execução da equipe, deveremos ter esse objeto de plano de projeto pronto para que possamos transformá-lo em JSON ou dicionário, permitindo enviar para sistemas externos ou fazer o que for necessário.

É uma maneira razoável e prática de enviar a saída para qualquer sistema externo que você possa ter.

Agora, para criarmos nossos agentes e tarefas, precisamos consultar os arquivos de configuração Yaml.

Observe que ao criar cada um dos agentes, estamos nos referindo à variável agents_config do arquivo Yaml e indicando a chave que fornece a configuração para cada agente.

Para as tarefas, carregamos o arquivo tasks_config com as configurações Yaml e especificamos a chave Yaml que contém a configuração de cada tarefa.

Estamos sendo muito explícitos aqui para tornar o entendimento mais fácil.

Na última tarefa de alocação de recursos, temos um atributo de saída pydantic.

Isso significa que queremos que a saída desta tarefa final seja um objeto pydantic, o que criamos anteriormente, o plano de projeto.

Esse é o output estruturado que queremos para possivelmente enviar para um sistema externo.

Ao finalizar, iniciamos uma equipe, com nossos três agentes e três tarefas, em um setup bem direto.

Agora, vamos falar sobre as entradas que enviamos para essa equipe e como essas informações são inseridas.

Lembre-se de que definimos um conjunto de variáveis para interpolação nos agentes e nas tarefas.

Ao configurá-las, estamos detalhando o projeto, a indústria, os objetivos do projeto, os membros da equipe e os requisitos do projeto.

Esse é um projeto de website para uma empresa do setor de tecnologia, e o objetivo é criar um site para um pequeno negócio.

Teremos cinco pessoas trabalhando nele, incluindo um gerente de projeto, um engenheiro de software, um designer e dois engenheiros de QA.

Após uma chamada inicial com o cliente, é possível trazer essas informações para nossa equipe, para que ela divida as tarefas e estime-as automaticamente.

Isso pode ser muito útil, especialmente para pequenas empresas ou consultorias que buscam acelerar a criação de propostas.

Requisitos do projeto: design responsivo, moderno e visualmente atraente, fácil de usar, com páginas como "sobre nós", "serviços", "contato", blog, links de redes sociais e depoimentos.

Essas são as informações que enviaremos à nossa equipe, e elas serão interpoladas ao longo dos agentes e tarefas para que possam realizar o trabalho.

Então, vamos executar a equipe e ver o que acontece.

Vai ser divertido.

Para iniciar, criamos um dicionário com todas as nossas entradas e o passamos como input para a função kickoff da equipe.

Chamando essa função, veremos nossos agentes começando o trabalho.

O agente planejador do projeto inicia analisando os requisitos para o projeto de website.

Já é possível ver uma das interpolações acontecendo: o tipo de projeto.

O agente exibe a lista de tarefas detalhada, incluindo descrições, cronograma, dependências, entregas e as pessoas atribuídas.

Durante essa execução, também geramos um gráfico de Gantt com todas as tarefas, suas durações, dependências e uma conclusão detalhada da divisão das tarefas.

Depois, o próximo agente é o analista de estimativas.

Este agente estima cada uma das tarefas.

Antes de ver o resultado final, é importante saber o custo de execução em produção.

Usando o GPT-4o-mini, o custo é de US$ 0,15 por milhão de tokens, e o Crew já fornece métricas de uso.

Rodar essa execução é bem barato, custando cerca de 0,001 centavos e usando 7000 tokens.

Agora vamos ver o resultado final: um dicionário com lista de tarefas, cada tarefa com nome e horas estimadas e lista de recursos.

Também temos marcos, onde cada um inclui uma lista de tarefas relacionadas.

Exibimos cada tarefa e marco como dataframes do Pandas para facilitar a visualização.

Esse exemplo fictício destaca o poder de automação, reduzindo processos que levariam horas a poucos minutos.

Esse caso de uso já está sendo aplicado e pode beneficiar você ou sua empresa.

Isso é só o começo.

Na próxima lição, aprenderemos como criar equipes ainda mais complexas e interessantes.

Nos vemos em breve.