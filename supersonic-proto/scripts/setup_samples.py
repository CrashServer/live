#!/usr/bin/env python3
"""
Create samples/ directory with symlinks to the UltimateSamples bank.
Run once: python3 scripts/setup_samples.py [--sample-path /path/to/UltimateSamples] [--bank 0]
"""
import argparse, json, os, re, sys

parser = argparse.ArgumentParser(description='Set up WebFoxDot sample symlinks')
parser.add_argument('--sample-path', help='Path to UltimateSamples root directory')
parser.add_argument('--bank', default='0', help='Sample bank subdirectory (default: 0)')
args = parser.parse_args()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(SCRIPT_DIR, '..')
SAMPLES_DIR = os.path.join(PROJECT_DIR, 'samples')

# Priority: CLI arg > webTroop/crash_config.json > ~/UltimateSamples
if args.sample_path:
    SAMPLE_ROOT = os.path.expanduser(args.sample_path)
else:
    config_path = os.path.join(PROJECT_DIR, '..', 'webTroop', 'crash_config.json')
    try:
        config = json.load(open(os.path.realpath(config_path)))
        SAMPLE_ROOT = config.get('sample_path', '')
    except Exception:
        SAMPLE_ROOT = os.path.expanduser('~/UltimateSamples')

BANK = args.bank
BANK_DIR = os.path.join(SAMPLE_ROOT, BANK)

if not os.path.isdir(BANK_DIR):
    print(f"Bank dir not found: {BANK_DIR}")
    print(f"Tried: {SAMPLE_ROOT}/{BANK}")
    sys.exit(1)

MAX_PER_DIR = 8  # max sample indices per character

# Special char name → symbol
SPECIAL = {
    'hyphen': '-',
    'asterix': '*',
    'plus': '+',
    'at': '@',
    'hash': '#',
    'exclamation': '!',
    'bar': '|',
    'question': '?',
    'colon': ':',
    'semicolon': ';',
    'dollar': '$',
    'equals': '=',
    'caret': '^',
    'tilde': '~',
    'backslash': '\\',
    'forwardslash': '/',
    'lessthan': '<',
    'percent': '%',
    'ampersand': '&',
    '1': '1', '2': '2', '3': '3', '4': '4',
}
SPECIAL_REV = {v: k for k, v in SPECIAL.items()}  # symbol → dir name

manifest = {}  # char → { lower: [url, ...], upper: [url, ...] }

def link_dir(char, src_dir, dst_dir):
    """Symlink sorted wav files from src_dir → dst_dir/0.wav, 1.wav, ..."""
    if not os.path.isdir(src_dir):
        return []
    wavs = sorted(f for f in os.listdir(src_dir) if f.lower().endswith('.wav'))
    os.makedirs(dst_dir, exist_ok=True)
    urls = []
    for i, wav in enumerate(wavs[:MAX_PER_DIR]):
        link_path = os.path.join(dst_dir, f'{i}.wav')
        src_path  = os.path.join(src_dir, wav)
        if os.path.islink(link_path):
            os.unlink(link_path)
        os.symlink(src_path, link_path)
        rel = os.path.relpath(link_path, PROJECT_DIR)
        urls.append(rel.replace('\\', '/'))
    return urls

# a-z / A-Z
for letter in 'abcdefghijklmnopqrstuvwxyz':
    char_dir = os.path.join(BANK_DIR, letter)
    manifest[letter] = {}
    manifest[letter.upper()] = {}

    lower_urls = link_dir(
        letter,
        os.path.join(char_dir, 'lower'),
        os.path.join(SAMPLES_DIR, letter, 'lower')
    )
    manifest[letter]['urls'] = lower_urls

    upper_urls = link_dir(
        letter,
        os.path.join(char_dir, 'upper'),
        os.path.join(SAMPLES_DIR, letter, 'upper')
    )
    manifest[letter.upper()]['urls'] = upper_urls

# Special chars
for dir_name, sym in SPECIAL.items():
    src_dir = os.path.join(BANK_DIR, '_', dir_name)
    safe_name = re.sub(r'[^a-z0-9]', '_', sym)
    dst_dir = os.path.join(SAMPLES_DIR, '_', dir_name)
    urls = link_dir(sym, src_dir, dst_dir)
    manifest[sym] = {'urls': urls}

# Assign buffer IDs and write manifest with bufIDs
buf_id = 0
for char, info in manifest.items():
    urls = info.get('urls', [])
    info['bufStart'] = buf_id
    info['count'] = len(urls)
    buf_id += len(urls)

manifest_path = os.path.join(SAMPLES_DIR, 'manifest.json')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"Manifest written: {manifest_path}")
print(f"Total buffers allocated: {buf_id}")
print(f"Characters covered: {len(manifest)}")
