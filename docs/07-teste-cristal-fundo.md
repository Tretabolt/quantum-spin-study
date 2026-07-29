# 🔬 Teste de Fundo de Cristal com Spins

## Objetivo

Detectar e medir a presença de **spins eletrônicos** em cristais comuns usando um setup simples e acessível.

---

## O que é "Fundo de Cristal"?

O "fundo" (background) de um cristal é o sinal que vem das **impurezas paramagnéticas** presentes naturalmente:

- **Quartzo (SiO₂):** contém traços de Fe³⁺, Mn²⁺, Al³⁺
- **Sal de cozinha (NaCl):** pode conter Fe³⁺ e outros metais de transição
- **Açúcar (sacarose):** radicais livres se irradiado
- **Safira (Al₂O₃):** Cr³⁺ (rubis), Fe³⁺/Ti⁴⁺ (safiras azuis)
- **Calcita (CaCO₃):** Mn²⁺ como impureza comum

Esses spins geram um **sinal magnético mensurável**!

---

## Método 1: Balança de Susceptibilidade Magnética (Gouy)

### Princípio
```
Cristal paramagnético → atraído por campo magnético
Cristal diamagnético → repelido por campo magnético

A força é proporcional à susceptibilidade magnética (χ)
```

### Materiais Necessários

| Item | Custo Estimado | Onde Encontrar |
|------|----------------|----------------|
| Balança de precisão (0.01g) | R$ 50-150 | Mercado Livre, Amazon |
| Ímãs de neodímio (2x) | R$ 30-80 | Mercado Livre |
| Suporte/argola | R$ 20-50 | Ferragem |
| Fio de nylon/seda | R$ 5 | Armarinho |
| Régua/microscópio | R$ 20-100 | Papelaria |
| Cristais para testar | R$ 20-50 | Mineralogia, lojas de cristal |

### Cristais para Testar

```
Cristal          | Tipo Esperado    | Sinal Esperado
-----------------|------------------|----------------
Quartzo (SiO₂)  | Diamagnético     | Fraca repulsão
Sal (NaCl)       | Diamagnético     | Fraca repulsão
Açúcar           | Diamagnético     | Fraca repulsão
Magnetita        | Ferromagnético   | Forte atração
Granada          | Paramagnético    | Atração moderada
Pirita (FeS₂)   | Paramagnético    | Atração moderada
Turmalina        | Piroelétrica     | Efeito variado
```

### Procedimento

```
1. Preparar a amostra:
   - Pesar o cristal (m₀)
   - Medir dimensões (comprimento L)

2. Montar o setup:
   - Suspender o cristal com fio entre os ímãs
   - Posicionar ímãs acima e abaixo
   - Distância: ~2-5 cm do cristal

3. Medir com campo:
   - Aplicar campo magnético (aproximar ímãs)
   - Pesar novamente (m₁)
   - Calcular Δm = m₁ - m₀

4. Repetir para cada cristal
5. Registrar resultados
```

### Cálculo

```
Susceptibilidade volumétrica (χ):

χ = (2·Δm·g) / (A·μ₀·H²)

Onde:
- Δm = variação de massa (kg)
- g = 9.81 m/s²
- A = área da seção do cristal (m²)
- μ₀ = 4π×10⁻⁷ T·m/A
- H = campo magnético (A/m)
```

---

## Método 2: Ressonância Paramagnética (DIY EPR)

### Princípio
```
Campo magnético B₀ + micro-ondas
         ↓
Quando hν = g·μB·B₀ → ressonância
         ↓
Os spins absorvem energia
         ↓
Detector mede absorção
```

### Materiais para EPR Simplificado

| Item | Custo Estimado | Observação |
|------|----------------|------------|
| Magnetron de micro-ondas | R$ 100-200 | De micro-ondas velho |
| Guia de ondas | R$ 50-150 | Alumínio/cobre |
| Cavidade ressonante | R$ 100-300 | Custom (ver abaixo) |
| Detector de micro-ondas | R$ 50-200 | Diodo Schottky |
| Ímãs permanentes | R$ 100-300 | Neodímio (0.3-0.5T) |
| Multímetro | R$ 50-100 | Para leitura |

### Montagem da Cavidade

```
┌─────────────────────────────────────┐
│  Cavidade Ressonante (Modo TE₁₀₂)   │
│                                     │
│    ┌─────────────────────────┐      │
│    │                         │      │
│    │     ← Cristal →         │      │
│    │                         │      │
│    └─────────────────────────┘      │
│                                     │
│  Material: Alumínio ou cobre        │
│  Dimensões: ~10×5×3 cm             │
│  Frequência: ~2.45 GHz             │
└─────────────────────────────────────┘
```

### Procedimento EPR

