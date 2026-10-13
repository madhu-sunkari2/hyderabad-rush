import sys

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>Hyderabad Rush! AAA Edition ☕🍪🔥</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Outfit:wght@500;700;800;900&display=swap');

    :root {
      --saffron: #ff9933;
      --gold: #ffd700;
      --royal-red: #8b0000;
      --ruby: #c0392b;
      --iran-teal: #1abc9c;
      --night-sky: #120307;
      --card-bg: rgba(28, 8, 12, 0.88);
      --border-gold: #e5b85a;
      --fever-color: #ff007f;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background: radial-gradient(circle at 50% 35%, #300810 0%, #150205 60%, #070002 100%);
      font-family: 'Outfit', sans-serif;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      color: #fff;
    }

    /* Screen Shake & Flash FX */
    #viewport-wrapper {
      position: relative;
      width: 100vw;
      max-width: 520px;
      height: 100vh;
      max-height: 920px;
      overflow: hidden;
      background: #180308;
      box-shadow: 0 0 50px rgba(0,0,0,0.9), 0 0 0 4px var(--border-gold);
      border-radius: 28px;
    }

    @media (max-width: 540px) or (max-height: 750px) {
      #viewport-wrapper {
        border-radius: 0;
        box-shadow: none;
        max-height: 100vh;
      }
    }

    .shake {
      animation: shakeFx 0.35s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
    }
    @keyframes shakeFx {
      10%, 90% { transform: translate3d(-4px, 0, 0); }
      20%, 80% { transform: translate3d(6px, 0, 0); }
      30%, 50%, 70% { transform: translate3d(-8px, 0, 0); }
      40%, 60% { transform: translate3d(8px, 0, 0); }
    }

    #game-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 5;
      touch-action: none;
      cursor: pointer;
    }

    /* Old City Hyderabad Silhouette Background */
    .city-bg {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      background: radial-gradient(ellipse at bottom, rgba(255, 120, 20, 0.35) 0%, rgba(20, 0, 6, 0.95) 75%);
    }

    .charminar-silhouette {
      position: absolute;
      bottom: 60px;
      left: 0;
      right: 0;
      height: 160px;
      background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 320' fill='%23080002' opacity='0.7'%3E%3Cpath d='M0,320 L0,220 L60,220 L60,320 L100,320 L100,240 L160,240 L160,320 L330,320 L330,220 L370,220 L370,100 L395,70 L395,40 L410,40 L410,320 L440,320 L440,150 L560,150 L560,320 L590,320 L590,40 L605,40 L605,70 L630,100 L630,220 L670,220 L670,320 L840,320 L840,240 L900,240 L900,320 L1000,320 Z'/%3E%3Cpath d='M445,250 C445,190 555,190 555,250 L555,320 L445,320 Z' fill='%23ff9933' opacity='0.3'/%3E%3C/svg%3E") repeat-x bottom;
      background-size: 520px auto;
    }

    /* HUD Top Header */
    #hud {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 84px;
      padding: 8px 14px 4px 14px;
      background: linear-gradient(180deg, rgba(20, 4, 8, 0.95) 0%, rgba(20, 4, 8, 0.6) 80%, transparent 100%);
      z-index: 20;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid rgba(229, 184, 90, 0.35);
      pointer-events: none;
    }

    .hud-col {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .hud-label {
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: var(--saffron);
      text-transform: uppercase;
      text-shadow: 0 1px 2px #000;
    }

    .hud-val {
      font-family: 'Fredoka One', cursive;
      font-size: 1.6rem;
      line-height: 1.1;
      color: var(--gold);
      text-shadow: 2px 2px 0 #3b090e, 0 0 12px rgba(255, 215, 0, 0.6);
    }

    /* Lives Display */
    .lives-box {
      display: flex;
      gap: 4px;
      margin-top: 2px;
    }

    .heart-icon {
      font-size: 1.25rem;
      filter: drop-shadow(0 2px 4px rgba(255, 0, 80, 0.5));
      transition: transform 0.2s, opacity 0.3s;
    }
    .heart-lost {
      opacity: 0.2;
      filter: grayscale(1);
      transform: scale(0.8);
    }

    /* Pause and Sound buttons inside HUD */
    .hud-btn {
      pointer-events: auto;
      background: rgba(255, 215, 0, 0.15);
      border: 1.5px solid var(--border-gold);
      border-radius: 12px;
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1rem;
      color: #fff;
      transition: transform 0.1s;
    }
    .hud-btn:active {
      transform: scale(0.9);
    }

    /* Level & Fever Progress Bar */
    #sub-hud {
      position: absolute;
      top: 86px;
      left: 14px;
      right: 14px;
      z-index: 20;
      display: flex;
      flex-direction: column;
      gap: 5px;
      pointer-events: none;
    }

    .bar-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .bar-track {
      flex: 1;
      height: 8px;
      background: rgba(0,0,0,0.65);
      border: 1px solid rgba(255, 215, 0, 0.35);
      border-radius: 8px;
      overflow: hidden;
      position: relative;
    }

    .bar-fill-level {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #ff9933, #ffd700);
      box-shadow: 0 0 8px #ffd700;
      transition: width 0.2s ease-out;
    }

    .bar-fill-fever {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #ff007f, #ff758c);
      box-shadow: 0 0 10px #ff007f;
      transition: width 0.15s ease-out;
    }

    .bar-tag {
      font-size: 0.7rem;
      font-weight: 800;
      color: #fce8ad;
      letter-spacing: 0.5px;
      min-width: 60px;
    }

    /* Active Powerup Chips */
    #active-powerups {
      display: flex;
      gap: 6px;
      margin-top: 2px;
    }
    .powerup-pill {
      background: rgba(0, 0, 0, 0.6);
      border: 1px solid #ffd700;
      border-radius: 12px;
      padding: 2px 8px;
      font-size: 0.7rem;
      font-weight: 800;
      color: #ffd700;
      display: flex;
      align-items: center;
      gap: 4px;
      animation: popIn 0.2s ease-out;
    }

    /* Floating Combos & Callouts */
    #callout-container {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 25;
      overflow: hidden;
    }

    .callout-popup {
      position: absolute;
      font-family: 'Fredoka One', cursive;
      text-transform: uppercase;
      font-size: 2.2rem;
      letter-spacing: 1.5px;
      text-align: center;
      transform: translate(-50%, -50%) scale(0.3);
      animation: calloutAnim 1.1s cubic-bezier(0.18, 0.89, 0.32, 1.28) forwards;
      pointer-events: none;
    }
    .callout-nice { color: #2ecc71; text-shadow: 0 0 12px #2ecc71, 3px 3px 0 #000; }
    .callout-great { color: #3498db; text-shadow: 0 0 14px #3498db, 3px 3px 0 #000; }
    .callout-amazing { color: #f39c12; text-shadow: 0 0 18px #f1c40f, 3px 3px 0 #000; }
    .callout-legendary {
      font-size: 2.6rem;
      color: #ff007f;
      text-shadow: 0 0 25px #ff007f, 4px 4px 0 #000;
      animation: calloutMega 1.3s cubic-bezier(0.18, 0.89, 0.32, 1.28) forwards;
    }

    @keyframes calloutAnim {
      0% { transform: translate(-50%, -50%) scale(0.2) rotate(-6deg); opacity: 0; }
      20% { transform: translate(-50%, -50%) scale(1.15) rotate(4deg); opacity: 1; }
      35% { transform: translate(-50%, -50%) scale(1) rotate(0deg); opacity: 1; }
      75% { transform: translate(-50%, -75px) scale(1.05); opacity: 1; }
      100% { transform: translate(-50%, -110px) scale(0.8); opacity: 0; }
    }
    @keyframes calloutMega {
      0% { transform: translate(-50%, -50%) scale(0.1) rotate(-12deg); opacity: 0; }
      25% { transform: translate(-50%, -50%) scale(1.35) rotate(6deg); opacity: 1; }
      40% { transform: translate(-50%, -50%) scale(1.1) rotate(-2deg); opacity: 1; }
      80% { transform: translate(-50%, -90px) scale(1.1); opacity: 1; }
      100% { transform: translate(-50%, -140px) scale(0.85); opacity: 0; }
    }

    /* Screen Overlay Popups & Menus */
    .screen-overlay {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at center, rgba(30, 6, 12, 0.94) 0%, rgba(10, 2, 4, 0.98) 100%);
      backdrop-filter: blur(12px);
      z-index: 40;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px;
      text-align: center;
      animation: fadeIn 0.25s ease-out;
    }
    .screen-overlay.hidden {
      display: none;
    }

    /* Persian / Urdu-inspired Ornate Border Box */
    .ornate-card {
      background: var(--card-bg);
      border: 3px solid var(--border-gold);
      border-radius: 20px;
      padding: 22px 18px;
      width: 100%;
      max-width: 420px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.75), inset 0 0 15px rgba(229, 184, 90, 0.25);
      position: relative;
    }

    .ornate-card::before, .ornate-card::after {
      content: "✦";
      position: absolute;
      font-size: 1.2rem;
      color: var(--gold);
    }
    .ornate-card::before { top: 6px; left: 10px; }
    .ornate-card::after { bottom: 6px; right: 10px; }

    .game-logo {
      font-family: 'Fredoka One', cursive;
      font-size: 2.8rem;
      line-height: 1.05;
      background: linear-gradient(180deg, #fff3a8 0%, #ffd700 45%, #ff7700 85%, #b32d00 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 4px 10px rgba(255, 120, 0, 0.5));
      margin-bottom: 4px;
    }

    .game-sub {
      font-size: 0.95rem;
      color: #ffe082;
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 20px;
      text-transform: uppercase;
    }

    /* Buttons */
    .btn {
      font-family: 'Fredoka One', cursive;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      border-radius: 50px;
      transition: transform 0.12s, box-shadow 0.12s;
      text-decoration: none;
      letter-spacing: 0.8px;
    }
    .btn:active {
      transform: scale(0.96);
    }

    .btn-primary {
      background: linear-gradient(135deg, #ff9933 0%, #d32f2f 100%);
      color: #fff;
      font-size: 1.35rem;
      padding: 14px 38px;
      box-shadow: 0 8px 25px rgba(211, 47, 47, 0.6), inset 0 2px 2px rgba(255, 255, 255, 0.4);
      border: 2px solid #ffd700;
      margin-top: 10px;
    }
    .btn-primary:hover {
      box-shadow: 0 10px 30px rgba(255, 153, 51, 0.8);
      transform: translateY(-2px);
    }

    .btn-secondary {
      background: rgba(255, 255, 255, 0.1);
      border: 1.5px solid var(--border-gold);
      color: #ffe082;
      font-size: 0.95rem;
      padding: 10px 22px;
      margin: 5px;
    }
    .btn-secondary:hover {
      background: rgba(255, 215, 0, 0.2);
    }

    /* Player Input Field */
    .player-input-wrap {
      margin-bottom: 14px;
    }
    .player-input-wrap input {
      width: 80%;
      max-width: 280px;
      padding: 10px 16px;
      border-radius: 30px;
      background: rgba(0, 0, 0, 0.6);
      border: 2px solid var(--border-gold);
      color: #ffd700;
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      text-align: center;
      outline: none;
    }
    .player-input-wrap input::placeholder {
      color: rgba(255, 255, 255, 0.4);
    }

    /* Item Guide Row */
    .menu-item-preview {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
      margin: 16px 0;
      background: rgba(0,0,0,0.35);
      padding: 10px 6px;
      border-radius: 14px;
      border: 1px solid rgba(255, 215, 0, 0.2);
    }
    .preview-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3px;
    }
    .preview-icon {
      font-size: 1.5rem;
    }
    .preview-name {
      font-size: 0.65rem;
      font-weight: 700;
      color: #f7d794;
      white-space: nowrap;
    }
    .preview-pts {
      font-size: 0.7rem;
      font-weight: 900;
      color: var(--gold);
    }

    /* Daily Challenge Tag */
    .daily-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(26, 188, 156, 0.2);
      border: 1px solid var(--iran-teal);
      border-radius: 20px;
      padding: 5px 14px;
      font-size: 0.8rem;
      font-weight: 800;
      color: #1abc9c;
      margin-bottom: 12px;
      cursor: pointer;
    }
    .daily-tag.active {
      background: var(--iran-teal);
      color: #06231d;
    }

    /* Leaderboard Table */
    .lead-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
      font-size: 0.88rem;
    }
    .lead-table th {
      color: var(--saffron);
      border-bottom: 2px solid var(--border-gold);
      padding: 6px;
      font-size: 0.75rem;
      letter-spacing: 1px;
    }
    .lead-table td {
      padding: 8px 6px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      font-weight: 700;
    }
    .lead-rank-1 { color: #ffd700; font-weight: 900; }
    .lead-rank-2 { color: #e0e0e0; }
    .lead-rank-3 { color: #cd7f32; }

    /* Stats Grid Game Over */
    .stats-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 16px 0;
      text-align: left;
    }
    .stat-pill {
      background: rgba(0,0,0,0.5);
      border: 1px solid rgba(255, 215, 0, 0.3);
      border-radius: 10px;
      padding: 8px 12px;
      display: flex;
      flex-direction: column;
    }
    .stat-lbl {
      font-size: 0.7rem;
      color: #fce8ad;
      text-transform: uppercase;
      font-weight: 700;
    }
    .stat-num {
      font-family: 'Fredoka One', cursive;
      font-size: 1.25rem;
      color: #fff;
    }

    /* Level-Up Banner Animation */
    #level-up-banner {
      position: absolute;
      top: 40%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.4);
      background: linear-gradient(135deg, #ffd700, #ff5722);
      border: 4px solid #fff;
      border-radius: 24px;
      padding: 16px 36px;
      color: #2c0906;
      font-family: 'Fredoka One', cursive;
      font-size: 2.2rem;
      text-shadow: 1px 1px 0 #fff;
      box-shadow: 0 0 50px #ffd700, 0 10px 30px rgba(0,0,0,0.8);
      z-index: 35;
      display: none;
      pointer-events: none;
      white-space: nowrap;
    }

    /* Screen Flash */
    #flash-overlay {
      position: absolute;
      inset: 0;
      background: white;
      opacity: 0;
      pointer-events: none;
      z-index: 32;
      transition: opacity 0.3s ease-out;
    }

    @keyframes popIn {
      0% { transform: scale(0.4); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.96); }
      to { opacity: 1; transform: scale(1); }
    }
  </style>
