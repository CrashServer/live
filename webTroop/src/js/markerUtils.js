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
      switch (color.toLowerCase()) {
        case "red":
          color = "var(--col-full-red)";
          break;
        case "green":
          color = "var(--col-full-green)";
          break;
        case "blue":
          color = "var(--col-full-blue)";
          break;
        default:
          break;
      }
      ychat.push([{ text: txt, userName: userName, userColor: color, line: line+1 }]); // Ajouter le message
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
  },

  // reset the ymarkers
  resetMarkers: function(ymarkers) {
    ymarkers.delete(0, ymarkers.length);
  },


};