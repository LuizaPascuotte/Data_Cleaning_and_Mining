# Projeto mineração de dados com Design de moda

A indústria de vestuário é um dos principais exemplos da globalização industrial desta era moderna. É uma indústria altamente intensiva em mão de obra com muitos processos manuais. Satisfazer a enorme demanda global por produtos de vestuário depende principalmente do desempenho de produção e entrega dos funcionários nas empresas de fabricação de vestuário. Portanto, é altamente desejável entre os tomadores de decisão na indústria de vestuário rastrear, analisar e prever o desempenho de produtividade das equipes de trabalho em suas fábricas.

O conjunto de dados a ser visualizado inclui atributos importantes do processo de fabricação de roupas e da produtividade dos funcionários, que foram coletados manualmente e também validados por especialistas do setor.

## Inicializando

Utilização de algumas bibliotecas necessárias
Pandas: O pandas é uma biblioteca poderosa para manipulação e análise de dados. Ela facilita o carregamento de arquivos, a limpeza de dados e a criação de estruturas como DataFrames

- Numpy: O numpy é utilizado para cálculos matemáticos eficientes e manipulação de arrays. Ele é frequentemente usado em conjunto com o pandas para realizar operações matemáticas e estatísticas em dados.

- Seaborn: O seaborn é uma biblioteca de visualização de dados baseada no matplotlib, mas com uma interface mais simples e visualmente atraente. Ela facilita a criação de gráficos estatísticos e o desenho de relações entre variáveis.

- matplotlib.pyplot: O matplotlib é a biblioteca base para a criação de gráficos em Python. Com o módulo pyplot, você pode criar gráficos personalizados, ajustar estilos e controlar as visualizações.(Auxiliar do Seaborn).

- sklearn.preprocessing.StandardScaler: O StandardScaler é uma ferramenta da biblioteca scikit-learn (ou sklearn) que padroniza os dados, escalando-os para ter média zero e variância igual a 1. Isso é importante quando diferentes variáveis têm escalas diferentes, especialmente em algoritmos de machine learning.

e o principal para nosso projeto: (Instalação)

- ucimlrepo.fetch_ucirepo: Essa função permite acessar datasets do repositório UCI Machine Learning Repository, que contém uma ampla variedade de conjuntos de dados prontos para análise. Estamos utilizando o fetch_ucirepo para carregar diretamente os dados de interesse do repositório UCI e usá-los nas análises.

Siga os passos abaixo para configurar o ambiente e instalar as dependências necessárias.

1. Clone o repositório

`git clone https://github.com/usuario/repositorio.git `
`cd repositorio `

2. Crie um ambiente virtual
No diretório do projeto clonado, crie um ambiente virtual:
`virtualenv venv`

3. Ative o ambiente virtual
Windows:
`venv\Scripts\activate`

Linux:
`source venv/bin/activate`

4. Instale as dependências do projeto
`pip install -r requirements.txt`

# Colab explicativo
Abaixo há o link do colab com cada função já executada e a explicação de cada tarefa delas e o justificativa das escolhas realizadas:

https://colab.research.google.com/drive/1ApHSFplphs66uHK9X8jbyo_nWauItrjD#scrollTo=ntNkLRJdvoai
