// FXChain — manages one fd_fx_chain synth node per player.
// Created on first player activation, freed when player stops.
// FX params updated live via /n_set each step.

import { buildFxParams } from './registry.js';

export class FXChain {
    constructor(bus, fxGroupId, sc) {
        this._nodeId = sc.nextNodeId();
        sc.send('/s_new', 'fd_fx_chain', this._nodeId, 0, fxGroupId, 'in_bus', bus, 'out', 0);
    }

    // Apply resolved FX args (only sends params that changed would be optimization, for now send all)
    update(resolvedFxArgs, sc) {
        const params = buildFxParams(resolvedFxArgs);
        if (params.length > 0) sc.send('/n_set', this._nodeId, ...params);
    }

    free(sc) {
        if (this._nodeId !== null) {
            try { sc.send('/n_free', this._nodeId); } catch (_) {}
            this._nodeId = null;
        }
    }
}
