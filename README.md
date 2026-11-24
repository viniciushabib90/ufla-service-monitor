# UFLA Service Monitor

Microsserviço desenvolvido como trabalho prático da disciplina DevOps, com o objetivo de monitorar a disponibilidade HTTP de serviços institucionais da Universidade Federal de Lavras (UFLA).

## 1. Tecnologias utilizadas

- Python 3.14
- FastAPI
- Uvicorn
- Pytest
- Docker
- Kubernetes
- HashiCorp Nomad
- GitHub Actions

## 2. Funcionalidades

O microsserviço disponibiliza três endpoints:

| Endpoint | Descrição |
|---|---|
| `/` | Informações gerais da aplicação |
| `/health` | Verificação de saúde do microsserviço |
| `/services` | Consulta da disponibilidade dos serviços institucionais |

### Serviços monitorados

- SEI: https://sei.ufla.br
- SIG: https://sig.ufla.br
- Campus Virtual: https://campusvirtual.ufla.br

A consulta retorna o estado de cada serviço, o código HTTP e o tempo de resposta.

## 3. Execução local

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a aplicação:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

A documentação interativa estará disponível em:

http://localhost:8000/docs

## 4. Testes automatizados

Execute:

```bash
pytest -v
```

## 5. Construção e execução com Docker

Construa a imagem:

```bash
docker build -t ufla-service-monitor:1.0 .
```

Execute o container:

```bash
docker run -d --name ufla-monitor -p 8001:8000 ufla-service-monitor:1.0
```

Acesse:

http://localhost:8001

## 6. Orquestração de containers

O projeto disponibiliza arquivos de configuração para implantação nos seguintes ambientes:

- Kubernetes: diretório `k8s/`.
- HashiCorp Nomad: diretório `nomad/`.

## 7. Integração e entrega contínuas (CI/CD)

O pipeline será implementado com GitHub Actions, contemplando as seguintes etapas:

1. **Test:** execução dos testes automatizados.
2. **Build:** construção da imagem Docker.
3. **Deploy:** implantação automatizada da aplicação.

## 8. Execução e avaliação

Projeto desenvolvido individualmente como atividade prática da disciplina DevOps.

Universidade Federal de Lavras (UFLA).
