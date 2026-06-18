# Desplegament amb clasp (una ordre)

`clasp` és l'eina oficial de Google per pujar codi a Apps Script des del terminal.
Necessites **Node.js** instal·lat.

## Fitxers d'aquesta carpeta

- `Codi.js` — codi del servidor (menú + diàleg + web app). clasp el converteix a `.gs`.
- `Dashboard.html` — el dashboard sencer.
- `appsscript.json` — manifest del projecte.
- `.claspignore` — limita la pujada a aquests tres fitxers.

## Passos (la primera vegada)

```bash
# 1. Instal·la clasp (un sol cop a l'ordinador)
npm install -g @google/clasp

# 2. Inicia sessió amb el teu compte de Google Workspace (s'obre el navegador)
clasp login

# 3. Des d'AQUESTA carpeta, crea el projecte lligat a un full nou
cd clasp
clasp create --title "Dashboard de Notes" --type sheets

# 4. Puja els fitxers
clasp push
```

`clasp create` genera un fitxer `.clasp.json` amb l'identificador del projecte
i un Google Sheets nou a la teva unitat. `clasp push` hi puja el codi.

## Obrir-ho

```bash
clasp open            # obre l'editor d'Apps Script
clasp open --addon    # obre el full vinculat
```

Al full vinculat: recarrega → menú **📊 Dashboard de Notes → Obrir dashboard**.

## Web app (imprimir / exportar sense límits)

```bash
clasp deploy --description "Dashboard web app"
```

Després, a l'editor (`clasp open`): **Desplegar → Gestionar desplegaments**,
edita el desplegament, tria **Aplicació web** i copia l'URL.
(El primer cop és més còmode fer aquest pas des de la interfície web.)

## Actualitzar més endavant

Edita els fitxers d'aquesta carpeta i torna a executar:

```bash
clasp push
```
