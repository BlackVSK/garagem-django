# Guia Completo de Testes com Pytest

Este repositório fornece um guia para uso do `pytest` em projetos Python, com foco especial em testes para aplicações Django utilizando o gerenciador de dependências [PDM](https://pdm.fming.dev/).

---

## 📁 Instalação

Instale o pytest e seus plugins:

```bash
pdm add -d pytest pytest-django
```

Configure o `pyproject.toml`:

```toml
[tool.pytest.ini_options]
DJANGO_SETTINGS_MODULE = "config.settings"
python_files = "tests/test_*.py"

[tool.pdm]
distribution = false
```

---

## ⚖️ Comandos Importantes

### Testes Unitários

```bash
pdm run pytest
```

Roda todos os testes no projeto.

```bash
pdm run pytest tests/test_modelo.py
```

Roda apenas o arquivo de teste especificado.

```bash
pdm run pytest -k nome_da_funcao
```

Roda testes que contenham "nome\_da\_funcao" no nome.

### Testes de Integração

Semelhantes aos testes unitários, mas incluem vários componentes:

```bash
pdm run pytest -m "integracao"
```

Com uso de markers:

```python
@pytest.mark.integracao
def test_exemplo():
    ...
```

### Testes de Sistema / Aceitação

Para testes ponta a ponta, use integração com frameworks como `Selenium` ou `Playwright`:

```bash
pdm add -d pytest-playwright
pdm run pytest --browser chromium
```

### Testes de Desempenho / Carga / Stress

Recomenda-se uso de ferramentas como `pytest-benchmark`:

```bash
pdm add -d pytest-benchmark
pdm run pytest --benchmark-only
```

### Testes de Segurança

Com ferramentas como `bandit` para análise estática:

```bash
pdm add -d bandit
pdm run bandit -r nome_do_projeto/
```

---

## ⚖️ Assertivas com `pytest`

### Mais comuns:

```python
assert a == b                      # igualdade
assert a != b                      # diferença
assert a > b, a < b, a >= b, etc.  # comparações
assert isinstance(obj, Tipo)      # tipo de dado
assert item in lista              # inclusão
assert not condicao               # negação
```

### Tratamento de exceções:

```python
import pytest

with pytest.raises(ValueError):
    funcao_que_gera_erro()
```

### Comparando coleções:

```python
assert lista1 == lista2
assert set(lista1) == set(lista2)
```

### Mensagem personalizada:

```python
assert valor == esperado, "Valor retornado está incorreto"
```

### Uso de `pytest.approx()` para floats:

```python
assert 0.1 + 0.2 == pytest.approx(0.3)
```

---

## 🔧 Outras funcionalidades úteis

### Verbosidade:

```bash
pdm run pytest -v
```

### Mostrar saída (print):

```bash
pdm run pytest -s
```

### Gerar relatório de cobertura:

```bash
pdm add -d pytest-cov
pdm run pytest --cov=nome_do_pacote
```

### Ignorar warnings:

```bash
pdm run pytest -p no:warnings
```

---

## 📈 Conclusão

Este guia cobre os principais recursos e comandos para executar uma bateria de testes completa com `pytest`. Recomendamos integrar isso a um CI/CD para execução automatizada.

Para mais informações, consulte a [documentação oficial do Pytest](https://docs.pytest.org/en/latest/).
