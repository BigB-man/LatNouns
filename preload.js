window.addEventListener('DOMContentLoaded', () => {
  const replaceText = (selector, text) => {
    const element = document.getElementById(selector)
    if (element) element.innerText = text
  }
  for (const dependency of ['chrome', 'node', 'electron']) {
    replaceText(`${dependency}-version`, process.versions[dependency])
  }
  //document.getElementById('path').innerText = 'cheese'
  //const storage = require('electron-json-storage');
  //const dataPath = storage.getDataPath();
  localStorage.setItem("myCat", "Tom");
  const cat = localStorage.getItem("myCat");
  document.getElementById('path').innerText = cat;
  const defaultDataPath = storage.getDefaultDataPath()
  document.getElementById('path').innerText = defaultDataPath;
  
  
})