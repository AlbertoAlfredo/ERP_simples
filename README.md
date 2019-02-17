# ERP simples

Python 3.6+ e Django 2.1.3+

Sistema simples de ERP para cadastro de produtos, serviços, clientes e controle de estoque

O sistema ainda está em fase alpha e estou trabalhando com Django, HTML, CSS e javascript

## Objetivo

O App tem como objetivo ser um sistema simples que seja o ideal para quem está com sua pequena empresa ou seja MEI e tenha um sistema que supra sua necessidade básica.

Tenho a meta de expandir o aplicativo para que ele com o tempo consiga suprir toda e qualquer necessidade que uma empresa possa ter.

O aplicativo tem como visão inicial ser instalado localmente e assim estou trabalhando para que o mesmo quando pronto possa ser facilmente instalado.


##Etc

Qualquer ajuda é sempre bem vinda

O aplicativo é feito sob a licensa Apache 2.0 que garante total liberdade a qualquer um de usar para qualquer fim o código/aplicativo e apenas deve informar de onde veio o código e que hoveram mudanças, além de que se um dia eu tiver uma marca registrada ela não está incluida no app e não deverá ser usada.

Na prática você está livre para usar a vontade e mudar o quanto quiser, apenas coloque no readme de onde veio a base e que a mesma foi modificada.

## Baixando e rodando a app

Baixe e rode o `setup.sh`. (Ainda sendo criado)

```
wget https://....../
source setup.sh
```

Ou siga o passo a passo.

1. Clone o repositório
2. Crie um virtualenv com Python 3.5+
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Rode o arquivo de migrações
7. Crie o super usuário (opcional)
8. Execute o server.

```bash
git clone https://github.com/AlbertoAlfredo/ERP_simples.git
cd ERP_simples
python -m venv venv
source venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional
pip install -U pip # update the pip
pip install -r requirements.txt
python manage.py migrate
python manage.py create_admin #opcional
python manage.py runserver
```


## Changelog

Veja o [Changelog](CHANGELOG.md). (ainda sendo criada)


Necessário instalar o python 3.6



##Copyright

Copyright [2019] [Alberto Alfredo]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.