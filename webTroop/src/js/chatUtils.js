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
      if (cm.openDialog) {
        cm.openDialog(this.makePrompt(msg), f, {bottom: true});
      } else {
        f(prompt(msg, ""));
      }
    },
  
    flashChatPanel: function() {
      this.chatPanel.classList.add("flash");
      setTimeout(() => this.chatPanel.classList.remove("flash"), 500);
    },

    insertChatMessage: function(cm, text, userName, userColor) {
        const line = cm.getCursor().line
        const chatMessage = document.createElement("div")
        chatMessage.textContent += `${line+1}| ${userName}: ${text}`
        chatMessage.style.color = userColor
        this.chatPanel.insertBefore(chatMessage, this.chatPanel.firstChild);
        this.flashChatPanel();
    }
  };