# API Kanvas

|   Como utilizar o projeto	|   Tecnologias utilizadas	|
|---	|---	|
|1º Clone o projeto em um diretório de sua preferência. 
2º  |  Python com _django_ e _djangorestframework_. 


&nbsp; 
###  Base URL: 
&nbsp; 
##  Endpoints públicos
####  POST /api/accounts/
> Criar um usuário. Temos três tipos de usuários:
> * Estudante - terá ambos os campos is_staff e > is_superuser com o valor False
> * Facilitador - terá os campos is_staff == True e > is_superuser == False
> * Instrutor - terá ambos os campos is_staff e is_superuser com o valor True

Criando um estudante

Body JSON:
```json
{
  "username": "student1",
  "password": "1234",
  "is_superuser": false,
  "is_staff": false
}
```
Response - HTTP Status 201:
```json
{
  "id": 1,
  "is_superuser": false,
  "is_staff": false,
  "username": "student1"
}
```

Criando um facilitador

Body JSON:
```json
{
  "username": "facilitator1",
  "password": "1234",
  "is_superuser": false,
  "is_staff": true
}
```
Response - HTTP Status 201:
```json
{
  "id": 2,
  "is_superuser": false,
  "is_staff": true,
  "username": "facilitator1"
}
```

Criando um instrutor

Body JSON:
```json
{
  "username": "instructor1",
  "password": "1234",
  "is_superuser": true,
  "is_staff": true
}
```
Response - HTTP Status 201:
```json
{
  "id": 3,
  "is_superuser": true,
  "is_staff": true,
  "username": "instructor1"
}
```

####  POST /api/login/
> Fazer login

Body JSON:
```json
{
	"username": "facilitador1",
	"password": "12345"
}
```
Response - HTTP Status 200:
```json
{
  "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

####  GET /api/courses/
> listar todos os cursos, mostrando cada aluno matriculado no curso.

Response - HTTP Status 200:
```json
[
  {
    "id": 1,
    "name": "Javascript 101",
    "user_set": [
      {
        "id": 1,
        "is_superuser": false,
        "is_staff": false,
        "username": "luiz"
      }
    ]
  },
  {
    "id": 2,
    "name": "Python 101",
    "user_set": []
  }
]
```

&nbsp;
## Endpoints restritos
Os endpoints a seguir estão disponíveis apenas para usuários com um token de autenticação. No header, espeficar nesse formato:
```json
Authorization: Token <token aqui>
```

####  POST /api/courses/
> Criando um curso. Apenas um instrutor pode criar e matricular usuarios nos cursos.

Header:
```json
// Authorization: Token <instrutor>
```

Body JSON:
```json
{
	"name": "Javascript 101"
}
```
Response - HTTP Status 201:
```json
{
  "id": 1,
  "name": "Javascript 101",
  "user_set": []
}
```

####  PUT /api/courses/registrations/
> Matriculando estudantes em um curso.

Header:
```json
// Authorization: Token <instrutor OU facilitador>
```

Body JSON:
```json
{
	"course_id": 1,
	"user_ids": [1, 2, 7]
}
```
Response - HTTP Status 200:
```json
{
  "id": 1,
  "name": "Javascript 101",
  "user_set": [
    {
      "id": 1,
      "is_superuser": false,
      "is_staff": false,
      "username": "luiz"
    },
    {
      "id": 7,
      "is_superuser": false,
      "is_staff": false,
      "username": "isabela"
    },
    {
      "id": 2,
      "is_superuser": false,
      "is_staff": false,
      "username": "raphael"
    }
  ]
}
```

####  POST /api/courses/registrations/
> Criando uma atividade. Um estudante pode criar uma atividade porém não pode atribuir uma nota. Somente instrutores e facilitadores podem atribuir uma nota para um atividade de um estudante.

Header:
```json
// Authorization: Token <estudante>
```

Body JSON:
```json
{
	"repo": "gitlab.com/cantina-kenzie",
	"user_id": 7,
	"grade": 10
}
```
Response - HTTP Status 201:
```json
{
  "id": 6,
  "user_id": 7,
  "repo": "gitlab.com/cantina-kenzie",
  "grade": null
}
```

####  PUT /api/courses/registrations/
> Editando uma atividade. Somente instrutores e facilitadores.

Header:
```json
// Authorization: Token <instrutor OU facilitador>
```

Body JSON:
```json
{
  "id": 6,
  "repo": "gitlab.com/cantina-kenzie",
  "user_id": 7,
  "grade": 10
}
```
Response - HTTP Status 201:
```json
{
  "id": 6,
  "user_id": 7,
  "repo": "gitlab.com/cantina-kenzie",
  "grade": 10
}
```

####  GET /api/activities/
> Recuperando atividafes. Estudante pode apenas visualizar uma lista com as suas próprias atividades. Já os instrutores e facilitadores podem visualizar todas as atividades de todos os estudantes e filtrar as atividades por usuários.

Header:
```json
// Authorization: Token <estudante>
```

Response:
```json
[
  {
    "id": 1,
    "user_id": 1,
    "repo": "github.com/luiz/cantina",
    "grade": null
  },
  {
    "id": 2,
    "user_id": 1,
    "repo": "github.com/hanoi",
    "grade": null
  },
  {
    "id": 3,
    "user_id": 1,
    "repo": "github.com/foodlabs",
    "grade": null
  },
]
```

Header:
```json
// Authorization: Token <facilitador OU instrutor>
```

Response:
```json
[
  {
    "id": 1,
    "user_id": 1,
    "repo": "github.com/luiz/cantina",
    "grade": null
  },
  {
    "id": 2,
    "user_id": 1,
    "repo": "github.com/hanoi",
    "grade": null
  },
  {
    "id": 3,
    "user_id": 1,
    "repo": "github.com/foodlabs",
    "grade": null
  },
  {
    "id": 35,
    "user_id": 99,
    "repo": "github.com/kanvas",
    "grade": null
  },
]
```

####  GET /api/activities/<int:user_id>/
> Filtrando atividades fornecendo um user_id. Somente instrutores e facilitadores.

Header:
```json
// Authorization: Token <facilitador OU instrutor>
```

Response:
```json
[
  {
    "id": 1,
    "user_id": 1,
    "repo": "github.com/luiz/cantina",
    "grade": null
  },
  {
    "id": 2,
    "user_id": 1,
    "repo": "github.com/hanoi",
    "grade": null
  },
  {
    "id": 3,
    "user_id": 1,
    "repo": "github.com/foodlabs",
    "grade": null
  },
]
```

&nbsp;  
#### Desenvolvedor
**[Alex Miguel](https://www.linkedin.com/in/alexmiguel95/)**

alexmiguel95@gmail.com
