# Tutorial sobre como conectar uma aplicação em Flask com o serviço App ID da IBM

O objetivo deste tutorial é fornecer um exemplo simples de aplicação em Flask conectando 
com o serviço [App ID da IBM](https://www.ibm.com/cloud/app-id).

Escrevi este projeto porque percebi que existem diversos exemplos de aplicações Flask conectando com o serviço
App ID. No entanto, nenhum destes exemplos funciona na sua integridade. Muitos deles usam versões antigas de 
bibliotecas, nomes errados para as variáveis de conexão ao App ID, entre outros problemas.

Na documentação do [App ID](https://cloud.ibm.com/docs/appid) é fácil encontrar exemplos em Node.js e Java. Inclusive, existem alguns SDKs que facilitam muito o trabalho. No entanto, não tem documentação para Python.  

Espero que este exemplo seja fácil de entender para quem precisa conectar uma aplicação escrita em Flask com um 
serviço de autenticação, como o App ID. Por favor, para fazer este exemplo funcionar, siga as instruções que estão no arquivo de [instalação](Install.md).

## Pré-requisitos

Este exemplo assume: 

* que você já tenha uma instância de App ID na [IBM Cloud](https://cloud.ibm.com/). Se não tiver, é só acessar a IBM Cloud e criar uma instância do App ID. Existe uma versão free que permite utilizar até 1000 eventos de autenticação e autorização. É bastante para fazer alguns testes! 

* que a sua aplicação é escrita em Python, usando [Flask](https://flask.palletsprojects.com/en/1.1.x/).

## Usei Flask-pyoidc

A extensão de Flask para autenticação com o protocolo OpenIS que eu utilizei foi a [Flask-pyoidc](https://pypi.org/project/Flask-pyoidc/). Por que? Porque foi a que funcionou! E a que pareceu mais simples ;) 

## Dúvidas

Se tiver alguma dúvida é só me mandar um email para fbarth@br.ibm.com ou fabricio.barth@gmail.com. 
