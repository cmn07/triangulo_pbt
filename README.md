# Triangle Classifier — Pytest vs Property-Based Testing

Projeto desenvolvido para a disciplina de Engenharia de Software 2 com o objetivo de comparar:

- Testes tradicionais com `pytest`
- Property-Based Testing (PBT) com `Hypothesis`

O sistema classifica triângulos em diferentes categorias e demonstra como o PBT pode validar propriedades matemáticas automaticamente através da geração de múltiplos casos de teste.

---

# Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/cmn07/triangulo_pbt
cd pbt_test
```

---

## 2. Crie um ambiente virtual

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```
