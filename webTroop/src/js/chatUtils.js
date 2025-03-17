export const chatUtils = {
    chatPanel: document.getElementById('chat'),

    makePrompt: function(msg) {
      const fragment = document.createDocumentFragment();
      const input = document.createElement("input");
      input.setAttribute("type", "text");
      input.style.width = "10rem";
      fragment.appendChild(document.createTextNode(msg + ">> "));
      fragment.appendChild(input);
      return fragment;
    },
  
    getChat: function(cm, msg, f) {
      const cursor = cm.getCursor();
      const line = cursor.line + 1;
      if (cm.openDialog) {
        cm.openDialog(this.makePrompt(msg), (input) => f(input, line), {bottom: true});
      } else {
        const input = prompt(msg, "");
        f(input, line);
      }
    },
  
    flashChatPanel: function() {
      this.chatPanel.classList.add("flash");
      setTimeout(() => this.chatPanel.classList.remove("flash"), 500);
    },

    insertChatMessage: function(cm, text, userName, userColor, line) {
        // const line = cm.getCursor().line
        const chatMessage = document.createElement("div")
        if (!line){
            line = 0;
        }
        chatMessage.textContent += `${line.toString().padStart(3, '0')}| ${userName}: ${text}`
        chatMessage.style.color = userColor
        this.chatPanel.insertBefore(chatMessage, this.chatPanel.firstChild);
        this.flashChatPanel();
    }
  };