</head>
<body>

  <div id="viewport-wrapper">
    <!-- Screen Flash Layer -->
    <div id="flash-overlay"></div>

    <!-- Background Silhouette Layer -->
    <div class="city-bg"></div>
    <div class="charminar-silhouette"></div>

    <!-- Level Up Banner -->
    <div id="level-up-banner">LEVEL UP! 🚀</div>

    <!-- Dynamic Callouts Overlay (NICE, GREAT, LEGENDARY) -->
    <div id="callout-container"></div>

    <!-- HUD Header -->
    <div id="hud">
      <div class="hud-col" style="align-items: flex-start;">
        <span class="hud-label">Score</span>
        <span id="hud-score" class="hud-val">0</span>
      </div>

      <div class="hud-col">
        <span class="hud-label" id="hud-level-label">Level 1</span>
        <div class="lives-box" id="lives-container">
          <span class="heart-icon">❤️</span>
          <span class="heart-icon">❤️</span>
          <span class="heart-icon">❤️</span>
        </div>
      </div>

      <div class="hud-col" style="align-items: flex-end; gap: 4px;">
        <div style="display: flex; gap: 6px;">
          <button id="btn-sound" class="hud-btn" title="Toggle Sound">🔊</button>
          <button id="btn-pause" class="hud-btn" title="Pause Game">⏸️</button>
        </div>
        <span id="streak-label" style="font-size: 0.72rem; font-weight: 900; color: #ff9933;">STREAK: 0 🔥</span>
      </div>
    </div>

    <!-- Level & Fever Multiplier Bars -->
    <div id="sub-hud">
      <div class="bar-row">
        <span class="bar-tag">GOAL</span>
        <div class="bar-track">
          <div id="bar-level" class="bar-fill-level"></div>
        </div>
      </div>
      <div class="bar-row">
        <span class="bar-tag" id="fever-tag-label" style="color: #ff007f;">FEVER</span>
        <div class="bar-track">
          <div id="bar-fever" class="bar-fill-fever"></div>
        </div>
      </div>
      <div id="active-powerups"></div>
    </div>

    <!-- Main Game Canvas -->
    <canvas id="game-canvas"></canvas>

    <!-- MAIN MENU OVERLAY -->
    <div id="screen-menu" class="screen-overlay">
      <div class="ornate-card">
        <h1 class="game-logo">HYDERABAD<br>RUSH!</h1>
        <p class="game-sub">☕ Royal AAA Old City Clicker 🍪</p>

        <div class="player-input-wrap">
          <input type="text" id="player-name-input" maxlength="14" placeholder="Enter Your Name Ustaad" value="Ustaad Player" />
        </div>

        <div id="btn-daily-mode" class="daily-tag">
          <span>📅</span><span>Daily Challenge Mode (Fixed Seed)</span>
        </div>

        <div class="menu-item-preview">
          <div class="preview-box">
            <span class="preview-icon">🍪</span>
            <span class="preview-name">Osmania</span>
            <span class="preview-pts">10 pts</span>
          </div>
          <div class="preview-box">
            <span class="preview-icon">☕</span>
            <span class="preview-name">Irani Chai</span>
            <span class="preview-pts">15 pts</span>
          </div>
          <div class="preview-box">
            <span class="preview-icon">🌶️</span>
            <span class="preview-name">Bajji</span>
            <span class="preview-pts">20 pts</span>
          </div>
          <div class="preview-box">
            <span class="preview-icon">🍲</span>
            <span class="preview-name">Haleem</span>
            <span class="preview-pts">25 pts</span>
          </div>
          <div class="preview-box">
            <span class="preview-icon">🍮</span>
            <span class="preview-name">Meetha</span>
            <span class="preview-pts">30 pts</span>
          </div>
        </div>

        <button id="btn-play-game" class="btn btn-primary">START RUSH 🚀</button>

        <div style="margin-top: 14px;">
          <button id="btn-open-leaderboard" class="btn btn-secondary">🏆 Top 5 Ranks</button>
          <button id="btn-open-howtoplay" class="btn btn-secondary">📜 How to Play</button>
        </div>
      </div>
    </div>

    <!-- LEADERBOARD OVERLAY -->
    <div id="screen-leaderboard" class="screen-overlay hidden">
      <div class="ornate-card">
        <h2 class="game-logo" style="font-size: 2.2rem;">ROYAL RANKS</h2>
        <p class="game-sub">Local Old City Legends 🏆</p>

        <table class="lead-table">
          <thead>
            <tr>
              <th>#</th>
              <th>PLAYER</th>
              <th>SCORE</th>
              <th>LVL</th>
            </tr>
          </thead>
          <tbody id="leaderboard-tbody">
            <!-- Rendered via JS -->
          </tbody>
        </table>

        <button id="btn-close-lead" class="btn btn-primary" style="margin-top: 20px; font-size: 1.1rem; padding: 10px 30px;">BACK TO MENU</button>
      </div>
    </div>

    <!-- HOW TO PLAY OVERLAY -->
    <div id="screen-howtoplay" class="screen-overlay hidden">
      <div class="ornate-card" style="text-align: left; font-size: 0.85rem; line-height: 1.6;">
        <h2 class="game-logo" style="font-size: 2.2rem; text-align: center;">HOW TO PLAY</h2>
        <p class="game-sub" style="text-align: center;">Master the Nawabi Rush</p>

        <p>🎯 <b>Catch Food</b>: Tap or click falling delicacies before they hit the ground.</p>
        <p>💥 <b>Lives</b>: Miss 3 items = lose 1 life (3 lives total). Protect the food!</p>
        <p>⚡ <b>Combo Multiplier</b>: Catch <b>3 of the SAME item in a row</b> for instant <b>2x points</b>.</p>
        <p>🔥 <b>FEVER MODE</b>: Catch <b>5 items in quick succession</b> to unleash <b>3x FEVER MODE</b>!</p>
        <p>🍲 <b>Boss Level (Level 5 & 10)</b>: Giant Biryani Handi falls slowly — tap it for <b>100 points</b>!</p>
        <p>🎁 <b>Power-Ups</b>: Catch glowing orbs for <b>🧲 Magnet</b>, <b>⏳ Slow Motion</b>, and <b>✨ 2x Double Points</b>.</p>

        <div style="text-align: center; margin-top: 16px;">
          <button id="btn-close-how" class="btn btn-primary" style="font-size: 1.1rem; padding: 10px 30px;">SAMJH GAYE! 👍</button>
        </div>
      </div>
    </div>

    <!-- PAUSE MENU OVERLAY -->
    <div id="screen-pause" class="screen-overlay hidden">
      <div class="ornate-card">
        <h2 class="game-logo" style="font-size: 2.4rem;">GAME PAUSED</h2>
        <p class="game-sub">Chai Break Ustaad? ☕</p>
        <button id="btn-resume-game" class="btn btn-primary" style="width: 80%; margin: 8px 0;">RESUME RUSH ▶️</button><br>
        <button id="btn-quit-game" class="btn btn-secondary" style="width: 80%; margin: 8px 0;">QUIT TO MENU 🏠</button>
      </div>
    </div>

    <!-- GAME OVER OVERLAY -->
    <div id="screen-gameover" class="screen-overlay hidden">
      <div class="ornate-card">
        <h2 id="go-title" class="game-logo" style="font-size: 2.3rem;">KHATAM!</h2>
        <p id="go-subtitle" class="game-sub">What a Royal Run!</p>

        <div class="stats-grid">
          <div class="stat-pill">
            <span class="stat-lbl">Final Score</span>
            <span id="stat-final-score" class="stat-num" style="color: #ffd700;">0</span>
          </div>
          <div class="stat-pill">
            <span class="stat-lbl">Level Reached</span>
            <span id="stat-final-level" class="stat-num">Level 1</span>
          </div>
          <div class="stat-pill">
            <span class="stat-lbl">Items Caught</span>
            <span id="stat-final-caught" class="stat-num">0</span>
          </div>
          <div class="stat-pill">
            <span class="stat-lbl">Best Combo</span>
            <span id="stat-final-combo" class="stat-num">0 🔥</span>
          </div>
          <div class="stat-pill">
            <span class="stat-lbl">Accuracy</span>
            <span id="stat-final-acc" class="stat-num">0%</span>
          </div>
          <div class="stat-pill">
            <span class="stat-lbl">Time Survived</span>
            <span id="stat-final-time" class="stat-num">0s</span>
          </div>
        </div>

        <button id="btn-restart-game" class="btn btn-primary" style="width: 85%;">PLAY AGAIN 🔄</button><br>
        <button id="btn-go-menu" class="btn btn-secondary" style="width: 85%; margin-top: 8px;">MAIN MENU 🏠</button>
      </div>
    </div>
  </div>

  <script>
    /* =========================================================================
       HYDERABAD RUSH: AAA ENGINE ARCHITECTURE
       ========================================================================= */

    // 1. Audio Synthesizer Engine (Sound FX & Background Music with Oscillators)
    class SoundEngine {
      constructor() {
        this.ctx = null;
        this.muted = false;
        this.bgOsc1 = null;
        this.bgOsc2 = null;
        this.bgGain = null;
        this.bgInterval = null;
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
        }
        if (this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      toggleMute() {
        this.muted = !this.muted;
        if (this.muted) {
          if (this.bgGain) this.bgGain.gain.setValueAtTime(0, this.ctx.currentTime);
        } else {
          if (this.bgGain) this.bgGain.gain.setValueAtTime(0.04, this.ctx.currentTime);
        }
        return this.muted;
      }

      startBGM() {
        if (this.bgInterval || !this.ctx || this.muted) return;
        // Festive Nawabi Pentatonic Ostinato
        const notes = [220, 247, 277, 330, 370, 440];
        let step = 0;

        this.bgGain = this.ctx.createGain();
        this.bgGain.gain.setValueAtTime(this.muted ? 0 : 0.035, this.ctx.currentTime);
        this.bgGain.connect(this.ctx.destination);

        this.bgInterval = setInterval(() => {
          if (this.muted || !this.ctx) return;
          const osc = this.ctx.createOscillator();
          const noteGain = this.ctx.createGain();
          const freq = notes[step % notes.length];
          step++;

          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          noteGain.gain.setValueAtTime(0.04, this.ctx.currentTime);
          noteGain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.22);

          osc.connect(noteGain);
          noteGain.connect(this.bgGain);
          osc.start();
          osc.stop(this.ctx.currentTime + 0.22);
        }, 260);
      }

      stopBGM() {
        if (this.bgInterval) {
          clearInterval(this.bgInterval);
          this.bgInterval = null;
        }
      }

      playCatch(itemType, comboCount = 1) {
        if (this.muted || !this.ctx) return;
        const now = this.ctx.currentTime;
        const baseFreq = {
          biscuit: 440,
          chai: 520,
          bajji: 600,
          haleem: 680,
          meetha: 780,
          boss: 320,
          powerup: 880
        }[itemType] || 440;

        const freq = baseFreq * Math.min(2.0, 1 + (comboCount * 0.05));
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now);
        osc.frequency.exponentialRampToValueAtTime(freq * 1.5, now + 0.09);

        gain.gain.setValueAtTime(0.28, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.09);

        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.09);
      }

      playRickshawHonk() {
        if (this.muted || !this.ctx) return;
        const now = this.ctx.currentTime;
        // Dual harsh horn tone simulating famous Hyderabad Auto-Rickshaw "POME-POME!"
        [480, 520].forEach(f => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(f, now);
          osc.frequency.setValueAtTime(f + 25, now + 0.08);

          gain.gain.setValueAtTime(0.22, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.18);

          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.18);
        });
      }

      playFeverStart() {
        if (this.muted || !this.ctx) return;
        const now = this.ctx.currentTime;
        [523, 659, 783, 1046, 1318].forEach((f, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(f, now + idx * 0.05);
          gain.gain.setValueAtTime(0.25, now + idx * 0.05);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.05 + 0.22);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.05);
          osc.stop(now + idx * 0.05 + 0.22);
        });
      }

      playMiss() {
        if (this.muted || !this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(180, now);
        osc.frequency.exponentialRampToValueAtTime(45, now + 0.28);
        gain.gain.setValueAtTime(0.35, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.28);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.28);
      }

      playPowerup() {
        if (this.muted || !this.ctx) return;
        const now = this.ctx.currentTime;
        [400, 600, 800, 1100].forEach((f, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(f, now + i * 0.04);
          gain.gain.setValueAtTime(0.2, now + i * 0.04);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.04 + 0.18);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.04);
          osc.stop(now + i * 0.04 + 0.18);
        });
      }

      playLevelUp() {
        if (this.muted || !this.ctx) return;
        const now = this.ctx.currentTime;
        [392, 523, 659, 783, 1046].forEach((f, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(f, now + idx * 0.07);
          gain.gain.setValueAtTime(0.3, now + idx * 0.07);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.07 + 0.35);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.07);
          osc.stop(now + idx * 0.07 + 0.35);
        });
      }

      playGameOver() {
        if (this.muted || !this.ctx) return;
        const now = this.ctx.currentTime;
        [340, 290, 240, 180].forEach((f, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(f, now + idx * 0.15);
          gain.gain.setValueAtTime(0.28, now + idx * 0.15);
          gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.15 + 0.25);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.15);
          osc.stop(now + idx * 0.15 + 0.25);
        });
      }
    }

    const sound = new SoundEngine();

    // 2. ITEM DEFINITIONS & COLOR PALETTES
    const ITEM_CONFIGS = {
      biscuit: {
        id: 'biscuit',
        name: 'Osmania Biscuit',
        emoji: '🍪',
        pts: 10,
        radius: 30,
        color: '#f39c12',
        unlockedAtLevel: 1
      },
      chai: {
        id: 'chai',
        name: 'Irani Chai',
        emoji: '☕',
        pts: 15,
        radius: 32,
        color: '#e67e22',
        unlockedAtLevel: 1
      },
      bajji: {
        id: 'bajji',
        name: 'Mirchi Bajji',
        emoji: '🌶️',
        pts: 20,
        radius: 32,
        color: '#e74c3c',
        unlockedAtLevel: 2
      },
      haleem: {
        id: 'haleem',
        name: 'Haleem Bowl',
        emoji: '🍲',
        pts: 25,
        radius: 34,
        color: '#d35400',
        unlockedAtLevel: 3
      },
      meetha: {
        id: 'meetha',
        name: 'Double ka Meetha',
        emoji: '🍮',
        pts: 30,
        radius: 34,
        color: '#f1c40f',
        unlockedAtLevel: 4
      },
      boss: {
        id: 'boss',
        name: 'Shahi Biryani Handi',
        emoji: '🥘',
        pts: 100,
        radius: 54,
        color: '#ffd700',
        unlockedAtLevel: 5
      }
    };

    const POWERUP_TYPES = [
      { id: 'magnet', name: 'MAGNET', emoji: '🧲', duration: 6, color: '#3498db' },
      { id: 'slow', name: 'SLOW-MO', emoji: '⏳', duration: 5, color: '#9b59b6' },
      { id: 'double', name: '2X PTS', emoji: '✨', duration: 7, color: '#f1c40f' }
    ];

    // Pseudo-random Seed Generator for Daily Challenge
    class RandomGenerator {
      constructor(seed = null) {
        this.seed = seed;
      }
      next() {
        if (this.seed === null) return Math.random();
        this.seed = (this.seed * 9301 + 49297) % 233280;
        return this.seed / 233280;
      }
    }

    // 3. GAME STATE MANAGEMENT
    const GameState = {
      MENU: 0,
      PLAYING: 1,
      PAUSED: 2,
      GAMEOVER: 3
    };

    let currentState = GameState.MENU;
    let playerName = 'Ustaad Player';
    let isDailyChallenge = false;
    let rng = new RandomGenerator(null);

    let canvas, ctx;
    let canvasW = 500, canvasH = 800;

    let score = 0;
    let level = 1;
    let levelTarget = 300;
    let lives = 3;
    let streak = 0;
    let bestCombo = 0;
    let itemsCaught = 0;
    let totalItemsSpawned = 0;
    let gameStartTime = 0;
    let elapsedTime = 0;

    let items = [];
    let particles = [];
    let confetti = [];
    let floatingTexts = [];

    // Combo system: Same item sequence
    let lastItemCaught = null;
    let sameItemCount = 0;

    // Chain Reaction: Fever Mode
    let recentCatchesTimestamps = [];
    let feverActive = false;
    let feverDuration = 0;

    // Powerups Active
    let activePowerups = {
      magnet: 0,
      slow: 0,
      double: 0
    };

    let missAccumulator = 0; // Miss 3 items = lose 1 life
    let spawnTimer = 0;
    let powerupSpawnTimer = 0;
    let bossSpawnedForLevel = false;

    // DOM Elements
    const wrapper = document.getElementById('viewport-wrapper');
    const hudScore = document.getElementById('hud-score');
    const hudLevelLabel = document.getElementById('hud-level-label');
    const livesContainer = document.getElementById('lives-container');
    const streakLabel = document.getElementById('streak-label');
    const barLevel = document.getElementById('bar-level');
    const barFever = document.getElementById('bar-fever');
    const feverTagLabel = document.getElementById('fever-tag-label');
    const activePowerupsDiv = document.getElementById('active-powerups');
    const calloutContainer = document.getElementById('callout-container');
    const levelUpBanner = document.getElementById('level-up-banner');
    const flashOverlay = document.getElementById('flash-overlay');

    const screenMenu = document.getElementById('screen-menu');
    const screenLeaderboard = document.getElementById('screen-leaderboard');
    const screenHowtoplay = document.getElementById('screen-howtoplay');
    const screenPause = document.getElementById('screen-pause');
    const screenGameover = document.getElementById('screen-gameover');

    const playerNameInput = document.getElementById('player-name-input');
    const btnDailyMode = document.getElementById('btn-daily-mode');
    const btnPlayGame = document.getElementById('btn-play-game');
    const btnOpenLeaderboard = document.getElementById('btn-open-leaderboard');
    const btnOpenHowtoplay = document.getElementById('btn-open-howtoplay');
    const btnCloseLead = document.getElementById('btn-close-lead');
    const btnCloseHow = document.getElementById('btn-close-how');
    const btnPause = document.getElementById('btn-pause');
    const btnSound = document.getElementById('btn-sound');
    const btnResumeGame = document.getElementById('btn-resume-game');
    const btnQuitGame = document.getElementById('btn-quit-game');
    const btnRestartGame = document.getElementById('btn-restart-game');
    const btnGoMenu = document.getElementById('btn-go-menu');

    // Stats display
    const statFinalScore = document.getElementById('stat-final-score');
    const statFinalLevel = document.getElementById('stat-final-level');
    const statFinalCaught = document.getElementById('stat-final-caught');
    const statFinalCombo = document.getElementById('stat-final-combo');
    const statFinalAcc = document.getElementById('stat-final-acc');
    const statFinalTime = document.getElementById('stat-final-time');
    const leaderboardTbody = document.getElementById('leaderboard-tbody');

    // 4. LEADERBOARD SYSTEM (Top 5 Local Highscores)
    function getLeaderboard() {
      const defaultBoard = [
        { name: "Sultan Mir", score: 2850, level: 8 },
        { name: "Nawab Hyder", score: 2100, level: 6 },
        { name: "Charminar Chicha", score: 1650, level: 5 },
        { name: "Chai Lover", score: 1200, level: 4 },
        { name: "Biryani King", score: 850, level: 3 }
      ];
      try {
        const stored = localStorage.getItem('hyd_rush_aaa_lead');
        return stored ? JSON.parse(stored) : defaultBoard;
      } catch (e) {
        return defaultBoard;
      }
    }

    function saveScoreToLeaderboard(name, sc, lvl) {
      let board = getLeaderboard();
      board.push({ name: name || 'Ustaad', score: sc, level: lvl });
      board.sort((a, b) => b.score - a.score);
      board = board.slice(0, 5);
      localStorage.setItem('hyd_rush_aaa_lead', JSON.stringify(board));
      renderLeaderboard();
      // Check if new #1 highscore
      if (board[0].score === sc && sc > 0) {
        triggerConfettiRain();
      }
    }

    function renderLeaderboard() {
      const board = getLeaderboard();
      leaderboardTbody.innerHTML = '';
      board.forEach((entry, idx) => {
        const row = document.createElement('tr');
        const rankClass = idx === 0 ? 'lead-rank-1' : (idx === 1 ? 'lead-rank-2' : (idx === 2 ? 'lead-rank-3' : ''));
        row.innerHTML = `
          <td class="${rankClass}">${idx + 1}</td>
          <td class="${rankClass}">${entry.name}</td>
          <td style="color: var(--gold);">${entry.score}</td>
          <td>${entry.level}</td>
        `;
        leaderboardTbody.appendChild(row);
      });
    }

    // 5. CANVAS & RESIZE HANDLER
    function initCanvas() {
      canvas = document.getElementById('game-canvas');
      ctx = canvas.getContext('2d');
      resizeCanvas();
      window.addEventListener('resize', resizeCanvas);
    }

    function resizeCanvas() {
      const rect = wrapper.getBoundingClientRect();
      canvasW = rect.width;
      canvasH = rect.height;
      canvas.width = canvasW;
      canvas.height = canvasH;
    }

    // 6. GAME CONTROLS & EVENT LISTENERS
    function setupEventListeners() {
      btnSound.addEventListener('click', () => {
        sound.init();
        const isMuted = sound.toggleMute();
        btnSound.textContent = isMuted ? '🔇' : '🔊';
      });

      btnDailyMode.addEventListener('click', () => {
        isDailyChallenge = !isDailyChallenge;
        btnDailyMode.classList.toggle('active', isDailyChallenge);
      });

      btnPlayGame.addEventListener('click', () => {
        sound.init();
        playerName = playerNameInput.value.trim() || 'Ustaad Player';
        startNewGame();
      });

      btnOpenLeaderboard.addEventListener('click', () => {
        renderLeaderboard();
        screenLeaderboard.classList.remove('hidden');
      });
      btnCloseLead.addEventListener('click', () => screenLeaderboard.classList.add('hidden'));

      btnOpenHowtoplay.addEventListener('click', () => screenHowtoplay.classList.remove('hidden'));
      btnCloseHow.addEventListener('click', () => screenHowtoplay.classList.add('hidden'));

      btnPause.addEventListener('click', togglePause);
      btnResumeGame.addEventListener('click', togglePause);

      btnQuitGame.addEventListener('click', () => {
        screenPause.classList.add('hidden');
        sound.stopBGM();
        currentState = GameState.MENU;
        screenMenu.classList.remove('hidden');
      });

      btnRestartGame.addEventListener('click', () => {
        screenGameover.classList.add('hidden');
        startNewGame();
      });

      btnGoMenu.addEventListener('click', () => {
        screenGameover.classList.add('hidden');
        currentState = GameState.MENU;
        screenMenu.classList.remove('hidden');
      });

      // Canvas Pointer Clicks / Taps
      const handlePointer = (e) => {
        if (currentState !== GameState.PLAYING) return;
        const rect = canvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
        const x = clientX - rect.left;
        const y = clientY - rect.top;
        checkClick(x, y);
      };

      canvas.addEventListener('pointerdown', handlePointer);
    }

    function togglePause() {
      if (currentState === GameState.PLAYING) {
        currentState = GameState.PAUSED;
        sound.stopBGM();
        screenPause.classList.remove('hidden');
      } else if (currentState === GameState.PAUSED) {
        currentState = GameState.PLAYING;
        sound.startBGM();
        screenPause.classList.add('hidden');
      }
    }

    // 7. GAME LIFECYCLE
    function startNewGame() {
      sound.init();
      sound.startBGM();

      score = 0;
      level = 1;
      levelTarget = 250;
      lives = 3;
      streak = 0;
      bestCombo = 0;
      itemsCaught = 0;
      totalItemsSpawned = 0;
      missAccumulator = 0;
      lastItemCaught = null;
      sameItemCount = 0;
      recentCatchesTimestamps = [];
      feverActive = false;
      feverDuration = 0;
      bossSpawnedForLevel = false;

      activePowerups = { magnet: 0, slow: 0, double: 0 };
      items = [];
      particles = [];
      floatingTexts = [];
      confetti = [];

      // Seed for daily challenge
      if (isDailyChallenge) {
        const today = new Date();
        const seedVal = today.getFullYear() * 10000 + (today.getMonth() + 1) * 100 + today.getDate();
        rng = new RandomGenerator(seedVal);
      } else {
        rng = new RandomGenerator(null);
      }

      gameStartTime = performance.now();
      elapsedTime = 0;

      updateHUD();
      screenMenu.classList.add('hidden');
      screenGameover.classList.add('hidden');
      currentState = GameState.PLAYING;
    }

    function updateHUD() {
      hudScore.textContent = score;
      hudLevelLabel.textContent = `Level ${level}`;
      streakLabel.textContent = `STREAK: ${streak} 🔥`;

      // Update Lives Hearts
      const hearts = livesContainer.querySelectorAll('.heart-icon');
      hearts.forEach((h, idx) => {
        if (idx < lives) {
          h.classList.remove('heart-lost');
        } else {
          h.classList.add('heart-lost');
        }
      });

      // Level Progress Bar
      const prevLevelThreshold = (level - 1) * 250;
      const progressInLevel = Math.max(0, score - prevLevelThreshold);
      const span = levelTarget - prevLevelThreshold;
      const pct = Math.min(100, (progressInLevel / span) * 100);
      barLevel.style.width = `${pct}%`;

      // Active Powerup Chips
      activePowerupsDiv.innerHTML = '';
      for (let p in activePowerups) {
        if (activePowerups[p] > 0) {
          const cfg = POWERUP_TYPES.find(x => x.id === p);
          const chip = document.createElement('div');
          chip.className = 'powerup-pill';
          chip.innerHTML = `${cfg.emoji} ${cfg.name} (${Math.ceil(activePowerups[p])}s)`;
          activePowerupsDiv.appendChild(chip);
        }
      }
    }

    function triggerScreenShake() {
      wrapper.classList.remove('shake');
      void wrapper.offsetWidth;
      wrapper.classList.add('shake');
    }

    function triggerScreenFlash() {
      flashOverlay.style.opacity = '0.6';
      setTimeout(() => { flashOverlay.style.opacity = '0'; }, 250);
    }

    function triggerLevelUp() {
      level++;
      sound.playLevelUp();
      triggerScreenFlash();

      levelUpBanner.textContent = `LEVEL ${level}! 🚀`;
      levelUpBanner.style.display = 'block';
      setTimeout(() => { levelUpBanner.style.display = 'none'; }, 1100);

      levelTarget = level * 300;
      bossSpawnedForLevel = false;

      // Special Boss Announcement for every 5 levels
      if (level % 5 === 0) {
        spawnBossHandi();
        showCallout("SHAHI BIRYANI BOSS! 🥘", "legendary");
      }
    }

    function triggerFeverMode() {
      feverActive = true;
      feverDuration = 5.0; // 5 seconds of 3x madness
      sound.playFeverStart();
      triggerScreenFlash();
      showCallout("FEVER MODE! 3X! 🔥", "legendary");
    }

    function triggerConfettiRain() {
      for (let i = 0; i < 90; i++) {
        confetti.push({
          x: Math.random() * canvasW,
          y: -20 - Math.random() * 80,
          vx: (Math.random() - 0.5) * 4,
          vy: Math.random() * 4 + 3,
          size: Math.random() * 10 + 6,
          color: ['#ffd700', '#ff9933', '#ff007f', '#2ecc71', '#3498db'][Math.floor(Math.random() * 5)],
          rotation: Math.random() * 360,
          vRot: (Math.random() - 0.5) * 10
        });
      }
    }

    function showCallout(text, type = "nice") {
      const el = document.createElement('div');
      el.className = `callout-popup callout-${type}`;
      el.textContent = text;
      el.style.left = `${canvasW / 2}px`;
      el.style.top = `${canvasH * 0.42}px`;
      calloutContainer.appendChild(el);
      setTimeout(() => el.remove(), 1300);
    }

    // 8. SPAWNING ENGINE (Levels 1 to 10 with item unlocks & powerups)
    function getAvailableItemTypes() {
      const types = [];
      for (let k in ITEM_CONFIGS) {
        if (k !== 'boss' && ITEM_CONFIGS[k].unlockedAtLevel <= level) {
          types.push(ITEM_CONFIGS[k]);
        }
      }
      return types;
    }

    function spawnItem() {
      totalItemsSpawned++;
      const available = getAvailableItemTypes();
      const cfg = available[Math.floor(rng.next() * available.length)];

      const speedFactor = 1 + (level - 1) * 0.12; // scales smoothly
      const speed = (rng.next() * 70 + 190) * speedFactor;
      const x = rng.next() * (canvasW - cfg.radius * 2 - 40) + cfg.radius + 20;

      items.push({
        isPowerup: false,
        config: cfg,
        x: x,
        y: -cfg.radius - 10,
        radius: cfg.radius,
        speed: speed,
        rotation: 0,
        rotSpeed: (rng.next() - 0.5) * 3,
        trail: []
      });
    }

    function spawnBossHandi() {
      bossSpawnedForLevel = true;
      totalItemsSpawned++;
      const cfg = ITEM_CONFIGS.boss;
      items.push({
        isPowerup: false,
        isBoss: true,
        config: cfg,
        x: canvasW / 2,
        y: -cfg.radius - 20,
        radius: cfg.radius,
        speed: 120, // falls slowly as requested
        rotation: 0,
        rotSpeed: 0.8,
        trail: []
      });
    }

    function spawnPowerup() {
      const pType = POWERUP_TYPES[Math.floor(rng.next() * POWERUP_TYPES.length)];
      const x = rng.next() * (canvasW - 80) + 40;
      items.push({
        isPowerup: true,
        config: pType,
        x: x,
        y: -35,
        radius: 26,
        speed: 160,
        rotation: 0,
        rotSpeed: 2,
        trail: []
      });
    }

    // 9. CLICK / TOUCH HIT TESTING & CHAIN LOGIC
    function checkClick(clickX, clickY) {
      for (let i = items.length - 1; i >= 0; i--) {
        const item = items[i];
        const dx = clickX - item.x;
        const dy = clickY - item.y;
        const dist = Math.hypot(dx, dy);

        // Generous touch hit box for mobile juice
        if (dist <= item.radius + 22) {
          handleCatch(item, i);
          return;
        }
      }
    }

    function handleCatch(item, index) {
      items.splice(index, 1);
      itemsCaught++;
      streak++;
      if (streak > bestCombo) bestCombo = streak;

      // Create Particle Explosion
      createParticleExplosion(item.x, item.y, item.config.color, item.isBoss ? 35 : 18);

      if (item.isPowerup) {
        // Collect Powerup
        activePowerups[item.config.id] = item.config.duration;
        sound.playPowerup();
        showFloatingText(`+${item.config.name}!`, item.x, item.y, item.config.color);
        showCallout(item.config.name, "great");
        updateHUD();
        return;
      }

      // Check Chain Reaction (5 catches within 2.5 seconds = FEVER MODE)
      const now = performance.now();
      recentCatchesTimestamps.push(now);
      recentCatchesTimestamps = recentCatchesTimestamps.filter(t => now - t <= 2600);
      if (recentCatchesTimestamps.length >= 5 && !feverActive) {
        triggerFeverMode();
      }

      // Combo System: 3 of same item in a row = 2x multiplier
      let sameItemMultiplier = 1;
      if (lastItemCaught === item.config.id) {
        sameItemCount++;
        if (sameItemCount === 3) {
          sameItemMultiplier = 2;
          sound.playRickshawHonk(); // Auto-rickshaw honk on combo!
          showCallout("SAME 3X! 2X COMBO! 🛺", "amazing");
          sameItemCount = 0; // reset
        }
      } else {
        lastItemCaught = item.config.id;
        sameItemCount = 1;
      }

      // Animated Combo Text Callouts based on streak milestones
      if (streak === 5) showCallout("NICE! 👏", "nice");
      else if (streak === 10) showCallout("GREAT! 🔥", "great");
      else if (streak === 15) showCallout("AMAZING! 🌟", "amazing");
      else if (streak === 25) showCallout("LEGENDARY! 👑", "legendary");

      // Score Calculation
      let pts = item.config.pts;
      let multipliersTotal = 1;

      if (sameItemMultiplier > 1) multipliersTotal *= sameItemMultiplier;
      if (feverActive) multipliersTotal *= 3;
      if (activePowerups.double > 0) multipliersTotal *= 2;

      pts *= multipliersTotal;
      score += pts;

      sound.playCatch(item.config.id, streak);

      const bonusLabel = multipliersTotal > 1 ? `+${pts} (${multipliersTotal}x!)` : `+${pts}`;
      showFloatingText(bonusLabel, item.x, item.y, feverActive ? '#ff007f' : item.config.color);

      // Check Level Up Progress
      if (score >= levelTarget && level < 10) {
        triggerLevelUp();
      }

      updateHUD();
    }

    function createParticleExplosion(x, y, color, count = 18) {
      for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 6 + 2;
        particles.push({
          x: x,
          y: y,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed,
          radius: Math.random() * 5 + 3,
          color: color,
          alpha: 1.0,
          decay: Math.random() * 0.03 + 0.02
        });
      }
    }

    function showFloatingText(text, x, y, color) {
      floatingTexts.push({
        text: text,
        x: x,
        y: y,
        vy: -2.2,
        alpha: 1.0,
        color: color
      });
    }

    // 10. GAME OVER HANDLER
    function triggerGameOver() {
      currentState = GameState.GAMEOVER;
      sound.stopBGM();
      sound.playGameOver();
      triggerScreenShake();

      const timeSurvived = Math.floor((performance.now() - gameStartTime) / 1000);
      const accuracy = totalItemsSpawned > 0 ? Math.round((itemsCaught / totalItemsSpawned) * 100) : 0;

      statFinalScore.textContent = score;
      statFinalLevel.textContent = `Level ${level}`;
      statFinalCaught.textContent = itemsCaught;
      statFinalCombo.textContent = `${bestCombo} 🔥`;
      statFinalAcc.textContent = `${accuracy}%`;
      statFinalTime.textContent = `${timeSurvived}s`;

      saveScoreToLeaderboard(playerName, score, level);
      screenGameover.classList.remove('hidden');
    }

    // 11. MAIN 60FPS GAME LOOP
    let lastTimestamp = 0;

    function gameLoop(timestamp) {
      if (!lastTimestamp) lastTimestamp = timestamp;
      const dt = Math.min((timestamp - lastTimestamp) / 1000, 0.1);
      lastTimestamp = timestamp;

      if (currentState === GameState.PLAYING) {
        updateGame(dt);
      }

      renderGame();
      requestAnimationFrame(gameLoop);
    }

    function updateGame(dt) {
      elapsedTime += dt;

      // Update Fever Countdown
      if (feverActive) {
        feverDuration -= dt;
        barFever.style.width = `${(feverDuration / 5.0) * 100}%`;
        if (feverDuration <= 0) {
          feverActive = false;
          barFever.style.width = '0%';
        }
      } else {
        // Show recent combo build up in fever bar
        const now = performance.now();
        recentCatchesTimestamps = recentCatchesTimestamps.filter(t => now - t <= 2600);
        barFever.style.width = `${(recentCatchesTimestamps.length / 5.0) * 100}%`;
      }

      // Update Active Powerups
      for (let p in activePowerups) {
        if (activePowerups[p] > 0) {
          activePowerups[p] -= dt;
          if (activePowerups[p] <= 0) {
            activePowerups[p] = 0;
            updateHUD();
          }
        }
      }

      // Spawning Items
      spawnTimer += dt;
      const baseGap = Math.max(0.38, 0.95 - (level * 0.065));
      const effectiveGap = feverActive ? baseGap * 0.6 : baseGap;

      if (spawnTimer >= effectiveGap) {
        spawnTimer = 0;
        spawnItem();
      }

      // Spawning Powerups (every 12-16 seconds)
      powerupSpawnTimer += dt;
      if (powerupSpawnTimer >= 14.0) {
        powerupSpawnTimer = 0;
        if (rng.next() < 0.7) {
          spawnPowerup();
        }
      }

      // Speed Modifier for Slow Motion Powerup
      const speedMult = activePowerups.slow > 0 ? 0.5 : 1.0;
      const groundY = canvasH - 50;

      // Magnet Attractor target (Center bottom)
      const magnetActive = activePowerups.magnet > 0;
      const magnetTargetX = canvasW / 2;
      const magnetTargetY = canvasH - 70;

      // Update Items
      for (let i = items.length - 1; i >= 0; i--) {
        const item = items[i];

        // Magnet attraction effect
        if (magnetActive && !item.isBoss) {
          const mdx = magnetTargetX - item.x;
          const mdy = magnetTargetY - item.y;
          const mdist = Math.hypot(mdx, mdy);
          if (mdist < 300) {
            item.x += (mdx / mdist) * 220 * dt;
            item.y += (mdy / mdist) * 220 * dt;
          }
        }

        item.y += item.speed * speedMult * dt;
        item.rotation += item.rotSpeed * dt;

        // Store trail positions
        item.trail.unshift({ x: item.x, y: item.y });
        if (item.trail.length > 7) item.trail.pop();

        // Check if item hit the ground (Missed!)
        if (item.y + item.radius >= groundY) {
          items.splice(i, 1);

          if (!item.isPowerup) {
            // Miss 3 items = lose 1 life rule
            streak = 0;
            lastItemCaught = null;
            sameItemCount = 0;
            missAccumulator++;

            sound.playMiss();
            triggerScreenShake();
            createParticleExplosion(item.x, groundY, '#7a2216', 10);
            showFloatingText("MISSED! 💥", item.x, groundY - 20, '#ff4757');

            if (missAccumulator >= 3) {
              missAccumulator = 0;
              lives--;
              updateHUD();
              if (lives <= 0) {
                triggerGameOver();
                return;
              }
            } else {
              updateHUD();
            }
          }
        }
      }

      // Update Particle Explosions
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.alpha -= p.decay;
        if (p.alpha <= 0) particles.splice(i, 1);
      }

      // Update Confetti
      for (let i = confetti.length - 1; i >= 0; i--) {
        const c = confetti[i];
        c.x += c.vx;
        c.y += c.vy;
        c.rotation += c.vRot;
        if (c.y > canvasH + 20) confetti.splice(i, 1);
      }

      // Update Floating Texts
      for (let i = floatingTexts.length - 1; i >= 0; i--) {
        const ft = floatingTexts[i];
        ft.y += ft.vy;
        ft.alpha -= 0.025;
        if (ft.alpha <= 0) floatingTexts.splice(i, 1);
      }
    }

    // 12. CANVAS RENDERING
    function renderGame() {
      ctx.clearRect(0, 0, canvasW, canvasH);

      // Reactive Pulsing Neon Background tied to Fever & High Score
      if (feverActive) {
        ctx.fillStyle = `rgba(255, 0, 127, ${0.12 + Math.sin(performance.now() / 150) * 0.06})`;
        ctx.fillRect(0, 0, canvasW, canvasH);
      }

      // Ground Table Counter
      ctx.fillStyle = 'rgba(74, 25, 12, 0.9)';
      ctx.fillRect(0, canvasH - 50, canvasW, 50);
      ctx.fillStyle = '#ff9933';
      ctx.fillRect(0, canvasH - 52, canvasW, 3);

      // Render Falling Items with Glowing Trails
      items.forEach(item => {
        // Draw Glowing Trail
        if (item.trail.length > 1) {
          ctx.save();
          for (let t = 0; t < item.trail.length; t++) {
            const pt = item.trail[t];
            const ratio = 1 - t / item.trail.length;
            ctx.beginPath();
            ctx.arc(pt.x, pt.y, item.radius * ratio * 0.7, 0, Math.PI * 2);
            ctx.fillStyle = item.config.color;
            ctx.globalAlpha = ratio * 0.35;
            ctx.shadowBlur = 12;
            ctx.shadowColor = item.config.color;
            ctx.fill();
          }
          ctx.restore();
        }

        // Draw Item Body & Icon
        ctx.save();
        ctx.translate(item.x, item.y);
        ctx.rotate(item.rotation);

        // Outer Glow Aura
        ctx.shadowBlur = item.isBoss ? 28 : (feverActive ? 20 : 12);
        ctx.shadowColor = feverActive ? '#ff007f' : item.config.color;

        // Background Circle for visual pop
        ctx.beginPath();
        ctx.arc(0, 0, item.radius, 0, Math.PI * 2);
        ctx.fillStyle = item.isPowerup ? '#1c2833' : 'rgba(25, 5, 10, 0.85)';
        ctx.fill();
        ctx.lineWidth = item.isBoss ? 5 : 3;
        ctx.strokeStyle = item.config.color;
        ctx.stroke();

        // Draw Icon / Emoji
        ctx.shadowBlur = 0;
        ctx.font = `${item.radius * 1.25}px 'Fredoka One', sans-serif`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(item.config.emoji, 0, 2);

        // Power-Up Label ring
        if (item.isPowerup) {
          ctx.font = "9px 'Outfit', sans-serif";
          ctx.fillStyle = "#fff";
          ctx.fillText(item.config.name, 0, item.radius + 12);
        }

        ctx.restore();
      });

      // Render Particles
      particles.forEach(p => {
        ctx.save();
        ctx.globalAlpha = p.alpha;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.shadowBlur = 10;
        ctx.shadowColor = p.color;
        ctx.fill();
        ctx.restore();
      });

      // Render Confetti Rain
      confetti.forEach(c => {
        ctx.save();
        ctx.translate(c.x, c.y);
        ctx.rotate((c.rotation * Math.PI) / 180);
        ctx.fillStyle = c.color;
        ctx.fillRect(-c.size / 2, -c.size / 2, c.size, c.size * 0.6);
        ctx.restore();
      });

      // Render Floating Numbers (+10, +30, FEVER!)
      floatingTexts.forEach(ft => {
        ctx.save();
        ctx.globalAlpha = ft.alpha;
        ctx.font = "bold 22px 'Fredoka One', cursive";
        ctx.textAlign = 'center';
        ctx.fillStyle = ft.color;
        ctx.shadowBlur = 8;
        ctx.shadowColor = '#000';
        ctx.fillText(ft.text, ft.x, ft.y);
        ctx.restore();
      });
    }

    // Initialize Game Engine on Window Load
    window.addEventListener('DOMContentLoaded', () => {
      initCanvas();
      setupEventListeners();
      renderLeaderboard();
      requestAnimationFrame(gameLoop);
    });
  </script>
</body>
</html>
'''

with open('/config/antigravity/focused-davinci/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully generated AAA Hyderabad Rush game into index.html")
