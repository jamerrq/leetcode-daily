"use strict";
(() => {
  // src/3483/animation.ts
  function buildTicks(digits) {
    const ticks = [];
    const foundList = [];
    const cumulativeFound = [];
    const indexOf = /* @__PURE__ */ new Map();
    const n = digits.length;
    const record = (tick) => {
      ticks.push(tick);
      cumulativeFound.push(foundList.length);
    };
    for (let i = 0; i < n; i++) {
      const first = digits[i];
      const iPruned = first === 0;
      let snap = {
        i,
        iDigit: first,
        iPruned,
        j: null,
        jDigit: null,
        k: null,
        kDigit: null,
        kPruned: null,
        candidate: null,
        isNew: null,
        foundIndex: null
      };
      record({ kind: "i", snapshot: snap });
      if (iPruned) continue;
      for (let j = 0; j < n; j++) {
        if (j === i) continue;
        const second = digits[j];
        snap = { ...snap, j, jDigit: second, k: null, kDigit: null, kPruned: null, candidate: null, isNew: null, foundIndex: null };
        record({ kind: "j", snapshot: snap });
        for (let k = 0; k < n; k++) {
          if (k === i || k === j) continue;
          const third = digits[k];
          const kPruned = third % 2 !== 0;
          if (kPruned) {
            snap = { ...snap, k, kDigit: third, kPruned: true, candidate: null, isNew: null, foundIndex: null };
            record({ kind: "k", snapshot: snap });
            continue;
          }
          const candidate = first * 100 + second * 10 + third;
          const existing = indexOf.get(candidate);
          let isNew;
          let foundIndex;
          if (existing === void 0) {
            foundIndex = foundList.length;
            foundList.push(candidate);
            indexOf.set(candidate, foundIndex);
            isNew = true;
          } else {
            foundIndex = existing;
            isNew = false;
          }
          snap = { ...snap, k, kDigit: third, kPruned: false, candidate, isNew, foundIndex };
          record({ kind: "k", snapshot: snap });
        }
      }
    }
    return { ticks, foundList, cumulativeFound };
  }
  var easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);
  var easeInCubic = (t) => t * t * t;
  var Smoothed = class {
    constructor(initial, duration = 280) {
      this.current = initial;
      this.target = initial;
      this.startVal = initial;
      this.startTime = -Infinity;
      this.duration = duration;
    }
    set(target, snap = false) {
      if (snap) {
        this.current = target;
        this.target = target;
        this.startVal = target;
        this.startTime = -Infinity;
        return;
      }
      if (target !== this.target) {
        this.startVal = this.current;
        this.target = target;
        this.startTime = performance.now();
      }
    }
    update() {
      const elapsed = performance.now() - this.startTime;
      const t = Math.max(0, Math.min(1, elapsed / this.duration));
      this.current = this.startVal + (this.target - this.startVal) * easeOutCubic(t);
      return this.current;
    }
  };
  var PRESET_DEFAULT = "2,1,3,0";
  var state = {
    digits: [],
    ticks: [],
    foundList: [],
    cumulativeFound: [],
    currentTick: -1,
    playing: false,
    speed: 6,
    lastAdvance: 0,
    manual: { active: false, i: 0, j: 0, k: 0 }
  };
  function parseDigits(raw) {
    const parts = raw.split(/[,\s]+/).map((p) => p.trim()).filter((p) => p.length > 0);
    if (parts.length < 3 || parts.length > 9) return null;
    const digits = [];
    for (const p of parts) {
      if (!/^\d$/.test(p)) return null;
      digits.push(Number(p));
    }
    return digits;
  }
  function foundSoFarCount() {
    return state.currentTick < 0 ? 0 : state.cumulativeFound[state.currentTick];
  }
  function computeEffectiveView() {
    if (state.digits.length === 0) return null;
    if (state.manual.active) {
      const { i, j, k } = state.manual;
      const iDigit = state.digits[i];
      const jDigit = state.digits[j];
      const kDigit = state.digits[k];
      const leadingZero = iDigit === 0;
      const jSameAsI = j === i;
      const kRepeats = k === i || k === j;
      const kOdd = kDigit % 2 !== 0;
      const invalid = leadingZero || jSameAsI || kRepeats || kOdd;
      let candidate = null;
      let status2 = "invalid";
      if (!invalid) {
        candidate = iDigit * 100 + jDigit * 10 + kDigit;
        const foundSoFar = state.foundList.slice(0, foundSoFarCount());
        status2 = foundSoFar.includes(candidate) ? "dup" : "new";
      }
      return {
        mode: "manual",
        i,
        iDigit,
        iInvalid: leadingZero,
        j,
        jDigit,
        jActive: true,
        jInvalid: jSameAsI,
        k,
        kDigit,
        kActive: true,
        kInvalid: kRepeats || kOdd,
        candidate,
        candidateStatus: invalid ? "invalid" : status2
      };
    }
    if (state.currentTick < 0) return null;
    const snap = state.ticks[state.currentTick].snapshot;
    let status = "none";
    if (snap.iPruned && snap.j === null) status = "invalid";
    else if (snap.kPruned) status = "invalid";
    else if (snap.isNew === true) status = "new";
    else if (snap.isNew === false) status = "dup";
    return {
      mode: "trace",
      i: snap.i,
      iDigit: snap.iDigit,
      iInvalid: snap.iPruned,
      j: snap.j,
      jDigit: snap.jDigit,
      jActive: snap.j !== null,
      jInvalid: false,
      k: snap.k,
      kDigit: snap.kDigit,
      kActive: snap.k !== null,
      kInvalid: !!snap.kPruned,
      candidate: snap.candidate,
      candidateStatus: status
    };
  }
  var els = {
    digitsInput: document.getElementById("digits-input"),
    applyBtn: document.getElementById("apply-digits"),
    error: document.getElementById("digits-error"),
    presets: Array.from(document.querySelectorAll("[data-preset]")),
    resetBtn: document.getElementById("btn-reset"),
    backBtn: document.getElementById("btn-back"),
    stepBtn: document.getElementById("btn-step"),
    playBtn: document.getElementById("btn-play"),
    progress: document.getElementById("progress"),
    speed: document.getElementById("speed"),
    speedValue: document.getElementById("speed-value"),
    uniqueCount: document.getElementById("unique-count"),
    foundList: document.getElementById("found-list"),
    pointerControls: document.getElementById("pointer-controls"),
    rowI: document.getElementById("pointer-row-i"),
    rowJ: document.getElementById("pointer-row-j"),
    rowK: document.getElementById("pointer-row-k"),
    sliderI: document.getElementById("slider-i"),
    sliderJ: document.getElementById("slider-j"),
    sliderK: document.getElementById("slider-k"),
    readoutI: document.getElementById("slider-i-readout"),
    readoutJ: document.getElementById("slider-j-readout"),
    readoutK: document.getElementById("slider-k-readout"),
    manualHint: document.getElementById("manual-hint"),
    resumeTraceBtn: document.getElementById("btn-resume-trace")
  };
  var chipEls = [];
  function setError(message) {
    els.error.textContent = message;
  }
  function loadDigits(raw) {
    const digits = parseDigits(raw);
    if (!digits) {
      setError("Enter 3\u20139 single digits (0\u20139), separated by commas.");
      return;
    }
    setError("");
    els.digitsInput.value = digits.join(",");
    state.digits = digits;
    const built = buildTicks(digits);
    state.ticks = built.ticks;
    state.foundList = built.foundList;
    state.cumulativeFound = built.cumulativeFound;
    state.currentTick = -1;
    state.playing = false;
    const n = digits.length;
    state.manual = { active: false, i: 0, j: Math.min(1, n - 1), k: Math.min(2, n - 1) };
    for (const slider of [els.sliderI, els.sliderJ, els.sliderK]) {
      slider.min = "0";
      slider.max = String(n - 1);
    }
    els.sliderI.value = String(state.manual.i);
    els.sliderJ.value = String(state.manual.j);
    els.sliderK.value = String(state.manual.k);
    chipEls = [];
    els.foundList.innerHTML = "";
    renderAll();
  }
  function renderAll() {
    renderProgress();
    renderFoundPanel();
    updateButtonsEnabled();
    renderPointerPanel();
  }
  function renderProgress() {
    const total = state.ticks.length;
    const cur = Math.max(0, state.currentTick + 1);
    els.progress.textContent = `tick ${cur} / ${total}`;
    els.playBtn.classList.toggle("is-playing", state.playing);
    els.playBtn.setAttribute("aria-label", state.playing ? "Pause" : "Play");
    els.playBtn.title = state.playing ? "Pause (space)" : "Play (space)";
  }
  function updateButtonsEnabled() {
    const atEnd = state.currentTick >= state.ticks.length - 1;
    const atStart = state.currentTick <= -1;
    els.stepBtn.disabled = atEnd;
    els.playBtn.disabled = atEnd;
    els.backBtn.disabled = atStart;
  }
  function appendChip(value) {
    const chip = document.createElement("div");
    chip.className = "chip";
    chip.textContent = String(value);
    els.foundList.appendChild(chip);
    chipEls.push(chip);
    els.foundList.scrollTop = els.foundList.scrollHeight;
    return chip;
  }
  function pulseChip(index) {
    const chip = chipEls[index];
    if (!chip) return;
    chip.classList.remove("pulse");
    void chip.offsetWidth;
    chip.classList.add("pulse");
  }
  function syncFoundChips(count) {
    while (chipEls.length > count) {
      const chip = chipEls.pop();
      chip?.remove();
    }
    while (chipEls.length < count) {
      appendChip(state.foundList[chipEls.length]);
    }
  }
  function renderFoundPanel() {
    const count = foundSoFarCount();
    syncFoundChips(count);
    els.uniqueCount.textContent = String(count);
  }
  function renderPointerRow(row, slider, readout, key, view) {
    const idx = view ? view[key] : null;
    const active = view ? key === "i" ? true : key === "j" ? view.jActive : view.kActive : false;
    const invalid = view ? key === "i" ? view.iInvalid : key === "j" ? view.jInvalid : view.kInvalid : false;
    if (!state.manual.active && idx !== null) {
      slider.value = String(idx);
    }
    readout.textContent = idx !== null ? `\u2192 digits[${idx}] = ${state.digits[idx]}` : "\u2192 not yet reached";
    row.classList.toggle("inactive", !active);
    row.classList.toggle("invalid", invalid);
  }
  function renderPointerPanel() {
    const view = computeEffectiveView();
    renderPointerRow(els.rowI, els.sliderI, els.readoutI, "i", view);
    renderPointerRow(els.rowJ, els.sliderJ, els.readoutJ, "j", view);
    renderPointerRow(els.rowK, els.sliderK, els.readoutK, "k", view);
    els.manualHint.hidden = !state.manual.active;
    els.pointerControls.classList.toggle("manual-active", state.manual.active);
  }
  function exitManualMode() {
    state.manual.active = false;
  }
  function setCurrentTick(next) {
    const clamped = Math.max(-1, Math.min(state.ticks.length - 1, next));
    if (clamped === state.currentTick) return;
    state.currentTick = clamped;
    const tick = state.currentTick >= 0 ? state.ticks[state.currentTick] : null;
    if (tick && tick.kind === "k" && tick.snapshot.candidate !== null && tick.snapshot.isNew === false && tick.snapshot.foundIndex !== null) {
      pulseChip(tick.snapshot.foundIndex);
    }
    renderAll();
  }
  function advanceOneTick() {
    if (state.currentTick >= state.ticks.length - 1) return;
    setCurrentTick(state.currentTick + 1);
  }
  function backOneTick() {
    if (state.currentTick <= -1) return;
    setCurrentTick(state.currentTick - 1);
  }
  els.applyBtn.addEventListener("click", () => loadDigits(els.digitsInput.value));
  els.digitsInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") loadDigits(els.digitsInput.value);
  });
  els.presets.forEach((btn) => {
    btn.addEventListener("click", () => {
      const preset = btn.getAttribute("data-preset");
      loadDigits(preset);
    });
  });
  els.resetBtn.addEventListener("click", () => loadDigits(els.digitsInput.value));
  els.backBtn.addEventListener("click", () => {
    exitManualMode();
    state.playing = false;
    backOneTick();
    renderAll();
  });
  els.stepBtn.addEventListener("click", () => {
    exitManualMode();
    state.playing = false;
    advanceOneTick();
    renderAll();
  });
  els.playBtn.addEventListener("click", () => {
    if (state.currentTick >= state.ticks.length - 1) return;
    exitManualMode();
    state.playing = !state.playing;
    renderAll();
  });
  els.speed.addEventListener("input", () => {
    state.speed = Number(els.speed.value);
    els.speedValue.textContent = `${state.speed} / s`;
  });
  function onPointerSliderInput(which, slider) {
    return () => {
      state.manual.active = true;
      state.manual[which] = Number(slider.value);
      state.playing = false;
      renderAll();
    };
  }
  els.sliderI.addEventListener("input", onPointerSliderInput("i", els.sliderI));
  els.sliderJ.addEventListener("input", onPointerSliderInput("j", els.sliderJ));
  els.sliderK.addEventListener("input", onPointerSliderInput("k", els.sliderK));
  els.resumeTraceBtn.addEventListener("click", () => {
    exitManualMode();
    renderAll();
  });
  window.addEventListener("keydown", (e) => {
    const tag = e.target?.tagName;
    if (tag === "INPUT") return;
    if (e.code === "Space") {
      e.preventDefault();
      els.playBtn.click();
    } else if (e.code === "ArrowRight") {
      e.preventDefault();
      els.stepBtn.click();
    } else if (e.code === "ArrowLeft") {
      e.preventDefault();
      els.backBtn.click();
    }
  });
  var LOGICAL_W = 640;
  var TILE_SIZE = 44;
  var SLOT_SIZE = 64;
  function buildLayout() {
    let y = 22;
    const digitsLabelY = y;
    y += 20;
    const badgeY = y + 8;
    y += 22;
    const tileY = y + TILE_SIZE / 2;
    y += TILE_SIZE;
    y += 12;
    const indexY = y;
    y += 18;
    y += 22;
    const slotLabelY = y;
    y += 16;
    const slotY = y + SLOT_SIZE / 2;
    y += SLOT_SIZE;
    y += 14;
    const slotBottomLabelY = y;
    y += 22;
    const logY = y + 6;
    y += 20;
    y += 22;
    return { digitsLabelY, badgeY, tileY, indexY, slotLabelY, slotY, slotBottomLabelY, logY, height: y };
  }
  var LAYOUT = buildLayout();
  var LOGICAL_H = LAYOUT.height;
  var sketch = (p) => {
    let colors = {};
    let tileX = [];
    const pointerI = new Smoothed(0, 260);
    const pointerJ = new Smoothed(0, 260);
    const pointerK = new Smoothed(0, 260);
    const opacityJ = new Smoothed(0, 220);
    const opacityK = new Smoothed(0, 220);
    let flashStart = -Infinity;
    const FLASH_MS = 650;
    let lastViewKey = "";
    function readColors() {
      const cs = getComputedStyle(document.documentElement);
      colors = {
        panel: cs.getPropertyValue("--panel").trim(),
        border: cs.getPropertyValue("--border").trim(),
        text: cs.getPropertyValue("--text").trim(),
        textDim: cs.getPropertyValue("--text-dim").trim(),
        current: cs.getPropertyValue("--accent-current").trim(),
        success: cs.getPropertyValue("--accent-success").trim(),
        warn: cs.getPropertyValue("--accent-warn").trim(),
        bg: cs.getPropertyValue("--bg").trim()
      };
    }
    function layoutTiles(n) {
      const gap = 12;
      const totalW = n * TILE_SIZE + (n - 1) * gap;
      const startX = (LOGICAL_W - totalW) / 2 + TILE_SIZE / 2;
      tileX = [];
      for (let idx = 0; idx < n; idx++) tileX.push(startX + idx * (TILE_SIZE + gap));
    }
    p.setup = () => {
      const container = document.getElementById("sketch-container");
      const w = container.clientWidth || LOGICAL_W;
      const h = w * LOGICAL_H / LOGICAL_W;
      const canvas = p.createCanvas(w, h);
      canvas.parent(container);
      readColors();
      layoutTiles(Math.max(state.digits.length, 1));
      p.textFont("Fira Code");
      p.frameRate(60);
    };
    p.windowResized = () => {
      const container = document.getElementById("sketch-container");
      const w = container.clientWidth || LOGICAL_W;
      const h = w * LOGICAL_H / LOGICAL_W;
      p.resizeCanvas(w, h);
    };
    let knownDigitsKey = "";
    function syncFromState() {
      const key = state.digits.join(",");
      if (key !== knownDigitsKey) {
        knownDigitsKey = key;
        layoutTiles(state.digits.length);
        pointerI.set(tileX[0] ?? LOGICAL_W / 2, true);
        pointerJ.set(tileX[0] ?? LOGICAL_W / 2, true);
        pointerK.set(tileX[0] ?? LOGICAL_W / 2, true);
        opacityJ.set(0, true);
        opacityK.set(0, true);
        lastViewKey = "";
      }
    }
    p.draw = () => {
      if (state.playing) {
        const now = performance.now();
        const interval = 1e3 / Math.max(1, state.speed);
        if (now - state.lastAdvance >= interval) {
          state.lastAdvance = now;
          advanceOneTick();
          if (state.currentTick >= state.ticks.length - 1) {
            state.playing = false;
            renderAll();
          }
        }
      }
      const scale = p.width / LOGICAL_W;
      syncFromState();
      p.push();
      p.scale(scale);
      p.background(colors.panel);
      const view = computeEffectiveView();
      const viewKey = view ? `${view.mode}:${view.i}:${view.j}:${view.k}` : "none";
      if (viewKey !== lastViewKey) {
        lastViewKey = viewKey;
        if (view) {
          pointerI.set(tileX[view.i]);
          opacityJ.set(view.jActive ? 1 : 0);
          if (view.j !== null) pointerJ.set(tileX[view.j]);
          opacityK.set(view.kActive ? 1 : 0);
          if (view.k !== null) pointerK.set(tileX[view.k]);
          if (view.mode === "trace") {
            flashStart = performance.now();
          }
        } else {
          opacityJ.set(0);
          opacityK.set(0);
        }
      }
      pointerI.update();
      pointerJ.update();
      pointerK.update();
      const jOp = opacityJ.update();
      const kOp = opacityK.update();
      drawDigitsRow(view, jOp, kOp);
      drawSlots(view);
      drawCandidate(view);
      drawLog(view);
      p.pop();
    };
    function flashEnvelope() {
      const age = performance.now() - flashStart;
      if (age < 0 || age > FLASH_MS) return 0;
      const t = age / FLASH_MS;
      if (t < 0.15) return t / 0.15;
      return 1 - easeInCubic((t - 0.15) / 0.85);
    }
    function tileHighlight(idx, view) {
      if (!view) return { active: false, invalid: false };
      let active = false;
      let invalid = false;
      if (view.i === idx) {
        active = true;
        invalid = invalid || view.iInvalid;
      }
      if (view.jActive && view.j === idx) {
        active = true;
        invalid = invalid || view.jInvalid;
      }
      if (view.kActive && view.k === idx) {
        active = true;
        invalid = invalid || view.kInvalid;
      }
      return { active, invalid };
    }
    function drawBadge(x, y, label, opacity, invalid) {
      if (opacity <= 0.01) return;
      const col = p.color(invalid ? colors.warn : colors.current);
      col.setAlpha(255 * opacity);
      p.push();
      p.translate(x, y);
      p.noStroke();
      p.fill(col);
      p.rectMode(p.CENTER);
      p.rect(0, 0, 18, 16, 4);
      p.triangle(-4, 8, 4, 8, 0, 13);
      const textCol = p.color(colors.bg);
      textCol.setAlpha(255 * opacity);
      p.fill(textCol);
      p.textAlign(p.CENTER, p.CENTER);
      p.textSize(11);
      p.textFont("Fira Code");
      p.text(label, 0, -1);
      p.pop();
    }
    function drawDigitsRow(view, jOp, kOp) {
      p.textAlign(p.CENTER, p.CENTER);
      p.textSize(11);
      p.noStroke();
      p.fill(colors.textDim);
      p.text("digits", LOGICAL_W / 2, LAYOUT.digitsLabelY);
      drawBadge(pointerI.current - 9, LAYOUT.badgeY, "i", 1, view?.iInvalid ?? false);
      drawBadge(pointerJ.current, LAYOUT.badgeY, "j", jOp, view?.jInvalid ?? false);
      drawBadge(pointerK.current + 9, LAYOUT.badgeY, "k", kOp, view?.kInvalid ?? false);
      for (let idx = 0; idx < state.digits.length; idx++) {
        const x = tileX[idx];
        const { active, invalid } = tileHighlight(idx, view);
        p.rectMode(p.CENTER);
        if (active) {
          const c = invalid ? colors.warn : colors.current;
          p.stroke(c);
          p.strokeWeight(2);
          const bg = p.color(c);
          bg.setAlpha(28);
          p.fill(bg);
        } else {
          p.stroke(colors.border);
          p.strokeWeight(1);
          p.fill(colors.bg);
        }
        p.rect(x, LAYOUT.tileY, TILE_SIZE, TILE_SIZE, 6);
        p.noStroke();
        p.fill(colors.text);
        p.textSize(18);
        p.textFont("Fira Code");
        p.text(String(state.digits[idx]), x, LAYOUT.tileY - 2);
        p.fill(colors.textDim);
        p.textSize(10);
        p.text(String(idx), x, LAYOUT.indexY);
      }
    }
    function slotPositions() {
      const cy = LAYOUT.slotY;
      return [
        { x: 210, y: cy, label: "hundreds" },
        { x: 300, y: cy, label: "tens" },
        { x: 390, y: cy, label: "units" }
      ];
    }
    function drawSlots(view) {
      const slots = slotPositions();
      const size = SLOT_SIZE;
      const values = [view?.iDigit ?? null, view ? view.jDigit : null, view ? view.kDigit : null];
      const opacities = [view ? 1 : 0.25, opacityJ.current, opacityK.current];
      const invalidFlags = [view?.iInvalid ?? false, view?.jInvalid ?? false, view?.kInvalid ?? false];
      for (let idx = 0; idx < 3; idx++) {
        const { x, y, label } = slots[idx];
        const invalid = invalidFlags[idx];
        const op = opacities[idx];
        p.push();
        p.translate(x, y);
        p.rectMode(p.CENTER);
        const alphaMul = 0.25 + 0.75 * op;
        const strokeColor = invalid ? colors.warn : colors.border;
        const sc = p.color(strokeColor);
        sc.setAlpha(255 * alphaMul);
        p.stroke(sc);
        p.strokeWeight(invalid ? 2 : 1);
        const bgc = p.color(colors.bg);
        bgc.setAlpha(255 * alphaMul);
        p.fill(bgc);
        p.rect(0, 0, size, size, 8);
        if (values[idx] !== null && op > 0.05) {
          p.noStroke();
          const tc = p.color(colors.text);
          tc.setAlpha(255 * op);
          p.fill(tc);
          p.textSize(26);
          p.textFont("Fira Code");
          p.textAlign(p.CENTER, p.CENTER);
          p.text(String(values[idx]), 0, -2);
          if (idx === 2 && invalid) {
            p.stroke(colors.warn);
            p.strokeWeight(3);
            p.line(-size / 2 + 8, -size / 2 + 8, size / 2 - 8, size / 2 - 8);
          }
        }
        p.pop();
        p.noStroke();
        p.fill(colors.textDim);
        p.textSize(10);
        p.textAlign(p.CENTER, p.CENTER);
        p.text(label, x, LAYOUT.slotBottomLabelY);
      }
      p.fill(colors.textDim);
      p.textSize(10);
      p.text("i", slots[0].x, LAYOUT.slotLabelY);
      p.text("j", slots[1].x, LAYOUT.slotLabelY);
      p.text("k", slots[2].x, LAYOUT.slotLabelY);
    }
    function drawCandidate(view) {
      const cx = 520;
      const cy = LAYOUT.slotY;
      const manual = view?.mode === "manual";
      const envelope = manual ? 1 : flashEnvelope();
      p.noStroke();
      p.fill(colors.textDim);
      p.textSize(20);
      p.textAlign(p.CENTER, p.CENTER);
      p.text("=", 452, cy);
      let borderColor = colors.border;
      let bgColor = colors.bg;
      const status = view?.candidateStatus ?? "none";
      if (status === "new" && envelope > 0) {
        borderColor = colors.success;
        bgColor = lerpColorHex(colors.bg, colors.success, envelope * 0.25);
      } else if (status === "dup" && envelope > 0) {
        borderColor = colors.warn;
        bgColor = lerpColorHex(colors.bg, colors.warn, envelope * 0.25);
      }
      p.rectMode(p.CENTER);
      p.stroke(borderColor);
      p.strokeWeight(manual ? 1 : (status === "new" || status === "dup") && envelope > 0 ? 2 : 1);
      if (manual) {
        p.drawingContext.setLineDash([4, 4]);
      }
      p.fill(bgColor);
      p.rect(cx, cy, 130, 64, 8);
      if (manual) {
        p.drawingContext.setLineDash([]);
      }
      p.noStroke();
      p.fill(colors.text);
      p.textSize(28);
      p.textFont("Fira Code");
      const text = view?.candidate !== null && view?.candidate !== void 0 ? String(view.candidate) : "\u2014";
      p.text(text, cx, cy - 2);
      let footer = "";
      let footerColor = colors.textDim;
      if (manual) {
        footer = "exploring";
        footerColor = colors.current;
      } else if (status === "dup" && envelope > 0) {
        footer = "duplicate";
        footerColor = colors.warn;
      } else if (status === "new" && envelope > 0) {
        footer = "new";
        footerColor = colors.success;
      }
      if (footer) {
        p.fill(footerColor);
        p.textSize(10);
        p.text(footer, cx, cy + 46);
      }
    }
    function lerpColorHex(a, b, amt) {
      const ca = p.color(a);
      const cb = p.color(b);
      return p.lerpColor(ca, cb, amt);
    }
    function buildLogMessage(view) {
      if (!view) return { msg: "Press Step or Play to begin the sweep.", dot: colors.textDim };
      if (view.mode === "manual") {
        const reasons = [];
        if (view.iInvalid) reasons.push(`digits[${view.i}]=${view.iDigit} is a leading zero`);
        if (view.jInvalid) reasons.push("j picks the same index as i");
        if (view.kInvalid) {
          if (view.k === view.i || view.k === view.j) reasons.push("k repeats an index already used");
          else reasons.push(`digits[${view.k}]=${view.kDigit} is odd`);
        }
        const prefix = `exploring i=${view.i}, j=${view.j}, k=${view.k}`;
        if (reasons.length > 0) return { msg: `${prefix} -> invalid: ${reasons.join(", ")}`, dot: colors.warn };
        if (view.candidateStatus === "dup") return { msg: `${prefix} -> ${view.candidate} already found`, dot: colors.warn };
        return { msg: `${prefix} -> ${view.candidate} would be new`, dot: colors.success };
      }
      if (view.iInvalid && view.j === null) {
        return { msg: `i=${view.i} -> digit ${view.iDigit} is a leading zero, whole hundreds choice skipped`, dot: colors.warn };
      }
      if (view.j === null) {
        return { msg: `i=${view.i} -> digit ${view.iDigit} is a valid hundreds digit, scanning tens digit j`, dot: colors.current };
      }
      if (view.k === null) {
        return { msg: `i=${view.i} digit ${view.iDigit}, j=${view.j} digit ${view.jDigit} -> scanning units digit k`, dot: colors.current };
      }
      if (view.kInvalid) {
        return { msg: `k=${view.k} -> digit ${view.kDigit} is odd, candidate skipped`, dot: colors.warn };
      }
      if (view.candidateStatus === "new") {
        return { msg: `${view.candidate} is new -> added to the set`, dot: colors.success };
      }
      return { msg: `${view.candidate} was already found -> duplicate, set size unchanged`, dot: colors.warn };
    }
    function drawLog(view) {
      const y = LAYOUT.logY;
      p.noStroke();
      p.textAlign(p.LEFT, p.CENTER);
      p.textSize(13);
      p.textFont("Fira Code");
      const { msg, dot } = buildLogMessage(view);
      p.fill(dot);
      p.ellipse(18, y, 8, 8);
      p.fill(colors.text);
      p.text(msg, 32, y);
    }
  };
  function boot() {
    els.speedValue.textContent = `${state.speed} / s`;
    loadDigits(PRESET_DEFAULT);
    new p5(sketch);
  }
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(boot);
  } else {
    boot();
  }
})();
//# sourceMappingURL=animation.js.map
