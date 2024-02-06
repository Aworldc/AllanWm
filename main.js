import { app, BrowserWindow, screen } from 'electron'

app.whenReady().then(() => {
    const { width, height } = screen.getPrimaryDisplay().workAreaSize

    let window = new BrowserWindow({
        width,
        height,
        frame: false,
        thickFrame: false,
        resizable: false,
        skipTaskbar: true
    })

    window.loadFile('index.html')
    window.setMenu(null)

    window.on('minimize', () => {
        window.restore()
    })
})
