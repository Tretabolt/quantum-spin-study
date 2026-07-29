# 🔬 Medindo Spins em Cristais

## Visão Geral

Sim, é possível medir spins de um cristal comum! Existem várias técnicas, cada uma com suas vantagens.

---

## 1. Ressonância Paramagnética Eletrônica (EPR/ESR)

A técnica mais direta para medir spins eletrônicos.

### Princípio:
```
Cristal em campo B₀ + radiação de micro-ondas
         ↓
Quando hν = gμB·B₀ → ressonância
         ↓
Os spins absorvem energia e transicionam
         ↓
Detector mede a absorção
```

### O que você obtém:
- **Posição do pico** → fator g (identifica o tipo de spin)
- **Largura do pico** → interações spin-spin
- **Estrutura fina** → acoplamento spin-órbita
- **Estrutura hiperfina** → interação com núcleos vizinhos

### Equipamento:
- Espectrômetro EPR (custo: ~$50k-$500k)
- Frequência típica: ~9.5 GHz (banda X)
- Campo magnético: ~0.3-0.5 T

---

## 2. Ressonância Magnética Nuclear (NMR)

Para spins nucleares (¹H, ¹³C, ²⁹Si, etc.).

### Aplicações em cristais:
- Determinar estrutura cristalina
- Medir ambientes químicos dos átomos
- Detectar defeitos e impurezas
- Estudar dinâmica molecular

### Equipamento:
- NMR benchtop (~$50k-$100k)
- NMR de alto campo (~$500k+)

---

## 3. Difração de Nêutrons

### Princípio:
```
Nêutrons têm spin 1/2
         ↓
Interagem com spins dos átomos no cristal
         ↓
Padrão de difração revela:
├── Posições atômicas
├── Ordenamento magnético (ferro/antiferromagnético)
└── Excitações de spin (magnons)
```

### Requisitos:
- Reator nuclear ou spallation source como fonte de nêutrons
- Acesso a grandes instalações (ILL, ORNL, IFE)

---

## 4. Magnetometria com NV Center (Diamante)

Técnica moderna e muito sensível.

### Setup:
```
Ponta de diamante com centro NV (nitrogênio-vacância)
         ↓
Posicionada a ~nm da superfície do cristal
         ↓
Laser + micro-ondas para leitura
         ↓
Sensibilidade: detecta spin individual!
```

### Aplicações:
- Imagem de domínios magnéticos
- Medição de campo magnético local
- Detecção de spins de defeitos em cristais

---

## 5. Exemplo Prático: Medindo Spins de Quartzo (SiO₂)

### Equipamento necessário:
- Espectrômetro EPR (custo: ~$50k-$500k)
- ou NMR benchtop (~$50k-$100k)
- ou SQUID magnetômetro (~$200k+)

### Procedimento EPR:
```
1. Preparar amostra (pó ou cristal, ~mg)
2. Colocar em tubo de quartzo
3. Inserir na cavidade de micro-ondas (~9.5 GHz, banda X)
4. Resfriar (77K ou 4K para melhor sinal)
5. Sweep do campo magnético (0-0.5 T)
6. Detectar absorção de micro-ondas
7. Analisar espectro
```

### O que você vai ver:
- **Quartzo puro:** sinal fraco (SiO₂ é diamagnético)
- **Quartzo com impurezas** (Fe³⁺, Mn²⁺, etc.): picos claros
- **Quartzo irradiado:** centros E' (oxigênio com elétron preso)

---

## Técnicas Comparadas

| Técnica | Sensibilidade | Resolução Espacial | Custo |
|---------|---------------|-------------------|-------|
| EPR/ESR | ~10⁹ spins | ~mm | $50k-$500k |
| NMR | ~10¹⁵ spins | ~μm | $50k-$1M |
| Difração de Nêutrons | Bulk | ~Å | Acesso a instalação |
| NV Center | **Spin individual** | ~nm | $100k-$500k |
| SQUID | ~10⁵ spins | ~μm | $200k+ |

---

## Referências

- Weil, J.A. & Bolton, J.R. (2007). *Electron Paramagnetic Resonance*
- Schweiger, A. & Jeschke, G. (2001). *Principles of Pulse Electron Paramagnetic Resonance*
- Degen, C.L. et al. (2017). "Quantum sensing". *Reviews of Modern Physics*
