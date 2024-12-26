import { chatUtils } from './chatUtils.js';

export const markerUtils = {
  setMarker: function(cm, color = "", txt = "", awareness, ymarkers, ychat) {
    const line = cm.getCursor().line;
    const info = cm.lineInfo(line);
    if (info.handle.gutterClass != null && info.handle.gutterClass.includes(`line${color}`)) {
      // find the marker in the Y.Array and remove it
      const markerArray = ymarkers.toArray();
      if (markerArray.length === 0) {
        return;
      }
      const markerToremove = markerArray.findIndex((i) => i.line === line);
      ymarkers.delete(markerToremove, 1);
    } else {
      const userState = awareness.getLocalState();
      const userName = userState?.user?.name || 'Anonymous';
      ymarkers.push([{ line, color, text: txt, userName: userName }]); // Ajouter le marqueur au Y.Array
      ychat.push([{ text: txt, userName: userName, userColor: color }]);
    }
  },

  applyMarker: function(cm, line, color) {    
    cm.removeLineClass(line, "gutter");
    cm.removeLineClass(line, "background");
    cm.addLineClass(line, "gutter", `line${color}`);
    cm.addLineClass(line, "background", `line${color}`);
  },

  removeMarker: function(cm, line) {
    cm.removeLineClass(line, "gutter");
    cm.removeLineClass(line, "background");
  }
};