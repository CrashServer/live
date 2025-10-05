export function setupConfigPanel(awareness, editor, otherEditor) {
    const configButton = document.getElementById('configButton');
    const configPanel = document.getElementById('configPanel');
    const userNameInput = document.getElementById('userName');
    const userColorInput = document.getElementById('userColor');
    const fontSelect = document.getElementById('fontSelect');
    const fontSizeSlider = document.getElementById('fontSizeSlider');
    const fontSizeValue = document.getElementById('fontSizeValue');
    const fontInterfaceSizeSlider = document.getElementById('fontInterfaceSizeSlider');
    const fontInterfaceSizeValue = document.getElementById('fontInterfaceSizeValue');
    const modal = document.getElementById("shortcutsModal");
    const modalbtn = document.getElementById("openModalBtn");
    const closeModal = document.getElementById("closeModal");
    const buttonValidatePlayerName = document.getElementById('validatePlayerName');
    const themeInterfaceSelector = document.getElementById('themeInterfaceSelector');

    const splitScreenToggle = document.getElementById('splitScreenToggle');    
    const otherEditorWrapper = document.getElementById('other-editor-wrapper');
    const editorResizeHandle = document.getElementById('editor-resize-handle');
    const mainEditorWrapper = document.getElementById('main-editor-wrapper');

    // Restaurer les données utilisateur
    const savedUser = localStorage.getItem('webtroop-user');
    if (savedUser) {
        const userInfo = JSON.parse(savedUser);
        userNameInput.value = userInfo.name;
        userColorInput.value = userInfo.color;
        updateUserInfo(); // Met à jour awareness
    }

    function updateUserInfo() {
        const userInfo = {
            name: userNameInput.value || 'Anonyme',
            color: userColorInput.value
        };
        
        // Sauvegarder dans localStorage
        localStorage.setItem('webtroop-user', JSON.stringify(userInfo));
        
        // Mettre à jour awareness
        awareness.setLocalStateField('user', userInfo);
    }

    // Event listeners
    userNameInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            updateUserInfo();
            userNameInput.blur();
        }
    });

    buttonValidatePlayerName.addEventListener('click', (e) => {
        e.preventDefault();
        updateUserInfo();
        userNameInput.blur();
    }
    );
    
    userColorInput.addEventListener('input', updateUserInfo);

    // Gestion du changement de police
    fontSelect.addEventListener('change', (e) => {
        const font = e.target.value;
        editor.getWrapperElement().style.fontFamily = font;
        otherEditor.getWrapperElement().style.fontFamily = font;
        document.body.style.fontFamily = font;
        localStorage.setItem('preferredFont', font);
    });

    // Restaurer la police sauvegardée
    const savedFont = localStorage.getItem('preferredFont');
    if (savedFont) {
        fontSelect.value = savedFont;
        editor.getWrapperElement().style.fontFamily = savedFont;
        otherEditor.getWrapperElement().style.fontFamily = savedFont;
        }

    // Gestion ouverture/fermeture du panneau
    configButton.addEventListener('click', () => {
        configPanel.classList.toggle('open');
    });

    // Fermer le panneau en cliquant en dehors
    document.addEventListener('click', (e) => {
        if (!configPanel.contains(e.target) && 
            !configButton.contains(e.target) && 
            configPanel.classList.contains('open')) {
            configPanel.classList.remove('open');
        }
    });

    // Gestion du thème
    const themeSelect = document.getElementById('themeSelect');
    themeSelect.addEventListener('change', (e) => {
        const theme = e.target.value;
        editor.setOption('theme', theme);
        otherEditor.setOption('theme', theme);
        localStorage.setItem('preferredTheme', theme);
    });

    // Restaurer le thème
    const savedTheme = localStorage.getItem('preferredTheme');
    if (savedTheme) {
        editor.setOption('theme', savedTheme);
        otherEditor.setOption('theme', savedTheme);
        themeSelect.value = savedTheme;
    }

    

    // Restaurer la taille sauvegardée
    const savedSize = localStorage.getItem('preferredFontSize');
    if (savedSize) {
        fontSizeSlider.value = savedSize;
        updateFontSize(savedSize);
    }

    const savedInterfaceSize = localStorage.getItem('preferredInterfaceFontSize');
    if (savedInterfaceSize) {
        fontInterfaceSizeSlider.value = savedInterfaceSize;
        updateInterfaceFontSize(savedInterfaceSize);
    }

    // Mettre à jour lors du changement
    fontSizeSlider.addEventListener('input', (e) => {
        const size = e.target.value;
        updateFontSize(size);
        });

    function updateFontSize(size) {
        // Mettre à jour l'affichage
        fontSizeValue.textContent = size;
        
        // Mettre à jour l'éditeur
        editor.getWrapperElement().style.fontSize = size + 'px';
        otherEditor.getWrapperElement().style.fontSize = size + 'px';
        

        // Forcer le rafraîchissement
        editor.refresh();
        otherEditor.refresh();

        // Sauvegarder la préférence
        localStorage.setItem('preferredFontSize', size);
    }

    fontInterfaceSizeSlider.addEventListener('input', (e) => {
        const size = e.target.value;
        updateInterfaceFontSize(size);
        });
    
    function updateInterfaceFontSize(size) {
        // Mettre à jour l'affichage
        fontInterfaceSizeValue.textContent = size;
        
        // Mettre à jour l'interface
        document.documentElement.style.fontSize = size + 'px';
        
        // Sauvegarder la préférence
        localStorage.setItem('preferredInterfaceFontSize', size);
    };

    // Ouvrir la modal
    modalbtn.onclick = function() {
        modal.style.display = "block";
    }

    // Fermer la modal
    closeModal.onclick = function() {
        modal.style.display = "none";
    }

    // Fermer la modal en cliquant en dehors de celle-ci
    window.onclick = function(event) {
        if (event.target == modal) {
        modal.style.display = "none";
        }
    }

    // Restore the interface theme
    const savedInterfaceTheme = localStorage.getItem('selectedInterfaceTheme') || 'dark';
    document.documentElement.className = `${savedInterfaceTheme}-theme`;
    themeInterfaceSelector.value = savedInterfaceTheme;
    
    // Gérer le changement de thème
    themeInterfaceSelector.addEventListener('change', (e) => {
        const selectedInterfaceTheme = e.target.value;
        document.documentElement.className = `${selectedInterfaceTheme}-theme`;
        localStorage.setItem('selectedInterfaceTheme', selectedInterfaceTheme);
    });


    // Gestion du split screen
    function toggleSplitScreen(enabled) {
        if (enabled) {
            // Activer le split screen
            otherEditorWrapper.style.display = 'flex';
            if (editorResizeHandle) {
                editorResizeHandle.style.display = 'block';
            }
            mainEditorWrapper.style.height = '90%';
            
            // Restaurer les flex values par défaut
            mainEditorWrapper.style.flex = '9';
            otherEditorWrapper.style.flex = '1';
        } else {
            // Désactiver le split screen
            otherEditorWrapper.style.display = 'none';
            if (editorResizeHandle) {
                editorResizeHandle.style.display = 'none';
            }
            mainEditorWrapper.style.height = '100%';
            mainEditorWrapper.style.flex = '1';
        }
        
        // Rafraîchir les éditeurs après changement
        setTimeout(() => {
            editor.refresh();
            if (enabled) {
                otherEditor.refresh();
            }
        }, 10);
        
        // Sauvegarder la préférence
        localStorage.setItem('splitScreenEnabled', enabled.toString());
    }

    // Restaurer l'état du split screen
    const savedSplitScreen = localStorage.getItem('splitScreenEnabled');
    const splitScreenEnabled = savedSplitScreen !== 'false'; // Par défaut activé
    splitScreenToggle.checked = splitScreenEnabled;
    toggleSplitScreen(splitScreenEnabled);

    // Event listener pour le toggle
    splitScreenToggle.addEventListener('change', (e) => {
        const enabled = e.target.checked;
        toggleSplitScreen(enabled);
        
        // Mettre à jour le label
        const toggleLabel = document.querySelector('.toggle-label');
        if (toggleLabel) {
            toggleLabel.textContent = enabled ? 'Actif' : 'Inactif';
        }
    });

    return {
        updateUserInfo() {
            const userInfo = {
                name: userNameInput.value || 'Anonyme',
                color: userColorInput.value
            };
            return userInfo;
        }, 
        isSplitScreenEnabled() {
            return splitScreenToggle.checked;
        },
    };
}