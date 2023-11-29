const counter = document.getElementById('counter')
const addbutton = document.getElementById('add')
const subtractbutton = document.getElementById('subtract')
const settings = document.getElementById('settings')
const {ipcMain} = require('electron');
function chez(){

}
 
subtractbutton.addEventListener('click', function () {
   var arg = "secondparam";
   // Send the info to the main process. We can pass any arguments as the second parameter.
   ipcRenderer.send("btnclick", arg); // ipcRenderer.send will pass the information to the main process
 });
// subtractbutton.addEventListener('click', () => {
//     window.electronAPI.openSettings(chez)
    
// })
