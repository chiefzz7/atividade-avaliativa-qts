# 📦 Atividade Avaliativa - QTS (Testes com Pytest)

## 📌 Descrição

Este projeto foi desenvolvido como uma atividade avaliativa da disciplina de **Qualidade e Testes de Software (QTS)**.

O objetivo principal é aplicar conceitos de testes automatizados utilizando **pytest**, garantindo o funcionamento correto de funções relacionadas a um sistema simples de cantina.

---

## ⚙️ Funcionalidades

O sistema possui duas funções principais:

- `calcular_total(quantidade, valor_unitario)`  
  ➝ Calcula o valor total de um pedido

- `validar_pedido(item, quantidade, valor_unitario)`  
  ➝ Verifica se um pedido é válido

---

## 🧪 Testes Automatizados

Foram implementados **mínimo de 5 testes com pytest**, distribuídos conforme solicitado:

### ✔️ Organização dos testes

- Testes feitos para dar certo `main`
- Testes feitos para dar erro `feature/testes-cantina`

### ⚠️ Teste propositalmente com erro

Um dos testes foi criado **intencionalmente errado**, com o objetivo de:

- Simular falha no sistema
- Observar o comportamento do pytest
- **Sem uso de decorator de exceção (`pytest.raises`)**

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/chiefzz7/atividade-avaliativa-qts.git
```

### 2. Entrar na pasta e inicializar o UV e o Pytest

```bash
cd atividade-avaliativa-qts
uv init
uv add pytest
```

### 3. Rodar o projeto com o Pytest

```bash
uv run pytest
```