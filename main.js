var text = "";

const { app, BrowserWindow, Menu, ipcMain } = require('electron');
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
  const menu = Menu.buildFromTemplate([
    
    {
      label: app.name,
      submenu: [
        {
          click: () => win.webContents.send('update-counter', 1),
          label: 'Increment'
        },
        {
          click: () => win.webContents.send('update-counter', -1),
          label: 'Decrement'
        },
        {
          click:settingsTab,
          label: 'Settings'
        }
      ]
    }

  ])

  Menu.setApplicationMenu(menu)
  win.loadFile('index.html')
}
function settingsTab(){
  const settingsTab = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })
  settingsTab.loadFile('settings.html')
}
// ...
app.whenReady().then(() => {
  ipcMain.on('counter-value', (_event, value) => {
    console.log(value) // will print value to Node console
  })
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
})
