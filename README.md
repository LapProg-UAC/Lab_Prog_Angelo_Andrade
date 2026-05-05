# Projeto: Geração de Receitas Médicas e Classificação de Interações Medicamentosas

Projeto desenvolvido na disciplina de **Laboratório de Programação (LP)**.
O objetivo é gerar prescrições médicas aleatórias para utentes e calcular o risco de interação medicamentosa com base numa matriz de interações criada automaticamente em Excel.

---

## 🎯 Objetivos da Tarefa

O projeto cumpre os seguintes requisitos:

* Processamento de ficheiros **TXT**, **XLSX** e **JSON**
* Utilização dos módulos:

  * `random`
  * `json`
  * `sys`
  * `openpyxl`
* Uso de estruturas de dados mutáveis e imutáveis
* Geração e leitura de ficheiros Excel
* Abordagem de **decomposição funcional**
* Tratamento de exceções
* Comentários em **docstring**

---

## 📂 Estrutura do Projeto

```bash
interacoes-medicamentosas/
│
├── data/
│   ├── nomesP.txt
│   ├── apelidos.txt
│   ├── medicamentos.txt
│   ├── prescricoes.json
│   └── matrizMed.xlsx
│
├── src/
│   └── matrizmed.py
│
├── README.md
```

---

## ⚙️ Funcionamento do Programa

O programa realiza os seguintes passos:

1. Lê ficheiros de texto:

   * `nomesP.txt` — lista de nomes próprios
   * `apelidos.txt` — lista de apelidos
   * `medicamentos.txt` — lista de medicamentos disponíveis

2. Gera automaticamente um ficheiro Excel:

   * `matrizMed.xlsx`
   * Cada célula representa o nível de interação entre dois medicamentos
   * Valores variam de **0 (sem interação)** até **6 (interação elevada)**

3. Cria prescrições médicas aleatórias:

   * Cada utente recebe entre **2 e 4 medicamentos**
   * É calculado o risco total de interação

4. Classifica o risco:

   * `< 15` → **Interação medicamentosa segura**
   * `>= 15` → **Interação medicamentosa não segura**

5. Guarda todas as prescrições:

   * `prescricoes.json`

---

## ▶️ Como executar

Certifique-se de que tem Python instalado (>= 3.10).

```bash
python src/matrizmed.py
```

---

## 📄 Exemplo de saída

```json
{
  "utente": "João Silva",
  "medicamentos": ["Aspirina", "Ibuprofeno"],
  "risco_total": 18,
  "classificacao": "Interação medicamentosa não segura"
}
```