```
1. Ligar o magnetron (CUIDADO: alta tensão!)
2. Alimentar a cavidade com micro-ondas
3. Posicionar o cristal dentro da cavidade
4. Aplicar campo magnético variável
5. Medir a potência refletida/transmitida
6. Procurar por absorção na frequência de ressonância

Frequência de ressonância:
f = (g·μB·B) / h

Para B = 0.35T e g = 2.0:
f ≈ 9.8 GHz (banda X)
```

---

## Método 3: Detecção Óptica de Spin (Faraday)

### Princípio
A polarização da luz rotaciona quando passa por um material com spins alinhados em campo magnético.

```
Luz polarizada → [Cristal + Campo B] → Analisador → Detector
                      ↓
              Rotação θ ∝ M (magnetização)
                      ↓
              M ∝ número de spins
```

### Materiais

| Item | Custo Estimado |
|------|----------------|
| Laser pointer | R$ 10-30 |
| Polarizador (2x) | R$ 20-50 |
| Fotodetector/LDR | R$ 10-30 |
| Multímetro | R$ 50-100 |
| Ímãs | R$ 50-100 |
| Cristal | R$ 20-50 |

### Montagem

```
[Laser] → [Polarizador 1] → [Cristal+Ímã] → [Polarizador 2] → [Detector]
     P₀         P₁              Campo B           P₂             I
```

### Procedimento

```
1. Alinhar laser e polarizadores
2. Cruzar polarizadores (P₁ ⊥ P₂) → mínimo de luz
3. Inserir cristal + campo magnético
4. Medir intensidade I com detector
5. Calcular rotação: θ = arcsin(√(I/I₀))
6. Repetir para diferentes cristais
```

---

## Experimento Prático Recomendado: Balança de Gouy

### Materiais Comprados

```python
materiais = {
    "Balança digital 0.01g": {"preco": 80, "onde": "Mercado Livre"},
    "Ímãs neodímio 50x20mm (2x)": {"preco": 60, "onde": "Mercado Livre"},
    "Suporte metálico": {"preco": 40, "onde": "Ferragem"},
    "Fio de nylon 0.3mm": {"preco": 5, "onde": "Armarinho"},
    "Tubo de ensaio": {"preco": 10, "onde": "Farmácia"},
    "Régua milimetrada": {"preco": 5, "onde": "Papelaria"},
    # Cristais
    "Quartzo natural (100g)": {"preco": 20, "onde": "Loja de cristais"},
    "Sal grosso (500g)": {"preco": 5, "onde": "Supermercado"},
    "Açúcar cristal (500g)": {"preco": 5, "onde": "Supermercado"},
    "Magnetita (50g)": {"preco": 30, "onde": "Loja mineralógica"},
    "Pirita (50g)": {"preco": 25, "onde": "Loja mineralógica"},
    "Granada (50g)": {"preco": 30, "onde": "Loja mineralógica"},
}

total = sum(item["preco"] for item in materiais.values())
print(f"Custo total estimado: R$ {total}")
# Saída: ~R$ 315
```

---

## Análise dos Resultados

### Tabela de Resultados Esperados

```
Cristal       | Δm (g)  | χ (10⁻⁶) | Tipo         | Spins
--------------|---------|-----------|--------------|--------
Quartzo       | -0.001  | -1.6      | Diamagnético | Nenhum
Sal (NaCl)    | -0.002  | -3.0      | Diamagnético | Nenhum
Açúcar        | -0.001  | -1.8      | Diamagnético | Nenhum
Granada       | +0.005  | +200      | Paramagnético| Fe³⁺
Pirita        | +0.003  | +50       | Paramagnético| Fe²⁺
Magnetita     | +0.500  | >>1000    | Ferromagnético| Fe₃O₄
```

### Interpretação

```
χ < 0 → Diamagnético (sem spins desemparelhados)
χ > 0 → Paramagnético (spins desemparelhados presentes)
χ >> 1 → Ferromagnético (ordenamento magnético)

Para cristais diamagnéticos:
- Todos os elétrons emparelhados
- Nenhum spin líquido
- Sinal muito fraco

Para cristais paramagnéticos:
- Impurezas com spins desemparelhados
- Sinal proporcional à concentração de impurezas
- Pode detectar ~10¹⁵ spins/g
```

---

## Segurança

⚠️ **CUIDADOS IMPORTANTES:**

1. **Ímãs de neodímio:** São muito fortes! Podem beliscar pele e estragar eletrônicos
2. **Micro-ondas (se usar EPR):** ALTA TENSÃO! Não abrir o magnetron
3. **Cristais:** Alguns podem ser tóxicos (não ingerir)
4. **Laser:** Não olhar diretamente no feixe

---

## Referências

- Kittel, C. *Introduction to Solid State Physics*
- Weil & Bolton. *Electron Paramagnetic Resonance*
- Cullity & Graham. *Introduction to Magnetic Materials*
