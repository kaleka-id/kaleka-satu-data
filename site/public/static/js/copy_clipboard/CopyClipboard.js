const copyButton = [...document.getElementsByClassName('copy-button')]

let previous = null

copyButton.forEach(btn => btn.addEventListener('click', ()=>{
    const dataUrl = btn.getAttribute('data-url')
    navigator.clipboard.writeText(dataUrl)
    if(previous){
        previous.textContent = 'Salin Referensi'
        previous.className = 'btn btn-secondary'
    }
    previous = btn
    btn.textContent = 'Tersalin'
    btn.className = 'btn btn-success'
}))