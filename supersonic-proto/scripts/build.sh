#!/usr/bin/env bash
# Build script — compile all SynthDefs to synthdefs/compiled/
# Usage:
#   ./scripts/build.sh          — compile everything
#   ./scripts/build.sh dbass    — compile one synth (looks for matching .scd)

set -e
cd "$(dirname "$0")/.."
mkdir -p synthdefs/compiled

if [ -n "$1" ]; then
    # Single synth compile
    FILE=$(find synthdefs/src -name "${1}.scd" | head -1)
    if [ -z "$FILE" ]; then
        echo "No SynthDef source found for: $1"
        exit 1
    fi
    echo "Compiling $FILE..."
    # Wrap in a minimal script that sets ~outDir then loads the file
    TMPSCRIPT=$(mktemp /tmp/sc_compile_XXXX.scd)
    echo "~outDir = \"$(pwd)/synthdefs/compiled/\";" > "$TMPSCRIPT"
    echo "\"$(pwd)/$FILE\".load;" >> "$TMPSCRIPT"
    echo "0.exit;" >> "$TMPSCRIPT"
    sclang "$TMPSCRIPT"
    rm "$TMPSCRIPT"
else
    # Full compile — generate script dynamically so paths work from any location
    echo "Compiling all SynthDefs..."
    TMPSCRIPT=$(mktemp /tmp/sc_compile_all_XXXX.scd)
    echo "~outDir = \"$(pwd)/synthdefs/compiled/\";" > "$TMPSCRIPT"
    for SCD in synthdefs/src/synths/*.scd synthdefs/src/fx/*.scd; do
        [ -f "$SCD" ] && echo "\"$(pwd)/$SCD\".load;" >> "$TMPSCRIPT"
    done
    echo "0.exit;" >> "$TMPSCRIPT"
    sclang "$TMPSCRIPT"
    rm "$TMPSCRIPT"
fi

echo "Done. Compiled files:"
ls -lh synthdefs/compiled/
