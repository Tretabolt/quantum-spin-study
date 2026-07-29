# 🧪 Teste Visual de Spins em Cristais

## O Vídeo Original

O [Experimento de Stern-Gerlach](https://www.instagram.com/reel/DbWYozSTtPq/) mostra que o spin do elétron é quantizado — só existe ↑ ou ↓, nada no meio.

Com cristais comuns, dá pra perceber isso na prática!

---

## Montagem Simples (Sem Equipamento)

```
     fixar no teto/mesa
          │
          │ fio (30-50cm)
          │
       [cristal]
          │
     ┌────┴────┐
     │  ÍMÃ    │
     └─────────┘
```

### Materiais
- Ímã forte (geladeira ou neodímio)
- Fio fino (costura, nylon, seda)
- Cristais variados

### Passo a Passo
1. Amarra o cristal no fio
2. Pendura firme (sem vento)
3. Aproxima o ímã por baixo (2-3 cm)
4. Observa o movimento

---

## Resultados

| Cristal | O que acontece | Tipo | Spins? |
|---------|----------------|------|--------|
| Quartzo (SiO₂) | Nada / repulsão fraca | Diamagnético | ❌ |
| Sal grosso (NaCl) | Nada / repulsão fraca | Diamagnético | ❌ |
| Açúcar | Nada / repulsão fraca | Diamagnético | ❌ |
| Pirita (FeS₂) | Atração fraca | Paramagnético | ✅ Fe²⁺ |
| Granada | Atração moderada | Paramagnético | ✅ Fe³⁺ |
| Magnetita (Fe₃O₄) | Atração FORTE | Ferromagnético | ✅✅✅ |

---

## Por Que Acontece?

### Cristais Diamagnéticos (quartzo, sal, açúcar)
- Todos os elétrons emparelhados
- Nenhum spin desemparelhado
- Campo magnético gera fraca repulsão

### Cristais Paramagnéticos (pirita, granada)
- Contêm impurezas com spins desemparelhados
- Fe²⁺ (4 elétrons livres) ou Fe³⁺ (5 elétrons livres)
- Campo magnético atrai

### Cristais Ferromagnéticos (magnetita)
- Spins alinhados em domínios
- Atração muito forte
- Pode magnetizar outros materiais

---

## Relação com Stern-Gerlach

O vídeo mostra:
- Átomos passam pelo ímã → dividem em 2 feixes
- Spin é quantizado: só ↑ ou ↓

Nos cristais:
- Impurezas têm spins desemparelhados
- Esses spins geram momento magnético
- O ímã detecta isso (atração/repulsão)

**Você está medindo diretamente a quantização do momento angular!**

---

## Dicas

- **Quartzo com impurezas** (ametista, citrino) pode ter Fe³⁺ → atrai
- **Cristais de loja** costumam ter mais impurezas que os sintéticos
- **Magnetita** é o controle positivo (sempre atrai)
- **Sal de cozinha** é o controle negativo (nunca atrai)

---

## Próximo Nível

Quer medir com precisão? Veja:
- [Guia Prático Completo](docs/08-guia-pratico-experimento.md)
- [Lista de Materiais](src/experimentos/lista_materiais.md)
- [Análise de Dados Python](src/experimentos/analise_dados.py)
