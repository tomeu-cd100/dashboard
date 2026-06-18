# Dashboard de Notes a Google Workspace

Versió per executar dins de Google Workspace amb Apps Script.
Arrenca **buida**: el tutor hi puja el seu Excel de notes i el dashboard es genera.
Tot el processament és **al navegador**: cap dada d'alumnes va a cap servidor.

## Fitxers

- `Codi.gs` — codi del servidor (menú, diàleg i punt d'entrada web app).
- `Dashboard.html` — el dashboard sencer (sense dades; es carreguen per pujada).
- `appsscript.json` — manifest del projecte (opcional).

## Instal·lació (una vegada)

1. Obre (o crea) un **Google Sheets** al teu Workspace.
2. Menú **Extensions → Apps Script**.
3. Al projecte que s'obre:
   - Esborra el contingut de `Code.gs` i enganxa-hi el de **`Codi.gs`**.
   - **+ → HTML** → anomena'l **`Dashboard`** (sense `.html`) i enganxa-hi **`Dashboard.html`**.
4. **Desa** (💾).

---

## Opció A · Des del full (menú) — la més senzilla

1. Torna al full i **recarrega la pàgina**.
2. Apareix el menú **📊 Dashboard de Notes → Obrir dashboard**.
3. La primera vegada, **autoritza** el script (és normal).
4. S'obre el dashboard en un diàleg → **puja el teu Excel**.

> Limitació: dins del diàleg de Sheets, imprimir i exportar CSV poden estar
> restringits. Si els necessites, usa l'opció B.

## Opció B · Web app (recomanada per a imprimir / exportar)

1. A l'editor d'Apps Script: **Desplegar → Nou desplegament**.
2. Tipus: **Aplicació web**.
3. Executa com a **Jo**; Qui hi té accés: **Qualsevol de l'organització** (o segons calgui).
4. **Desplegar** → copia l'**URL de l'aplicació web**.
5. Obre l'URL → **puja el teu Excel**. Aquí imprimir, exportar CSV i copiar funcionen sense restriccions.

Aquest enllaç es pot afegir a Google Sites, a un marcador o compartir amb l'equip.

---

## Recomanacions

- Funciona millor a **Chrome** (la lectura de l'Excel usa APIs modernes del navegador).
- Per actualitzar el dashboard: torna a generar `Dashboard.html` i enganxa'l al fitxer `Dashboard`.
- Si has fet servir la web app i en canvies el codi, fes **Desplegar → Gestionar desplegaments → edita → Versió nova**.
