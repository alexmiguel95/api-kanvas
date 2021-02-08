# API Kanvas

|   Descrição	|   Tecnologias utilizadas	|
|---	|---	|
|Plataforma para guardar receitas. Cadastrar uma receita com suas tags e os ingredientes utilizados |  Python com _django_ e _djangorestframework_. 


&nbsp; 
###  Base URL: 
&nbsp; 
## Endpoints
###  Rotas públicas
####  POST /api/accounts/
> Criar um usuário. Temos três tipos de usuários:


Body JSON:
```json
{
  "name": "Brigadeiro de Champanhe",
  "description": "É um brigadeiro gourmet",
  "instructions": "Junte espumante ao chocolate branco e deixe ferver",
  "tags": [
    {
      "name": "doce"
    },
    {
      "name": "gourmet"
    }
  ],
  "ingredient_set": [
		{
      "name": "chocolate branco",
      "unit": "g",
      "amount": 300
    },
    {
      "name": "espumante",
      "unit": "mL",
      "amount": 100
    }
  ]
}
```
Response:
```json
{
  "id": 2,
  "name": "Brigadeiro de Champanhe",
  "description": "É um brigadeiro gourmet",
  "instructions": "Junte espumante ao chocolate branco e deixe ferver",
  "tags": [
    {
      "name": "doce"
    },
    {
      "name": "gourmet"
    }
  ],
  "ingredient_set": [
    {
      "name": "chocolate branco",
      "unit": "g",
      "amount": 300
    },
    {
      "name": "espumante",
      "unit": "mL",
      "amount": 100
    }
  ]
}
```

####  GET /recipes/
> Recuperar todas as Receitas com suas Tags e Ingredientes.

Response:
```json
[
  {
    "id": 1,
    "name": "Brigadeiro de Champanhe",
    "description": "É um brigadeiro gourmet",
    "instructions": "Junte espumante ao chocolate branco e deixe ferver",
    "tags": [
      {
        "name": "doce"
      },
      {
        "name": "gourmet"
      }
    ],
    "ingredient_set": [
      {
        "name": "chocolate branco",
        "unit": "g",
        "amount": 300
      },
      {
        "name": "espumante",
        "unit": "mL",
        "amount": 100
      }
    ]
  },
  {
    "id": 2,
    "name": "Brigadeiro de Champanhe",
    "description": "É um brigadeiro gourmet",
    "instructions": "Junte espumante ao chocolate branco e deixe ferver",
    "tags": [
      {
        "name": "doce"
      },
      {
        "name": "gourmet"
      }
    ],
    "ingredient_set": [
      {
        "name": "chocolate branco",
        "unit": "g",
        "amount": 300
      },
      {
        "name": "espumante",
        "unit": "mL",
        "amount": 100
      }
    ]
  }
]
```

####  GET /recipes/<int:recipe_id>
> Recuperar uma receita específica.

Response:
```json
{
  "id": 2,
  "name": "Brigadeiro de Champanhe",
  "description": "É um brigadeiro gourmet",
  "instructions": "Junte espumante ao chocolate branco e deixe ferver",
  "tags": [
    {
      "name": "doce"
    },
    {
      "name": "gourmet"
    }
  ],
  "ingredient_set": [
    {
      "name": "chocolate branco",
      "unit": "g",
      "amount": 300
    },
    {
      "name": "espumante",
      "unit": "mL",
      "amount": 100
    }
  ]
}
```

####  DELETE /recipes/<int:recipe_id>
> Apagar uma Receita.

Response:

No Content, HTTP status 204


&nbsp;  
#### Desenvolvedor
**[Alex Miguel](https://www.linkedin.com/in/alexmiguel95/)**

alexmiguel95@gmail.com
