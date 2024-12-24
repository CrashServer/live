import { chatUtils } from './chatUtils.js';

export const markerUtils = {
  setMarker: function(cm, color = "", txt = "", awareness, ymarkers, ychat) {
    const line = cm.getCursor().line;
    const info = cm.lineInfo(line);
    if (info.handle.gutterClass != null && info.handle.gutterClass.includes(`line${color}`)) {
      cm.removeLineClass(line, "gutter");
      cm.removeLineClass(line, "background");
    } else {
      cm.removeLineClass(line, "gutter");
      cm.removeLineClass(line, "background");
      cm.addLineClass(line, "gutter", `line${color}`);
      cm.addLineClass(line, "background", `line${color}`);
      const userState = awareness.getLocalState();
      const userName = userState?.user?.name || 'Anonymous';
    //   chatUtils.insertChatMessage(cm, txt, userName, color);
      ymarkers.push([{ line, color, text: txt, userName: userName }]); // Ajouter le marqueur au Y.Array
    //   ychat.push([{ txt, userName, color }]);
    }
  },

  applyMarker: function(cm, line, color, text) {
    cm.addLineClass(line, "gutter", `line${color}`);
    cm.addLineClass(line, "background", `line${color}`);
    // chatUtils.insertChatMessage(cm, text, "System", color);
  }
};