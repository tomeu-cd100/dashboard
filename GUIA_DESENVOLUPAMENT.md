# Dashboard de Notes — Guia de Desenvolupament

---

## Punt de partida
- Full Excel de notes trimestrals (ESO, escala NA / AS / AN / AE)
- Objectiu: eina visual per al tutor/a sense coneixements tècnics

---

## Fase 1 · Lectura automàtica de l'Excel
- Script Python que detecta grups, matèries i alumnes
- Processament 100 % al navegador — cap dada surt de l'ordinador

## Fase 2 · Primer dashboard visual
- Distribució global de notes (gràfic de donut)
- Rànquing d'alumnes per mitjana
- Anàlisi per matèria amb barres apilades i percentatges

## Fase 3 · Alumnes en risc i seguiment
- Criteri de seguiment: 3 o més matèries no assolides
- Llistat d'alumnes a tocar d'aprovar (1–2 NA)
- Mapa de calor alumnes × matèries

## Fase 4 · Millores pedagògiques (primera ronda)
- Agrupació per **àmbits competencials** (LOMLOE)
- Distinció individual vs. sistèmic (≥ 40 % NA = tema de junta)
- Perfils de l'alumnat: En risc · Fràgil · Consolidat · Excel·lent
- Propostes de grups de reforç per matèria

## Fase 5 · Eines de gestió i accessibilitat
- Pujada d'Excel directament al navegador (sense instal·lació)
- Botó d'impressió del dashboard i de la fitxa individual
- Exportació CSV per a Excel
- Mode daltònic (paleta Okabe-Ito)

## Fase 6 · Vistes per moment pedagògic
- Vista **Junta** · Vista **Tutoria** · Vista **Dades**
- Resum executiu copiable per a l'acta
- Objectius de millora amb seguiment per trimestre
- Evolució entre trimestres (per alumne i per àmbit)

## Fase 7 · Integració a Google Workspace
- Desplegament com a web app d'Apps Script
- Accés per a tots els tutors del domini (@conselldecent.com)
- Enllaç permanent — s'actualitza sense canviar la URL

## Fase 8 · Versió 3 · Eina de junta d'avaluació
- **Guió de sessió temporitzat** (Diagnòstic 20 % · Causes 20 % · Acords 60 %)
  - Fases clicables per saltar manualment
- **Camps de context per alumne**: clima d'aula, barreres, actitud
- **Marca NEE / NESE** visible a la fitxa
- **Plantilla d'acords estructurada**: mesura · responsable · data de revisió
- Mode clar / fosc compatible amb mode daltònic

---

## Principis tècnics transversals
- Tot el processament és **local** — zero servidors, zero núvol de dades
- HTML autocontingut, sense dependències externes
- Compatible amb Chrome, Edge i Firefox
- Imprimir fitxa individual (orientada a famílies)

---

*Desenvolupat amb Claude Code · Institut Consell de Cent · 2025–2026*
