<h1>Alexa Skill - Monitoramento GoodWe</h1>

Esta é uma Alexa Skill para monitoramento de sistemas fotovoltaicos GoodWe. A skill permite que o usuário pergunte sobre status, consumo e geração de energia em tempo real, via integração com uma API intermediária, que por sua vez consome dados da API oficial da GoodWe.
  <h2>Estrutura do Projeto</h2>

    Skill Backend: Python (usando o Alexa Skills Kit SDK para AWS Lambda)

    API Intermediária: Responsável por buscar os dados da GoodWe, tratar e repassar para a skill.

    API GoodWe: API oficial dos inversores GoodWe.

 <h2>Fluxo de Dados</h2>

    Usuário pergunta: "Alexa, qual é o status da GoodWe?"

    Skill Backend → faz um GET para API intermediária

    API → faz um GET para a API da GoodWe

    Resposta → Volta da GoodWe → API → Alexa → Fala com o usuário.

<h2>Endpoints da API (Intermediária)</h2>
Recurso	Método	URL Exemplo	Retorno esperado
Status do Sistema	GET	https://api-intermediaria.com/status	{ "status": "online" }
Consumo Atual	GET	https://api-intermediaria.com/consumo	{ "consumo": "350W" }
Geração Atual	GET	https://api-intermediaria.com/geracao	{ "geracao": "1200W" }
<h2>Intents disponíveis na Skill</h2>
Intent	Exemplo de Pergunta	Resposta Esperada
GetStatusIntent	"Alexa, qual é o status da GoodWe?"	"O status atual é online."
GetConsumoIntent	"Alexa, qual é o consumo?"	"O consumo atual é de 350W."
GetGeracaoIntent	"Alexa, qual é a geração?"	"A geração atual é de 1200W."
FallbackIntent	Perguntas inválidas	Mensagem de ajuda para reformular a pergunta.
 <h2>Deploy da Skill (Resumo)</h2>

    Suba o código Python da skill na AWS Lambda.

    Copie o ARN da Lambda e cole no campo de Endpoint no Alexa Developer Console.

    Teste a skill pelo Alexa Simulator.

    Garanta que a API intermediária e a da GoodWe estejam online e acessíveis via HTTPS.

Requisitos da API intermediária

    Deve estar online, com certificado HTTPS válido.

    Retornar os dados em JSON, exatamente nos formatos esperados pela skill (exemplo: {"status": "online"}).

Testes Locais (se quiser emular sem a GoodWe)

Durante o desenvolvimento, você pode simular os endpoints da sua API com dados mockados (fake), para testar a skill mesmo que a API da GoodWe esteja offline.

Exemplo simples de resposta mockada para o endpoint /status:

{
  "status": "online"
}

<h2>Tecnologias Usadas</h2>

    Python 3.x

    Alexa Skills Kit SDK

    AWS Lambda

    API REST (intermediária)

    API GoodWe (oficial)
