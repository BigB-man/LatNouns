const counter = document.getElementById('counter')

window.electronAPI.handleCounter((event, value) => {
  const oldValue = Number(counter.innerText)
  const newValue = oldValue + value
  counter.innerText = newValue
  event.sender.send('counter-value', newValue)
})

const addbutton = document.getElementById('add')
const subtractbutton = document.getElementById('subtract')
addbutton.addEventListener('click', () => {
    const oldValue = Number(counter.innerText)
    const newValue = oldValue + 1
    counter.innerText = newValue
    event.sender.send('counter-value', newValue)
})
subtractbutton.addEventListener('click', () => {
    const oldValue = Number(counter.innerText)
    const newValue = oldValue - 1
    counter.innerText = newValue
    event.sender.send('counter-value', newValue)
})