# WebFoxDot FX Registry
_Generated 2026-05-29 02:54 from supersonic-proto/js/fx/registry.js (12 params)_

| Param | SC param | Default | Description |
|---|---|---|---|
| `lpf` | `lpf` | `0` | LPF cutoff Hz (0=off, e.g. 2000) |
| `lpf_rq` | `lpf_rq` | `0.7` | LPF resonance (0.01=sharp, 1=flat) |
| `hpf` | `hpf` | `0` | HPF cutoff Hz (0=off, e.g. 400) |
| `hpf_rq` | `hpf_rq` | `0.7` | HPF resonance |
| `reverb` | `reverb` | `0` | Reverb mix |
| `room` | `rev_room` | `0.6` | Room size |
| `damp` | `rev_damp` | `0.5` | High-freq damping |
| `tanh` | `tanh` | `0` | Soft clip mix |
| `drive` | `tanh_drive` | `2` | Drive amount |
| `echo` | `echo` | `0` | Echo mix |
| `echo_time` | `echo_time` | `0.25` | Echo delay in seconds |
| `echo_dec` | `echo_dec` | `0.5` | Echo decay/feedback |

## Adding a new FX param

1. Add the processing to `synthdefs/src/fx/fx_chain.scd`
2. Add entry here in `js/fx/registry.js`:
```javascript
myeff: { scParam: 'myeff', default: 0, desc: 'My effect (0=off, 1=full)' },
```
3. Run `scripts/build.sh` to recompile, reload browser