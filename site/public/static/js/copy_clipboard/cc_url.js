const copyButton = [...document.getElementsByClassName('copy-button')]

let previous = null

copyButton.forEach(btn => btn.addEventListener('click', ()=>{
    const dataUrl = btn.getAttribute('data-url')
    navigator.clipboard.writeText(dataUrl)
    if(previous){
        previous.textContent = 'Copy URL'
        previous.className = 'btn btn-outline-secondary'
    }
    previous = btn
    btn.textContent = 'Tersalin'
    btn.className = 'btn btn-secondary'
}))