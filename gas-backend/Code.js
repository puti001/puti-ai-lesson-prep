/**
 * Puti-AI 教師AI研習需求調查表 - 完整前後端一體化 GAS 專案
 * 作者：屏東縣後庄國小 黃朝榮老師 (Puti-AI)
 * 試算表 ID: 1rG4tyW47aTsvJs6dVFbvSDFln8JmCE58HtnVkfhuggw
 */

// 0. 確保並主動初始化【全國現役教師大調查】專屬分頁與美化表頭
function getOrInitSurveySheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var TARGET_SHEET_NAME = "全國現役教師大調查";
  var sheet = ss.getSheetByName(TARGET_SHEET_NAME);

  var NEW_HEADERS = [
    "填答時間",
    "生理性別",
    "年齡區間",
    "教學年資",
    "主要任教階段",
    "任教學科領域 (複選)",
    "AI熟悉程度",
    "教學現場挑戰 (複選)",
    "最希望減輕負擔的教學任務",
    "面對AI融入教育的擔憂或疑慮",
    "備註"
  ];

  if (!sheet) {
    sheet = ss.insertSheet(TARGET_SHEET_NAME);
  }

  // 若分頁為空或只有舊標題，建立美化標準表頭
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(NEW_HEADERS);
    var headerRange = sheet.getRange(1, 1, 1, NEW_HEADERS.length);
    headerRange.setBackground("#4338ca");
    headerRange.setFontColor("#ffffff");
    headerRange.setFontWeight("bold");
    headerRange.setHorizontalAlignment("center");
    sheet.setFrozenRows(1);
  }

  return sheet;
}

// 1. 提供前端 HTML 頁面與備用 JSON API
function doGet(e) {
  try {
    // 主動確保專屬分頁已在試算表建立
    getOrInitSurveySheet();
  } catch (err) {
    console.warn("主動建立工作表分頁失敗:", err);
  }

  // 支援手動觸發初始化或檢查分頁
  if (e && e.parameter && e.parameter.action === "initSheet") {
    var s = getOrInitSurveySheet();
    return ContentService
      .createTextOutput(JSON.stringify({ result: "success", message: "工作表分頁【全國現役教師大調查】已建立就緒！", sheetName: s.getName() }))
      .setMimeType(ContentService.MimeType.JSON);
  }

  // 支援透過 GET 參數直接獲取數據（例如本地預覽或第三方取用）
  if (e && e.parameter && e.parameter.action === "getRecords") {
    var recordsData = getSurveyRecords();
    return ContentService
      .createTextOutput(JSON.stringify(recordsData))
      .setMimeType(ContentService.MimeType.JSON);
  }

  return HtmlService.createHtmlOutputFromFile("index")
    .setTitle("Puti-AI | 全國現役教師教學痛點與AI需求大調查")
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag("viewport", "width=device-width, initial-scale=1.0");
}

// 2. 前端透過 google.script.run 直連寫入試算表（極速、免 CORS、免 URL）
function saveSurveyRecord(data) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000); // 鎖定防多人併發衝突

  try {
    var sheet = getOrInitSurveySheet();

    var timestamp = data.timestamp || new Date().toLocaleString("zh-TW", { timeZone: "Asia/Taipei" });
    var gender = data.gender || "未填";
    var ageGroup = data.ageGroup || "未填";
    var experience = data.experience || "未填";
    var stage = data.stage || "";
    
    // 學科領域支援陣列複選
    var subjectsStr = "";
    if (Array.isArray(data.subjects)) {
      subjectsStr = data.subjects.join(", ");
    } else if (data.subjects) {
      subjectsStr = String(data.subjects);
    } else if (data.subject) {
      subjectsStr = String(data.subject);
    }

    var aiLevel = data.aiLevel || "";
    var painpoints = Array.isArray(data.painpoints) ? ("• " + data.painpoints.join("\n• ")) : (data.painpoints || "");
    var urgentNeed = data.urgentNeed || "";
    var worry = data.worry || "";
    var notes = data.notes || "";

    // 寫入新資料行至專屬分頁
    sheet.appendRow([
      timestamp,
      gender,
      ageGroup,
      experience,
      stage,
      subjectsStr,
      aiLevel,
      painpoints,
      urgentNeed,
      worry,
      notes
    ]);

    return { result: "success", message: "資料已順利存入【全國現役教師大調查】獨立分頁！" };

  } catch (error) {
    return { result: "error", error: error.toString() };

  } finally {
    lock.releaseLock();
  }
}

// 3. 前端透過 google.script.run 即時獲取雲端試算表真實填答數據（嚴格僅讀取全國現役教師大調查分頁）
function getSurveyRecords() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var TARGET_SHEET_NAME = "全國現役教師大調查";
    var sheet = ss.getSheetByName(TARGET_SHEET_NAME);

    // 若尚未有全國大調查分頁或無數據，回傳乾淨的空陣列，絕不誤抓工作表1 (建華國小專用)
    if (!sheet || sheet.getLastRow() <= 1) {
      return { result: "success", records: [], count: 0 };
    }

    var data = sheet.getDataRange().getValues();
    var records = [];
    var headerRow = data[0];
    var isNewSchema = (headerRow && String(headerRow[1]).indexOf("性別") !== -1);

    // 從第 2 列開始讀取（跳過表頭）
    for (var i = 1; i < data.length; i++) {
      var row = data[i];
      if (!row[0] && !row[2] && !row[4]) continue;

      var timestamp = String(row[0] || "");
      var gender = isNewSchema ? String(row[1] || "未填") : "未填";
      var ageGroup = isNewSchema ? String(row[2] || "未填") : "未填";
      var experience = isNewSchema ? String(row[3] || "未填") : "未填";
      var stage = isNewSchema ? String(row[4] || "") : String(row[2] || "");
      var rawSubjects = isNewSchema ? String(row[5] || "") : String(row[3] || "");
      var aiLevel = isNewSchema ? String(row[6] || "") : String(row[4] || "");
      var rawPain = isNewSchema ? String(row[7] || "") : String(row[5] || "");
      var urgentNeed = isNewSchema ? String(row[8] || "") : String(row[6] || "");
      var worry = isNewSchema ? String(row[9] || "") : String(row[7] || "");
      var notes = isNewSchema ? String(row[10] || "") : String(row[8] || "");

      // 解析學科領域清單（逗號分隔或陣列）
      var subjectsList = rawSubjects.split(/[,，、]/).map(function(item) {
        return item.trim();
      }).filter(function(item) { return item.length > 0; });

      var painpointsList = rawPain.split("\n• ").map(function(item) {
        return item.replace(/^•\s*/, "").trim();
      }).filter(function(item) { return item.length > 0; });

      records.push({
        id: "survey_" + i,
        timestamp: timestamp,
        gender: gender,
        ageGroup: ageGroup,
        experience: experience,
        stage: stage,
        subjects: subjectsList,
        subject: subjectsList.join(", "),
        aiLevel: aiLevel,
        painpoints: painpointsList,
        urgentNeed: urgentNeed,
        worry: worry,
        notes: notes
      });
    }

    return { result: "success", records: records, count: records.length };
  } catch (err) {
    return { result: "error", error: err.toString(), records: [] };
  }
}

// 4. 備用 HTTP POST 端點
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var res = saveSurveyRecord(data);
    return ContentService
      .createTextOutput(JSON.stringify(res))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: "error", error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
