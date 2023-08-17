const setButton = document.getElementById('btn')
const titleInput = document.getElementById('title')
setButton.addEventListener('click', () => {
  const title = titleInput.value
  window.electronAPI.setTitle(title)
  window.replaceText(`title`, title)
  //window.setBackgroundColor('#ff00a3')
})