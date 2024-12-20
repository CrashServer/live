// Redimensionner le panneau de logs
  const separator = document.getElementById('separator')
  const logs = document.getElementById('logs')
  const editorContainer = document.getElementById('editor-container')

  let isResizing = false

  separator.addEventListener('mousedown', (e) => {
    isResizing = true
    document.addEventListener('mousemove', resize)
    document.addEventListener('mouseup', stopResize)
  })

  function resize(e) {
    if (isResizing) {
      const containerHeight = editorContainer.clientHeight
      const newLogsHeight = containerHeight - e.clientY
      logs.style.height = `${newLogsHeight}px`
      editor.getWrapperElement().style.height = `${containerHeight - newLogsHeight - separator.clientHeight}px`
      editor.refresh()
    }
  }

  function stopResize() {
    isResizing = false
    document.removeEventListener('mousemove', resize)
    document.removeEventListener('mouseup', stopResize)
  }