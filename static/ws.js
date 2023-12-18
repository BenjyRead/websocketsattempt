socket = io('http://localhost:5000')


socket.on('connect', () => {console.log("WebSocket connection state:", socket.readyState)})

socket.on("message", (text) => {
    console.log(text)
})

sendbutton = document.getElementById("send")

sendbutton.addEventListener("click", () => {
    messagebox = document.getElementById("message")
    message = messagebox.value
    messagebox.value = ""
    socket.emit('message', message)
})
