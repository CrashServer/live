import qbs
import qbs.Process
import qbs.File
import qbs.FileInfo
import qbs.TextFile
import "../../../libs/openFrameworksCompiled/project/qtcreator/ofApp.qbs" as ofApp

Project{
    property string of_root: "../../.."

    ofApp {
        name: { return FileInfo.baseName(sourceDirectory) }

        files: [
            "src/Audio.cpp",
            "src/Audio.h",
            "src/VideoplayerHap.cpp",
            "src/VideoplayerHap.h",
            "src/boot.cpp",
            "src/boot.h",
            "src/dmx.cpp",
            "src/dmx.h",
            "src/easing.h",
            "src/imageplayer.cpp",
            "src/imageplayer.h",
            "src/ofxBeat.cpp",
            "src/ofxBeat.h",
            "src/Camera.cpp",
            "src/Camera.h",
            "src/Getdata.cpp",
            "src/Getdata.h",
            "src/UiMisc.cpp",
            "src/UiMisc.h",
            "src/Videoplayer.cpp",
            "src/Videoplayer.h",
            "src/drawwindows.cpp",
            "src/drawwindows.h",
            "src/glitcher.cpp",
            "src/glitcher.h",
            "src/main.cpp",
            "src/ofApp.cpp",
            "src/ofApp.h",
            "src/ofxImageSequencePlayback.h",
            "src/ofxImageSequencePlayback.cpp",
            "src/fft.cpp",
            "src/fft.h",
            "src/scene.cpp",
            "src/scene.h",
            "src/textris.cpp",
            "src/textris.h",
        ]

        of.addons: [
            'ofxGui',
            'ofxImageSequence',
            'ofxNetwork',
            'ofxOsc',
            'ofxXmlSettings',
            'ofxGenericDmx',
            'ofxBox2d',
            'ofxHapPlayer'
        ]

        // additional flags for the project. the of module sets some
        // flags by default to add the core libraries, search paths...
        // this flags can be augmented through the following properties:
        of.pkgConfigs: []       // list of additional system pkgs to include
        of.includePaths: []     // include search paths
        of.cFlags: []           // flags passed to the c compiler
        of.cxxFlags: ['-std=c++17']         // flags passed to the c++ compiler
        of.linkerFlags: []      // flags passed to the linker
        of.defines: []          // defines are passed as -D to the compiler
                                // and can be checked with #ifdef or #if in the code
        of.frameworks: []       // osx only, additional frameworks to link with the project
        of.staticLibraries: ["ftdi"]  // static libraries
        of.dynamicLibraries: [] // dynamic libraries

        // other flags can be set through the cpp module: http://doc.qt.io/qbs/cpp-module.html
        // eg: this will enable ccache when compiling
        //
        // cpp.compilerWrapper: 'ccache'

        Depends{
            name: "cpp"
        }

        // common rules that parse the include search paths, core libraries...
        Depends{
            name: "of"
        }

        // dependency with the OF library
        Depends{
            name: "openFrameworks"
        }
    }

    property bool makeOF: true  // use makfiles to compile the OF library
                                // will compile OF only once for all your projects
                                // otherwise compiled per project with qbs
    

    property bool precompileOfMain: false  // precompile ofMain.h
                                           // faster to recompile when including ofMain.h 
                                           // but might use a lot of space per project

    references: [FileInfo.joinPaths(of_root, "/libs/openFrameworksCompiled/project/qtcreator/openFrameworks.qbs")]
}
