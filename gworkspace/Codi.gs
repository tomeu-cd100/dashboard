/**
 * Dashboard de Notes — Google Workspace (Apps Script)
 * Script lligat a un full de Google Sheets.
 * Afegeix un menú que obre el dashboard en un diàleg.
 * Les notes es carreguen pujant l'Excel des de dins del propi dashboard.
 */

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('📊 Dashboard de Notes')
    .addItem('Obrir dashboard', 'obrirDashboard')
    .addToUi();
}

function obrirDashboard() {
  var html = HtmlService.createHtmlOutputFromFile('Dashboard')
    .setWidth(1500)
    .setHeight(900)
    .setTitle('Dashboard de Notes');
  SpreadsheetApp.getUi().showModalDialog(html, 'Dashboard de Notes');
}

/**
 * Punt d'entrada com a WEB APP (Desplegar → Nou desplegament → Aplicació web).
 * Es serveix a pàgina completa, sense les limitacions del diàleg de Sheets
 * (impressió, exportació CSV i porta-retalls funcionen sense restriccions).
 */
function doGet() {
  return HtmlService.createHtmlOutputFromFile('Dashboard')
    .setTitle('Dashboard de Notes')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}
