# 🧲 Experimento de Stern-Gerlach (1922)

## Visão Geral

O experimento de Stern-Gerlach é um dos mais importantes da história da mecânica quântica. Ele forneceu a primeira evidência direta da **quantização do momento angular** e, posteriormente, levou à descoberta do **spin do elétron**.

---

## O Aparelho Experimental

```
Fonte de Ag → [Feixe] → Ímã não-uniforme → Detector
                       (campo magnético B)
```

### Componentes:
1. **Fonte (Source):** Forno que vaporiza átomos de prata (Ag)
2. **Colimador:** Cria um feixe estreito e paralelo de átomos
3. **Ímã:** Produz um campo magnético **não-uniforme** (gradiente ∂B/∂z)
4. **Detector:** Placa que registra onde os átomos aterrissam

---

## Resultados Observados

### Sem Campo Magnético
```
Detector:  ─────────── [linha única] ───────────
```
- O feixe forma uma única linha no detector
- Comportamento clássico esperado ✓

### Com Campo Magnético
```
Detector:     ●●●●●  (spin ↑)
              ─────
              ●●●●●  (spin ↓)
```
- A linha se divide em **exatamente dois pontos**
- **Não** uma faixa borrada (como esperado classicamente)
- **Não** três, cinco ou cem pontos
- Exatamente **dois**

---

## A Contradição com a Física Clássica

### Previsão Clássica:
- Átomos de Ag possuem momento magnético **μ** (como pequenos ímãs)
- Em um feixe aleatório, **μ** aponta em todas as direções
- O campo não-uniforme deveria deflectir cada átomo proporcionalmente à componente de **μ** ao longo de B
- **Resultado esperado:** uma faixa contínua borrada no detector

### Resultado Real:
- Apenas **dois** pontos discretos
- Isso só é possível se o momento angular for **quantizado**

---

## Interpretação Quântica

### Número Quântico Magnético (mₗ)
- A componente z do momento angular orbital é quantizada:
  ```
  Lz = mₗ · ℏ,  onde mₗ = -l, -l+1, ..., l-1, l
  ```
- Para l=1: mₗ = -1, 0, +1 → deveria haver 3 pontos
- Mas o experimento mostrou apenas **2 pontos**

### A Descoberta do Spin
- Em 1925, Uhlenbeck e Goudsmit propuseram o **spin intrínseco**
- O elétron tem spin s = 1/2
- Componente z: Sz = ±ℏ/2
- **Isso explica os 2 pontos!**

---

## Fórmulas Importantes

### Momento Angular de Spin
```
|S| = √(s(s+1)) · ℏ = √(3/4) · ℏ = (√3/2)ℏ
```

### Componente Z
```
Sz = ms · ℏ,  onde ms = ±1/2
```

### Momento Magnético de Spin
```
μs = -gs · (e/2me) · S

Onde:
- gs ≈ 2.0023 (fator g do elétron)
- e = carga do elétron
- me = massa do elétron
```

### Deflexão no Campo Não-Uniforme
```
Fz = μz · (∂B/∂z)

Para Sz = +ℏ/2: deflexão para cima
Para Sz = -ℏ/2: deflexão para baixo
```

---

## Implicações Fundamentais

1. **Quantização é real:** grandezas físicas podem só assumir valores discretos
2. **Spin não é rotação clássica:** é uma propriedade intrínseca sem análogo clássico
3. **Dois níveis naturais:** o spin-1/2 é o sistema de dois níveis mais fundamental
4. **Base da computação quântica:** |↑⟩ = |0⟩, |↓⟩ = |1⟩

---

## Referências

- Stern, O. & Gerlach, W. (1922). *Zeitschrift für Physik*, 9, 349-352
- Uhlenbeck, G. & Goudsmit, S. (1925). *Naturwissenschaften*, 13, 953
- Griffiths, D.J. *Introduction to Quantum Mechanics*, Cap. 4
