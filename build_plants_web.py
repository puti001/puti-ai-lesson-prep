import os

html_code = """<!DOCTYPE html>
<html lang="zh-TW" data-theme="warm">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Puti-AI | 國小校園植物 ╳ AI 自主探究研究室 - 4~6年級互動教學指南</title>
  <meta name="description" content="屏東縣後庄國小黃朝榮老師專為國小4~6年級設計：校園植物 ╳ NotebookLM ╳ Canva 深度AI人機協作自主研究與發表互動教學平台。">
  
  <!-- Google Fonts: Zen Maru Gothic (日系圓體) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;500;700;900&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    /* ========== 日式暖心美學 Design Tokens ========== */
    :root {
      --bg-body: #FFFDF9;
      --bg-card: #FFFFFF;
      --primary: #FF9F1C;
      --primary-light: #FFE8D6;
      --secondary: #FFBF69;
      --accent: #2EC4B6;
      --accent-light: #E2F8F6;
      --text: #3D352E;
      --text-muted: #7A6F66;
      --border-color: #F0E6DA;
      --shadow: rgba(80, 60, 40, 0.08);
      --shadow-hover: rgba(80, 60, 40, 0.16);
      --banner-gradient: linear-gradient(135deg, #FF9F1C 0%, #FFBF69 100%);
      --card-radius: 28px;
      --pill-radius: 40px;
      --base-font-size: 19px;
    }

    [data-theme="warm"] {
      --bg-body: #FFFDF9;
      --bg-card: #FFFFFF;
      --primary: #FF9F1C;
      --primary-light: #FFF0DF;
      --secondary: #FFBF69;
      --accent: #2EC4B6;
      --accent-light: #E5F9F7;
      --text: #3D352E;
      --text-muted: #7A6F66;
      --border-color: #F3E8DC;
      --shadow: rgba(180, 110, 50, 0.09);
      --banner-gradient: linear-gradient(135deg, #FF9F1C 0%, #FFBF69 100%);
    }

    [data-theme="sky"] {
      --bg-body: #F4F9FD;
      --bg-card: #FFFFFF;
      --primary: #197BBD;
      --primary-light: #E3F2FD;
      --secondary: #64B5F6;
      --accent: #00B4D8;
      --accent-light: #E0F7FA;
      --text: #203A4D;
      --text-muted: #5C768D;
      --border-color: #D9EAF5;
      --shadow: rgba(25, 123, 189, 0.08);
      --banner-gradient: linear-gradient(135deg, #197BBD 0%, #64B5F6 100%);
    }

    [data-theme="sakura"] {
      --bg-body: #FFF7F9;
      --bg-card: #FFFFFF;
      --primary: #F06292;
      --primary-light: #FCE4EC;
      --secondary: #FF80AB;
      --accent: #AB47BC;
      --accent-light: #F3E5F5;
      --text: #422835;
      --text-muted: #855871;
      --border-color: #F8DDE5;
      --shadow: rgba(240, 98, 146, 0.08);
      --banner-gradient: linear-gradient(135deg, #F06292 0%, #FFB2D2 100%);
    }

    [data-theme="forest"] {
      --bg-body: #F5F9F5;
      --bg-card: #FFFFFF;
      --primary: #4CAF50;
      --primary-light: #E8F5E9;
      --secondary: #81C784;
      --accent: #00897B;
      --accent-light: #E0F2F1;
      --text: #263B28;
      --text-muted: #5C775F;
      --border-color: #DCEDDC;
      --shadow: rgba(76, 175, 80, 0.08);
      --banner-gradient: linear-gradient(135deg, #43A047 0%, #81C784 100%);
    }

    body.font-large {
      --base-font-size: 22px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Zen Maru Gothic', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: var(--base-font-size);
      line-height: 1.85;
      letter-spacing: 0.04em;
      background-color: var(--bg-body);
      color: var(--text);
      transition: background-color 0.3s ease, color 0.3s ease;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background: var(--bg-card);
      border-bottom: 2px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 4px 16px var(--shadow);
    }

    .nav-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-icon {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: var(--banner-gradient);
      color: #FFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      box-shadow: 0 4px 12px var(--shadow);
    }

    .brand-text h1 {
      font-size: 1.35rem;
      font-weight: 900;
      color: var(--text);
      line-height: 1.2;
    }

    .brand-text span {
      font-size: 0.95rem;
      color: var(--primary);
      font-weight: 700;
      display: block;
    }

    .controls-group {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .theme-picker {
      display: flex;
      background: var(--bg-body);
      border: 2px solid var(--border-color);
      border-radius: var(--pill-radius);
      padding: 4px;
      gap: 6px;
    }

    .theme-dot {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      cursor: pointer;
      border: 2px solid transparent;
      transition: transform 0.2s, border-color 0.2s;
    }
    .theme-dot:hover { transform: scale(1.15); }
    .theme-dot.active { border-color: var(--text); }
    .theme-dot.warm { background: #FF9F1C; }
    .theme-dot.sky { background: #197BBD; }
    .theme-dot.sakura { background: #F06292; }
    .theme-dot.forest { background: #4CAF50; }

    .btn-toggle-font {
      background: var(--primary-light);
      color: var(--primary);
      border: none;
      font-family: inherit;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 8px 18px;
      border-radius: var(--pill-radius);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .btn-toggle-font:hover {
      background: var(--primary);
      color: #FFF;
      transform: translateY(-2px);
    }

    .hero-banner {
      background: var(--banner-gradient);
      color: #FFFFFF;
      padding: 48px 20px 42px;
      text-align: center;
      border-bottom-left-radius: 40px;
      border-bottom-right-radius: 40px;
      box-shadow: 0 12px 30px var(--shadow);
      margin-bottom: 30px;
    }

    .hero-content {
      max-width: 920px;
      margin: 0 auto;
    }

    .hero-badge {
      display: inline-block;
      background: rgba(255, 255, 255, 0.28);
      backdrop-filter: blur(8px);
      padding: 6px 20px;
      border-radius: var(--pill-radius);
      font-weight: 800;
      font-size: 1.05rem;
      margin-bottom: 12px;
      letter-spacing: 0.06em;
    }

    .hero-title {
      font-size: 2.3rem;
      font-weight: 900;
      line-height: 1.35;
      margin-bottom: 14px;
      text-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
    }

    .hero-desc {
      font-size: 1.2rem;
      opacity: 0.96;
      max-width: 820px;
      margin: 0 auto 22px;
      font-weight: 500;
      line-height: 1.8;
    }

    .hero-metrics {
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .metric-pill {
      background: rgba(255, 255, 255, 0.92);
      color: var(--text);
      padding: 8px 20px;
      border-radius: var(--pill-radius);
      font-weight: 800;
      font-size: 1rem;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .tab-bar {
      max-width: 1120px;
      margin: 0 auto 30px;
      padding: 0 15px;
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .tab-btn {
      background: var(--bg-card);
      border: 2px solid var(--border-color);
      color: var(--text-muted);
      font-family: inherit;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 12px 26px;
      border-radius: var(--pill-radius);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 4px 12px var(--shadow);
      transition: all 0.25s ease;
    }

    .tab-btn:hover {
      transform: translateY(-2px);
      border-color: var(--primary);
      color: var(--primary);
    }

    .tab-btn.active {
      background: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
      box-shadow: 0 8px 22px var(--shadow-hover);
    }

    .main-container {
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 20px 50px;
      flex: 1;
    }

    .tab-pane {
      display: none;
      animation: fadeIn 0.35s ease;
    }
    .tab-pane.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .warm-card {
      background: var(--bg-card);
      border-radius: var(--card-radius);
      border: 2px solid var(--border-color);
      padding: 32px;
      margin-bottom: 26px;
      box-shadow: 0 8px 24px var(--shadow);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .warm-card:hover {
      box-shadow: 0 14px 36px var(--shadow-hover);
    }

    .section-title {
      font-size: 1.65rem;
      font-weight: 900;
      color: var(--text);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .section-title i {
      color: var(--primary);
    }

    .section-desc {
      color: var(--text-muted);
      font-size: 1.12rem;
      margin-bottom: 24px;
      line-height: 1.8;
    }

    .filter-pills {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 22px;
    }

    .filter-btn {
      background: var(--bg-body);
      border: 2px solid var(--border-color);
      color: var(--text-muted);
      font-family: inherit;
      font-size: 0.98rem;
      font-weight: 800;
      padding: 7px 18px;
      border-radius: var(--pill-radius);
      cursor: pointer;
      transition: all 0.2s;
    }
    .filter-btn.active, .filter-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }

    .week-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
      gap: 22px;
    }

    .week-card {
      background: var(--bg-card);
      border-radius: 24px;
      border: 2px solid var(--border-color);
      padding: 24px;
      box-shadow: 0 6px 18px var(--shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .week-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 10px 24px var(--shadow-hover);
    }

    .week-card.completed {
      border-color: var(--accent);
      background: #F6FCFA;
    }

    .week-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }

    .week-number {
      font-size: 0.95rem;
      font-weight: 900;
      padding: 4px 14px;
      border-radius: var(--pill-radius);
      background: var(--primary-light);
      color: var(--primary);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .week-category {
      font-size: 0.9rem;
      font-weight: 800;
      color: var(--text-muted);
    }

    .week-title {
      font-size: 1.3rem;
      font-weight: 900;
      color: var(--text);
      margin-bottom: 10px;
      line-height: 1.4;
    }

    .week-detail {
      font-size: 1.02rem;
      color: var(--text-muted);
      margin-bottom: 16px;
      line-height: 1.7;
    }

    .week-tag-row {
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding-top: 12px;
      border-top: 1px dashed var(--border-color);
      margin-bottom: 16px;
    }

    .tag-item {
      font-size: 0.95rem;
      display: flex;
      align-items: flex-start;
      gap: 8px;
      line-height: 1.6;
    }
    .tag-item i {
      margin-top: 4px;
      font-size: 0.9rem;
    }
    .tag-human { color: #C65A15; }
    .tag-ai { color: var(--accent); }

    .check-btn {
      width: 100%;
      background: var(--bg-body);
      border: 2px solid var(--border-color);
      color: var(--text);
      font-family: inherit;
      font-weight: 800;
      padding: 10px;
      border-radius: var(--pill-radius);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-size: 1rem;
      transition: all 0.2s;
    }
    .check-btn:hover {
      background: var(--accent-light);
      color: var(--accent);
      border-color: var(--accent);
    }
    .week-card.completed .check-btn {
      background: var(--accent);
      color: #FFF;
      border-color: var(--accent);
    }

    .prompt-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 22px;
    }

    .prompt-card {
      background: var(--bg-card);
      border-radius: 24px;
      border: 2px solid var(--border-color);
      padding: 26px;
      box-shadow: 0 6px 18px var(--shadow);
    }

    .prompt-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 12px;
    }

    .prompt-title-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .prompt-icon {
      width: 44px;
      height: 44px;
      border-radius: 14px;
      background: var(--primary-light);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
    }

    .prompt-title {
      font-size: 1.35rem;
      font-weight: 900;
    }

    .prompt-box {
      background: var(--bg-body);
      border: 2px solid var(--border-color);
      border-radius: 18px;
      padding: 18px;
      font-size: 1.08rem;
      line-height: 1.8;
      color: var(--text);
      white-space: pre-wrap;
      font-family: inherit;
      margin-bottom: 14px;
    }

    .btn-copy {
      background: var(--primary);
      color: #FFF;
      border: none;
      font-family: inherit;
      font-weight: 800;
      padding: 9px 22px;
      border-radius: var(--pill-radius);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 1rem;
      transition: all 0.2s;
      box-shadow: 0 4px 10px var(--shadow);
    }
    .btn-copy:hover {
      background: var(--secondary);
      transform: translateY(-2px);
    }

    .generator-grid {
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 26px;
    }
    @media (max-width: 900px) {
      .generator-grid { grid-template-columns: 1fr; }
    }

    .form-group {
      margin-bottom: 18px;
    }

    .form-label {
      font-weight: 900;
      font-size: 1.12rem;
      margin-bottom: 8px;
      display: block;
      color: var(--text);
    }

    .form-input, .form-textarea {
      width: 100%;
      background: var(--bg-body);
      border: 2px solid var(--border-color);
      border-radius: 18px;
      padding: 14px 18px;
      font-family: inherit;
      font-size: 1.05rem;
      color: var(--text);
      transition: border-color 0.2s;
    }
    .form-input:focus, .form-textarea:focus {
      outline: none;
      border-color: var(--primary);
      background: #FFF;
    }

    .form-textarea {
      resize: vertical;
      min-height: 100px;
    }

    .btn-generate {
      width: 100%;
      background: var(--banner-gradient);
      color: #FFF;
      border: none;
      font-family: inherit;
      font-weight: 900;
      font-size: 1.25rem;
      padding: 15px;
      border-radius: var(--pill-radius);
      cursor: pointer;
      box-shadow: 0 6px 16px var(--shadow);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all 0.2s;
    }
    .btn-generate:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 22px var(--shadow-hover);
    }

    .preview-box {
      background: var(--bg-body);
      border: 2px dashed var(--border-color);
      border-radius: 22px;
      padding: 22px;
      min-height: 420px;
      font-size: 1.05rem;
      line-height: 1.85;
      white-space: pre-wrap;
    }

    .timer-card {
      text-align: center;
      max-width: 640px;
      margin: 0 auto;
      padding: 40px 26px;
    }

    .timer-display {
      font-size: 5.5rem;
      font-weight: 900;
      color: var(--primary);
      line-height: 1;
      margin: 22px 0;
      font-variant-numeric: tabular-nums;
    }

    .timer-progress-bg {
      width: 100%;
      height: 18px;
      background: var(--border-color);
      border-radius: var(--pill-radius);
      overflow: hidden;
      margin-bottom: 26px;
    }

    .timer-progress-bar {
      width: 100%;
      height: 100%;
      background: var(--banner-gradient);
      border-radius: var(--pill-radius);
      transition: width 1s linear;
    }

    .timer-controls {
      display: flex;
      justify-content: center;
      gap: 16px;
      margin-bottom: 26px;
    }

    .timer-btn {
      font-family: inherit;
      font-size: 1.15rem;
      font-weight: 900;
      padding: 13px 30px;
      border-radius: var(--pill-radius);
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 4px 12px var(--shadow);
      transition: all 0.2s;
    }
    .timer-btn-primary {
      background: var(--primary);
      color: #FFF;
    }
    .timer-btn-secondary {
      background: var(--bg-body);
      border: 2px solid var(--border-color);
      color: var(--text);
    }
    .timer-btn:hover {
      transform: translateY(-2px);
    }

    .speech-tips {
      background: var(--primary-light);
      border-radius: 20px;
      padding: 18px 24px;
      text-align: left;
      font-size: 1.05rem;
      color: var(--text);
      line-height: 1.8;
    }

    .toast-msg {
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: #2D3748;
      color: #FFF;
      padding: 14px 26px;
      border-radius: var(--pill-radius);
      font-size: 1.05rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 999;
    }
    .toast-msg.show {
      transform: translateY(0);
      opacity: 1;
    }

    footer {
      text-align: center;
      padding: 35px 20px;
      font-size: 1.05rem;
      color: #665E55;
      background: var(--bg-card);
      border-top: 2px solid var(--border-color);
      margin-top: auto;
    }
    footer a {
      color: var(--primary);
      font-weight: 800;
      text-decoration: none;
    }
    footer a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <!-- ========== 頂部導航 ========== -->
  <header>
    <div class="nav-container">
      <div class="brand-group">
        <div class="brand-icon">
          <i class="fa-solid fa-seedling"></i>
        </div>
        <div class="brand-text">
          <h1>Puti-AI 校園植物研究室</h1>
          <span>4～6年級自主研究 ╳ AI人機協作教學指南</span>
        </div>
      </div>

      <div class="controls-group">
        <div class="theme-picker" title="切換暖心粉彩主題">
          <div class="theme-dot warm active" onclick="setTheme('warm')"></div>
          <div class="theme-dot sky" onclick="setTheme('sky')"></div>
          <div class="theme-dot sakura" onclick="setTheme('sakura')"></div>
          <div class="theme-dot forest" onclick="setTheme('forest')"></div>
        </div>

        <button class="btn-toggle-font" onclick="toggleFontSize()" id="fontToggleBtn">
          <i class="fa-solid fa-text-height"></i>
          <span>切換超大字</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ========== 主視覺橫幅 ========== -->
  <section class="hero-banner">
    <div class="hero-content">
      <span class="hero-badge">🌿 國小中高年級 PBL ╳ 深度人機協作實戰</span>
      <h2 class="hero-title">告別無趣百科！讓校園樹木成為發表主角</h2>
      <p class="hero-desc">
        真實世界親手採集 ➔ 丟進 NotebookLM 打造知識大腦 ➔ Canva 設計超美小書與海報 ➔ 60秒流暢導覽發表！零回家作業，社團課內高效閉環。
      </p>
      <div class="hero-metrics">
        <div class="metric-pill"><i class="fa-solid fa-calendar-check" style="color:#FF9F1C;"></i> 17次精準課程時程</div>
        <div class="metric-pill"><i class="fa-solid fa-brain" style="color:#2EC4B6;"></i> NotebookLM 來源對談</div>
        <div class="metric-pill"><i class="fa-solid fa-palette" style="color:#E91E63;"></i> Canva 視覺小書海報</div>
        <div class="metric-pill"><i class="fa-solid fa-microphone-lines" style="color:#4CAF50;"></i> 實體解說與發表演練</div>
      </div>
    </div>
  </section>

  <!-- ========== 分頁導覽按鈕 ========== -->
  <nav class="tab-bar">
    <button class="tab-btn active" onclick="switchTab('roadmap')">
      <i class="fa-solid fa-route"></i>
      <span>17 週探究地圖</span>
    </button>
    <button class="tab-btn" onclick="switchTab('prompts')">
      <i class="fa-solid fa-wand-magic-sparkles"></i>
      <span>AI 咒語神隊友</span>
    </button>
    <button class="tab-btn" onclick="switchTab('generator')">
      <i class="fa-solid fa-book-open"></i>
      <span>小書與海報產生器</span>
    </button>
    <button class="tab-btn" onclick="switchTab('timer')">
      <i class="fa-solid fa-stopwatch-20"></i>
      <span>60 秒導覽演練器</span>
    </button>
  </nav>

  <!-- ========== 核心內容主區 ========== -->
  <main class="main-container">

    <!-- ==================== Tab 1: 17 週探究地圖 ==================== -->
    <div id="pane-roadmap" class="tab-pane active">
      <div class="warm-card">
        <div class="section-title">
          <i class="fa-solid fa-compass"></i>
          <span>17 週進度與自主管理任務卡</span>
        </div>
        <p class="section-desc">
          每週 2 節課（80 分鐘）當堂搞定！戶外採樣快速收工，重心放在 NotebookLM 提煉資料、Canva 深度視覺製作與老師親自精修發表演練。
        </p>

        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px;">
          <div class="filter-pills">
            <button class="filter-btn active" onclick="filterWeeks('all', this)">全部 17 次</button>
            <button class="filter-btn" onclick="filterWeeks('戶外極速採樣', this)">戶外採樣</button>
            <button class="filter-btn" onclick="filterWeeks('NotebookLM 提煉', this)">NotebookLM 提煉</button>
            <button class="filter-btn" onclick="filterWeeks('Canva 視覺產出', this)">Canva 小書海報</button>
            <button class="filter-btn" onclick="filterWeeks('發表精修與彩排', this)">發表精修彩排</button>
            <button class="filter-btn" onclick="filterWeeks('成果發表與結案', this)">成果展現結案</button>
          </div>
          <div style="font-weight:800; font-size:1.1rem; color:var(--primary);" id="progressDisplay">
            目前完成進度：0 / 17 次 (0%)
          </div>
        </div>

        <div class="week-grid" id="weekGridContainer"></div>
      </div>
    </div>

    <!-- ==================== Tab 2: AI 咒語神隊友 ==================== -->
    <div id="pane-prompts" class="tab-pane">
      <div class="warm-card">
        <div class="section-title">
          <i class="fa-solid fa-robot"></i>
          <span>專屬國小高年級：人機協作提示詞庫</span>
        </div>
        <p class="section-desc">
          在電腦教室打開 NotebookLM 或 ChatGPT，點擊「一鍵複製」咒語，替換掉括號內的校園植物名稱，立刻獲得高水準的內容支援！
        </p>

        <div class="prompt-grid">
          <div class="prompt-card">
            <div class="prompt-header">
              <div class="prompt-title-group">
                <div class="prompt-icon"><i class="fa-solid fa-comments"></i></div>
                <div>
                  <h3 class="prompt-title">咒語一：樹木擬人化訪談（跟樹聊聊天）</h3>
                  <small style="color:var(--text-muted);">使用工具：NotebookLM / ChatGPT ｜ 時機：第 2~3 次課</small>
                </div>
              </div>
              <button class="btn-copy" onclick="copyPrompt('prompt-1')">
                <i class="fa-regular fa-copy"></i> 複製咒語
              </button>
            </div>
            <div class="prompt-box" id="prompt-1">你現在是我們學校操場旁的「［填入植物名稱，如：大葉欖仁］」，已經在學校活了超過 20 年。請用幽默、有點傲嬌但親切的口氣回答我接下來的 3 個問題，每次回答不要超過 80 個字，並且要讓國小四年級學生覺得超級好笑又學得到東西：
1. 每天看我們下課在操場跑步，你心裡最常想什麼？
2. 你身上最厲害的「超能力」（防蟲、防風或變色技巧）是什麼？
3. 如果你可以對全校學生說一句話，你想大喊什麼？</div>
          </div>

          <div class="prompt-card">
            <div class="prompt-header">
              <div class="prompt-title-group">
                <div class="prompt-icon"><i class="fa-solid fa-book"></i></div>
                <div>
                  <h3 class="prompt-title">咒語二：提煉 6 頁冒險小書章節腳本</h3>
                  <small style="color:var(--text-muted);">使用工具：NotebookLM ｜ 時機：第 4 次課</small>
                </div>
              </div>
              <button class="btn-copy" onclick="copyPrompt('prompt-2')">
                <i class="fa-regular fa-copy"></i> 複製咒語
              </button>
            </div>
            <div class="prompt-box" id="prompt-2">請根據我上傳的［校園樹木觀察筆記與照片手稿］，幫我們這組規劃一本 6 頁的「校園植物冒險小書」內容。
請為每一頁設計：
1. 一個吸引人的【趣味副標題】
2. 一段 50 字以內的【解說內文】（白話、生動、拒絕死板維基百科）
3. 一個【插圖建議】（告訴我們在 Canva 可以放什麼照片或插圖）

6 頁章節分配如下：
- 第 1 頁：封面與我的檔案密碼
- 第 2 頁：我的超帥身體構造（葉片與樹幹）
- 第 3 頁：我的神奇生理超能力（耐旱、落葉或防禦）
- 第 4 頁：誰住在我的樹冠上？（微生態住客）
- 第 5 頁：校園不可不知的 3 大驚奇冷知識
- 第 6 頁：給守護這棵樹的小朋友一句真心話</div>
          </div>

          <div class="prompt-card">
            <div class="prompt-header">
              <div class="prompt-title-group">
                <div class="prompt-icon"><i class="fa-solid fa-file-powerpoint"></i></div>
                <div>
                  <h3 class="prompt-title">咒語三：5 頁簡報大綱與台上台詞</h3>
                  <small style="color:var(--text-muted);">使用工具：NotebookLM / Canva Magic ｜ 時機：第 9 次課</small>
                </div>
              </div>
              <button class="btn-copy" onclick="copyPrompt('prompt-3')">
                <i class="fa-regular fa-copy"></i> 複製咒語
              </button>
            </div>
            <div class="prompt-box" id="prompt-3">我們要製作 5 頁的發表簡報，對象是全校師生。請根據我們的資料，為每一頁簡報規劃：
1. 【投影片大標題】（不超過 8 個字，要有吸睛點）
2. 【投影片畫面內容】（只要 2 個列點關鍵字，嚴禁長篇大論）
3. 【演講者台詞提示】（給我們上台拿麥克風時說的 2 句話，口語化、有自信）</div>
          </div>

          <div class="prompt-card">
            <div class="prompt-header">
              <div class="prompt-title-group">
                <div class="prompt-icon"><i class="fa-solid fa-shield-halved"></i></div>
                <div>
                  <h3 class="prompt-title">咒語四：模擬考官提問（防被問倒演練）</h3>
                  <small style="color:var(--text-muted);">使用工具：NotebookLM / ChatGPT ｜ 時機：第 13 次課</small>
                </div>
              </div>
              <button class="btn-copy" onclick="copyPrompt('prompt-4')">
                <i class="fa-regular fa-copy"></i> 複製咒語
              </button>
            </div>
            <div class="prompt-box" id="prompt-4">我們研究的主題是［學校操場旁的大葉欖仁］。
請你現在扮演一位「既幽默但又非常嚴格的國小自然科校長」，閱讀我們目前的資料後，提出 2 個觀眾最可能會好奇、或是很有挑戰性的問題來考考我們。
請先只給我們問題，等我們回答後，再幫我們打分數並提供完美的回答建議！</div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== Tab 3: 小書與海報產生器 ==================== -->
    <div id="pane-generator" class="tab-pane">
      <div class="warm-card">
        <div class="section-title">
          <i class="fa-solid fa-wand-magic-sparkles"></i>
          <span>小書與海報「文字骨架一鍵產生器」</span>
        </div>
        <p class="section-desc">
          寫不出句子？沒關係！在左邊填入你們採集到的關鍵字，點擊產生，系統立刻幫你們轉化為 6 頁小書完整草稿與展覽看板 3 大亮點！
        </p>

        <div class="generator-grid">
          <div>
            <div class="form-group">
              <label class="form-label">🌱 植物名稱（必填）</label>
              <input type="text" id="genName" class="form-input" placeholder="例如：大葉欖仁、黑板樹、榕樹、艷紫荊" value="大葉欖仁">
            </div>
            <div class="form-group">
              <label class="form-label">📍 校園所在地點</label>
              <input type="text" id="genLoc" class="form-input" placeholder="例如：西棟大樓旁、司令台後方草地" value="操場司令台西側">
            </div>
            <div class="form-group">
              <label class="form-label">📏 測量數據（樹圍與葉片特徵）</label>
              <input type="text" id="genData" class="form-input" placeholder="例如：樹胸圍 115 公分、落葉長約 22 公分、葉子倒卵形" value="樹圍 120 公分，葉片長達 25 公分，葉片厚實光滑">
            </div>
            <div class="form-group">
              <label class="form-label">✨ 最驚訝的觀察或冷知識</label>
              <textarea id="genFunFact" class="form-textarea" placeholder="例如：冬天葉子變紅是因為植物防曬油、葉柄互勾拔河超難斷！">冬天葉子變紅像楓葉一樣，是因為花青素保護葉片；葉柄超級粗壯，在落葉拔河賽中拿下了全校第一名！</textarea>
            </div>
            <button class="btn-generate" onclick="generateBookDraft()">
              <i class="fa-solid fa-wand-magic-sparkles"></i> 一鍵生成小書與海報文案
            </button>
          </div>

          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <span style="font-weight:900; font-size:1.1rem; color:var(--text);">📄 生成結果預覽（可複製到 Canva）</span>
              <button class="btn-copy" style="padding:6px 16px; font-size:0.95rem;" onclick="copyGeneratedDraft()">
                <i class="fa-regular fa-copy"></i> 複製全部文案
              </button>
            </div>
            <div class="preview-box" id="draftOutput">點擊左側「一鍵生成」按鈕，立即產出專屬小書 6 頁文字稿與海報文案！</div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== Tab 4: 60 秒導覽演練器 ==================== -->
    <div id="pane-timer" class="tab-pane">
      <div class="warm-card">
        <div class="section-title">
          <i class="fa-solid fa-stopwatch"></i>
          <span>發表實戰：60 秒導覽黃金計時器</span>
        </div>
        <p class="section-desc">
          上台發表最忌諱講太長或死背課本！每人精準 60 秒，介紹 1 個核心亮點。戴上耳機或大聲計時，練習一分鐘定點解說！
        </p>

        <div class="timer-card">
          <div style="font-size:1.3rem; font-weight:800; color:var(--text-muted);\" id="timerPhase">
            準備就緒，請深呼吸～
          </div>

          <div class="timer-display" id="timerDisplay">60</div>

          <div class="timer-progress-bg">
            <div class="timer-progress-bar" id="timerBar"></div>
          </div>

          <div class="timer-controls">
            <button class="timer-btn timer-btn-primary" id="btnTimerStart" onclick="toggleTimer()">
              <i class="fa-solid fa-play"></i> 開始計時
            </button>
            <button class="timer-btn timer-btn-secondary" onclick="resetTimer()">
              <i class="fa-solid fa-rotate-left"></i> 重置 60 秒
            </button>
          </div>

          <div class="speech-tips">
            <h4 style="font-weight:900; margin-bottom:8px; color:var(--primary); font-size:1.15rem;">
              🎤 導覽員上台必勝 3 大心法：
            </h4>
            <p>1. <strong>眼神看觀眾</strong>：不要一直低頭看簡報或地板，找前排兩位同學對視。</p>
            <p>2. <strong>手勢指亮點</strong>：說到哪張照片，手就平平地比向螢幕，自信大方。</p>
            <p>3. <strong>聲音像說秘密</strong>：「大家知道嗎？這棵樹其實有個不可思議的秘密...」開場最吸引人！</p>
          </div>
        </div>
      </div>
    </div>

  </main>

  <div class="toast-msg" id="toastBox">
    <i class="fa-solid fa-circle-check" style="color:#4CAF50;"></i>
    <span id="toastText">已成功複製到剪貼簿！</span>
  </div>

  <!-- ========== 頁尾版權宣告區 ========== -->
  <footer>
    屏東縣後庄國小黃朝榮老師作品，免費分享，歡迎擴散推廣，嚴禁商用與任何侵權、不尊重著作權的行為，更多 Puti-AI 教學工具 <a href="https://padlet.com/clongwh/puti_ai_tools" target="_blank">點此前往</a>
  </footer>

  <script>
    const WEEKS_DATA = [
      {
        num: 1,
        cat: '戶外極速採樣',
        title: '校園極速踏查與拍齊 4 視角',
        detail: '帶平板/手機衝操場，各組認領 1 棵目標樹。拍齊「全貌、樹皮、葉片、花果」高清照，撿 5 片落葉回電腦教室。',
        human: '戶外拍照、量樹胸圍、採集落葉',
        ai: 'Google Lens 拍照辨識學名科屬',
      },
      {
        num: 2,
        cat: '戶外極速採樣',
        title: '電腦教室建立研究手稿',
        detail: '將拍好的照片上傳電腦，打字記錄樹圍、地點與第一印象，匯出成第一份「原始研究手稿 PDF」。',
        human: '整理照片、輸入量測數字',
        ai: '協助將雜亂筆記格式化排版',
      },
      {
        num: 3,
        cat: 'NotebookLM 提煉',
        title: '導入 NotebookLM：跟樹聊聊天',
        detail: '將研究手稿丟入 NotebookLM 作為來源。進行「樹木擬人化訪談」，發掘樹木在學校的趣味回憶。',
        human: '發想訪談題目、挑選最佳對答',
        ai: '扮演百年老樹進行幽默對話',
      },
      {
        num: 4,
        cat: 'NotebookLM 提煉',
        title: '提煉小書大綱與 3 大冷知識',
        detail: '利用咒語讓 NotebookLM 一鍵產出 6 頁小書的章節腳本，並找出全校沒人知道的 3 個校園植物冷知識。',
        human: '核對學校真實環境、篩選金句',
        ai: '濃縮長篇百科為 50 字精華',
      },
      {
        num: 5,
        cat: 'Canva 視覺產出',
        title: 'Canva 啟航：小書封面與前 2 頁',
        detail: '登入 Canva 套用 A5 小書折頁範本。今天只專心完成「超美封面」與「第 1~2 頁身家密碼」。',
        human: '排版照片、挑選圓體與主色調',
        ai: 'Canva Magic Design 智慧配色',
      },
      {
        num: 6,
        cat: 'Canva 視覺產出',
        title: 'Canva 小書製作：補齊 3～6 頁',
        detail: '排入生理超能力、微生態觀察與冷知識。用 Canva 內建 AI 生成樹木吉祥物插圖補強視覺。',
        human: '手動微調字距、排列圖文對齊',
        ai: '生成植物擬人化 Q 版插圖',
      },
      {
        num: 7,
        cat: 'Canva 視覺產出',
        title: 'Canva 小書定稿與老師檢核',
        detail: '老師逐組檢視版面：統一字級大小（確保印出來字不會太小），修正圖片跑版，匯出印刷高解析 PDF。',
        human: '修正錯字、檢查排版層次',
        ai: '自動偵測字體對比度與版面間距',
      },
      {
        num: 8,
        cat: 'Canva 視覺產出',
        title: '展覽看板海報與解說牌設計',
        detail: '從小書素材一鍵轉化為 A3 展覽海報。將文字再次精簡為「大字號、大照片、3個醒目條列」。',
        human: '設計遠距離一眼看懂的海報主視覺',
        ai: '一鍵濃縮文案為海報吸睛標語',
      },
      {
        num: 9,
        cat: 'Canva 視覺產出',
        title: 'NotebookLM 轉簡報 5 頁骨架',
        detail: '輸入咒語生成 5 頁簡報大標題與台詞。進 Canva 套用清新簡報範本，各組認領頁面貼字貼圖。',
        human: '替換為校園真實拍攝照片',
        ai: '生成 5 頁簡報條列式骨架',
      },
      {
        num: 10,
        cat: 'Canva 視覺產出',
        title: '錄製 30 秒語音與生成 QR Code',
        detail: '對電腦麥克風錄製 30 秒導覽短音訊，轉成專屬 QR Code 貼進海報尾頁與小書封底。',
        human: '錄音、彩色列印海報初版',
        ai: '產出含樹木 Logo 的彩色 QR Code',
      },
      {
        num: 11,
        cat: '發表精修與彩排',
        title: '發表精修 1：砍字與製作演講小卡',
        detail: '老師逐組修簡報：嚴格砍掉投影片上的大段文字，指導學生手寫「防忘詞演講小卡」，每頁只記 2 關鍵字。',
        human: '大刀闊斧刪除冗贅文字、製作手卡',
        ai: '將複雜句子轉為口語化提示詞',
      },
      {
        num: 12,
        cat: '發表精修與彩排',
        title: '發表精修 2：台風手勢與視線訓練',
        detail: '電腦教室內半場演練：持麥克風高度、不看螢幕看觀眾、指示照片時的開合手勢、按翻頁筆的節奏。',
        human: '組員互相計時、抓出說「然後」的次數',
        ai: '提供口條流暢度自主檢核清單',
      },
      {
        num: 13,
        cat: '發表精修與彩排',
        title: 'NotebookLM 模擬考官刁難提問',
        detail: '讓 NotebookLM 扮演挑剔的自然科校長，拋出 2 個冷門問題。學生演練「臨場被問倒時的應變話術」。',
        human: '模擬應答：「謝謝校長提問，這點我們發現...」',
        ai: '扮演嚴肅評審進行壓力測試',
      },
      {
        num: 14,
        cat: '發表精修與彩排',
        title: '全流程總彩排（計時大驗收）',
        detail: '正式發表模擬：每組限時 3 分鐘，計時器響起立刻鞠躬下台，老師給予最後修訂微調。',
        human: '全流程不中斷演練、掌控時間',
        ai: '統計發表時間精準度',
      },
      {
        num: 15,
        cat: '成果發表與結案',
        title: '實體加工：小書折頁與海報護貝',
        detail: '彩色輸出成果動手加工：折小書、雙面護貝海報、四角打孔穿上棉繩，佈置發表現場展台。',
        human: '美工裁切、打孔穿繩、布展',
        ai: '確認 QR Code 掃描與連結暢通',
      },
      {
        num: 16,
        cat: '成果發表與結案',
        title: '「校園植物 AI 博覽會」公開發表',
        detail: '盛大發表日！邀請主任與隔壁班同學。台上投影 Canva 簡報發表，台下擺設展台供翻閱小書與掃描。',
        human: '自信登台解說、接待參觀來賓',
        ai: '雲端語音導覽同時在線提供服務',
      },
      {
        num: 17,
        cat: '成果發表與結案',
        title: '樹下正式掛牌儀式與專案結案',
        detail: '帶隊走到該植物現場，用彈性魔鬼氈將解說牌固定在樹上！回教室回顧紀錄照片、頒發小小植物學家證書。',
        human: '正式掛牌、心得反思、吃點心結業',
        ai: '協助將心得筆記生成個人學習歷程',
      }
    ];

    let userProgress = {};
    try {
      userProgress = JSON.parse(localStorage.getItem('puti_plant_progress') || '{}');
    } catch(e) { userProgress = {}; }

    function saveProgress() {
      try {
        localStorage.setItem('puti_plant_progress', JSON.stringify(userProgress));
      } catch(e){}
    }

    function renderWeekCards(filter = 'all') {
      const container = document.getElementById('weekGridContainer');
      if (!container) return;

      const filtered = filter === 'all' 
        ? WEEKS_DATA 
        : WEEKS_DATA.filter(item => item.cat === filter);

      container.innerHTML = filtered.map(item => {
        const isDone = !!userProgress[item.num];
        return `
          <div class="week-card ${isDone ? 'completed' : ''}" id="card-week-${item.num}">
            <div>
              <div class="week-header">
                <span class="week-number"><i class="fa-regular fa-clock"></i> 第 ${item.num < 10 ? '0' + item.num : item.num} 次課</span>
                <span class="week-category">${item.cat}</span>
              </div>
              <h4 class="week-title">${item.title}</h4>
              <p class="week-detail">${item.detail}</p>
              
              <div class="week-tag-row">
                <div class="tag-item tag-human">
                  <i class="fa-solid fa-user-check"></i>
                  <span><strong>學生動手：</strong>${item.human}</span>
                </div>
                <div class="tag-item tag-ai">
                  <i class="fa-solid fa-sparkles"></i>
                  <span><strong>AI 賦能：</strong>${item.ai}</span>
                </div>
              </div>
            </div>

            <button class="check-btn" onclick="toggleWeekCheck(${item.num})">
              <i class="fa-solid ${isDone ? 'fa-circle-check' : 'fa-circle'}"></i>
              <span>${isDone ? '已完成本週任務！' : '標記為完成'}</span>
            </button>
          </div>
        `;
      }).join('');

      updateProgressDisplay();
    }

    function toggleWeekCheck(num) {
      userProgress[num] = !userProgress[num];
      saveProgress();
      renderWeekCards(currentFilter);
      if (userProgress[num]) {
        triggerConfetti();
        showToast(`🎉 太棒了！已完成第 ${num} 次課程任務！`);
      }
    }

    let currentFilter = 'all';
    function filterWeeks(category, btn) {
      currentFilter = category;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderWeekCards(category);
    }

    function updateProgressDisplay() {
      let count = 0;
      WEEKS_DATA.forEach(w => {
        if (userProgress[w.num]) count++;
      });
      const percent = Math.round((count / 17) * 100);
      const display = document.getElementById('progressDisplay');
      if (display) {
        display.innerText = `目前完成進度：${count} / 17 次 (${percent}%)`;
      }
    }

    function switchTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));

      const targetPane = document.getElementById(`pane-${tabId}`);
      if (targetPane) targetPane.classList.add('active');

      const activeBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick')?.includes(tabId));
      if (activeBtn) activeBtn.classList.add('active');

      window.scrollTo({ top: 400, behavior: 'smooth' });
    }

    function setTheme(themeName) {
      document.documentElement.setAttribute('data-theme', themeName);
      document.querySelectorAll('.theme-dot').forEach(d => {
        d.classList.toggle('active', d.classList.contains(themeName));
      });
      showToast(`已切換為「${getThemeName(themeName)}」粉彩主題`);
    }

    function getThemeName(t) {
      switch(t) {
        case 'warm': return '暖日橘';
        case 'sky': return '晴空藍';
        case 'sakura': return '櫻花粉';
        case 'forest': return '青草綠';
        default: return '經典';
      }
    }

    function toggleFontSize() {
      const body = document.body;
      const isLarge = body.classList.toggle('font-large');
      const btnSpan = document.querySelector('#fontToggleBtn span');
      if (btnSpan) {
        btnSpan.innerText = isLarge ? '還原標準字' : '切換超大字';
      }
      showToast(isLarge ? '已啟用「超大字號」護眼模式！' : '已恢復「標準字號」模式');
    }

    function copyPrompt(id) {
      const el = document.getElementById(id);
      if (!el) return;
      navigator.clipboard.writeText(el.innerText).then(() => {
        showToast('📋 AI 咒語已成功複製！可直接貼進 NotebookLM 或 ChatGPT');
      }).catch(() => {
        showToast('複製失敗，請手動選取');
      });
    }

    function generateBookDraft() {
      const name = document.getElementById('genName').value.trim() || '校園植物主角';
      const loc = document.getElementById('genLoc').value.trim() || '校園角落';
      const data = document.getElementById('genData').value.trim() || '葉片茂盛，樹圍粗壯';
      const fact = document.getElementById('genFunFact').value.trim() || '它在校園默默陪伴大家成長，充滿生命力！';

      const draft = `【📖 Puti-AI 校園植物小書：${name} 的冒險秘密】\n\n` +
        `■ 第 1 頁（封面）：\n` +
        `【主標題】校園綠巨人！${name} 的身家解密手冊\n` +
        `【副標題】住在「${loc}」的神秘居民\n` +
        `【研究小組】後庄國小植物特警隊 著\n\n` +
        `■ 第 2 頁（身體密碼）：\n` +
        `【標題】不可思議的身材秘密！\n` +
        `【內文】我們親手拿捲尺測量，發現這棵 ${name} 的${data}。每一片葉子都像是天然的遮陽傘，在校園裡為大家擋風遮雨。\n\n` +
        `■ 第 3 頁（生存超能力）：\n` +
        `【標題】我有超強適應力！\n` +
        `【內文】不管是烈日直曬還是大雨傾盆，${name} 都能牢牢抓住泥土。它的葉片表面有特殊的微結構，水滴滴在上面會形成圓滾滾的水珠！\n\n` +
        `■ 第 4 頁（微生態鄰居）：\n` +
        `【標題】熱鬧的樹冠小公寓！\n` +
        `【內文】拿放大鏡仔細看，樹皮上有青苔與地衣，枝椏間偶爾有鳥雀停留覓食。這棵大樹不只是一棵植物，更是一座小型生態樂園！\n\n` +
        `■ 第 5 頁（驚奇冷知識）：\n` +
        `【標題】連老師都不知道的 3 大冷知識！\n` +
        `1. ${fact}\n` +
        `2. 只要觀察它的落葉顏色與厚度，就能推測最近天氣的乾濕變化！\n` +
        `3. 在落葉拔河大賽中，它的葉柄韌度遠超乎想像！\n\n` +
        `■ 第 6 頁（給人類的悄悄話）：\n` +
        `【標題】謝謝你們停下腳步看我！\n` +
        `【內文】「下次下課經過${loc}時，別忘了抬頭跟我打個招呼喔！」—— 掃描封底 QR Code，聽聽我們親口錄製的 30 秒聲音導覽！\n\n` +
        `----------------------------------------\n` +
        `【🎨 展覽看板海報 3 大排版重點】：\n` +
        `1. 巨型大標：【學校最神秘的綠色朋友：${name}】\n` +
        `2. 核心照片：放上 4 視角拼圖（全貌、樹幹、葉片、花果）\n` +
        `3. 互動焦點：附上專屬語音導覽 QR Code，邀請觀眾現場拿起手機掃描！`;

      document.getElementById('draftOutput').innerText = draft;
      showToast('✨ 小書 6 頁完整草稿與海報重點生成成功！');
      triggerConfetti();
    }

    function copyGeneratedDraft() {
      const text = document.getElementById('draftOutput').innerText;
      if (!text || text.includes('點擊左側')) {
        showToast('請先填寫資料並點擊一鍵生成！');
        return;
      }
      navigator.clipboard.writeText(text).then(() => {
        showToast('📋 小書草稿文案已複製！可直接貼進 Canva 排版');
      });
    }

    let timerDuration = 60;
    let timerRemaining = 60;
    let timerInterval = null;
    let isTimerRunning = false;

    function toggleTimer() {
      if (isTimerRunning) {
        pauseTimer();
      } else {
        startTimer();
      }
    }

    function startTimer() {
      if (timerRemaining <= 0) timerRemaining = 60;
      isTimerRunning = true;
      document.getElementById('btnTimerStart').innerHTML = '<i class="fa-solid fa-pause"></i> 暫停計時';
      document.getElementById('timerPhase').innerText = '🎤 演練中！深呼吸，放慢速度，看著觀眾～';

      timerInterval = setInterval(() => {
        timerRemaining--;
        updateTimerDisplay();

        if (timerRemaining <= 0) {
          clearInterval(timerInterval);
          isTimerRunning = false;
          document.getElementById('btnTimerStart').innerHTML = '<i class="fa-solid fa-play"></i> 重新開始';
          document.getElementById('timerPhase').innerText = '🎉 60秒時間到！漂亮收尾！';
          triggerConfetti();
          showToast('🔔 60 秒發表演練完成！請組員給予肯定回饋！');
        }
      }, 1000);
    }

    function pauseTimer() {
      clearInterval(timerInterval);
      isTimerRunning = false;
      document.getElementById('btnTimerStart').innerHTML = '<i class="fa-solid fa-play"></i> 繼續計時';
      document.getElementById('timerPhase').innerText = '⏸️ 目前已暫停';
    }

    function resetTimer() {
      clearInterval(timerInterval);
      isTimerRunning = false;
      timerRemaining = 60;
      updateTimerDisplay();
      document.getElementById('btnTimerStart').innerHTML = '<i class="fa-solid fa-play"></i> 開始計時';
      document.getElementById('timerPhase').innerText = '準備就緒，請深呼吸～';
    }

    function updateTimerDisplay() {
      const display = document.getElementById('timerDisplay');
      const bar = document.getElementById('timerBar');
      if (display) display.innerText = timerRemaining;
      if (bar) {
        const pct = (timerRemaining / timerDuration) * 100;
        bar.style.width = `${pct}%`;
      }
    }

    function triggerConfetti() {
      if (typeof confetti === 'function') {
        confetti({
          particleCount: 50,
          spread: 60,
          origin: { y: 0.8 }
        });
      }
    }

    function showToast(msg) {
      const box = document.getElementById('toastBox');
      const text = document.getElementById('toastText');
      if (!box || !text) return;
      text.innerText = msg;
      box.classList.add('show');
      setTimeout(() => {
        box.classList.remove('show');
      }, 3000);
    }

    window.addEventListener('DOMContentLoaded', () => {
      renderWeekCards('all');
    });
  </script>
</body>
</html>
"""

with open('campus-plants.html', 'w', encoding='utf-8') as f:
    f.write(html_code.strip())
print("campus-plants.html successfully created! Size:", len(html_code.encode('utf-8')), "bytes")
