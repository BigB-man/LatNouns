var text = "";

const { app, BrowserWindow } = require('electron');
const storage = require('electron-json-storage');




// include the Node.js 'path' module at the top of your file
const path = require('path')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  win.loadFile('index.html')
}
// ...
app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
})

function addTo(){
  text = document.getElementById("typeMe").value;
}