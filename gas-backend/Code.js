/**
 * Puti-AI 教師AI研習需求調查表 - 完整前後端一體化 GAS 專案
 * 作者：屏東縣後庄國小 黃朝榮老師 (Puti-AI)
 * 試算表 ID: 1rG4tyW47aTsvJs6dVFbvSDFln8JmCE58HtnVkfhuggw
 */

// 1. 提供前端 HTML 頁面
// 1. 提供前端 HTML 頁面與備用 JSON API
function doGet(e) {
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
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var TARGET_SHEET_NAME = "全國現役教師大調查";
    var sheet = ss.getSheetByName(TARGET_SHEET_NAME);

    // 若專屬工作表分頁尚不存在，則新建獨立分頁，嚴禁寫入工作表1
    if (!sheet) {
      sheet = ss.insertSheet(TARGET_SHEET_NAME);
      sheet.appendRow([
        "填答時間",
        "服務學校",
        "任教階段",
        "任教學科領域",
        "AI熟悉程度",
        "教學現場挑戰 (複選)",
        "最希望減輕負擔的教學任務",
        "面對AI融入教育的擔憂或疑慮",
        "備註"
      ]);
      
      // 美化表頭格式（藍靛底白字、置中、凍結首列）
      var headerRange = sheet.getRange(1, 1, 1, 9);
      headerRange.setBackground("#4338ca");
      headerRange.setFontColor("#ffffff");
      headerRange.setFontWeight("bold");
      headerRange.setHorizontalAlignment("center");
      sheet.setFrozenRows(1);
    }

    var timestamp = data.timestamp || new Date().toLocaleString("zh-TW", { timeZone: "Asia/Taipei" });
    var school = data.school || "";
    var stage = data.stage || "";
    var subject = data.subject || "";
    var aiLevel = data.aiLevel || "";
    var painpoints = Array.isArray(data.painpoints) ? data.painpoints.join("\n• ") : (data.painpoints || "");
    var urgentNeed = data.urgentNeed || "";
    var worry = data.worry || "";
    var notes = data.notes || "";

    // 寫入新資料行至專屬分頁
    sheet.appendRow([
      timestamp,
      school,
      stage,
      subject,
      aiLevel,
      (painpoints ? "• " + painpoints : ""),
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

    // 從第 2 列開始讀取（跳過表頭）
    for (var i = 1; i < data.length; i++) {
      var row = data[i];
      if (!row[0] && !row[2] && !row[3]) continue;

      var timestamp = String(row[0] || "");
      var school = String(row[1] || "未填寫/匿名");
      var stage = String(row[2] || "");
      var subject = String(row[3] || "");
      var aiLevel = String(row[4] || "");
      var rawPain = String(row[5] || "");
      var urgentNeed = String(row[6] || "");
      var worry = String(row[7] || "");
      var notes = String(row[8] || "");

      var painpointsList = rawPain.split("\n• ").map(function(item) {
        return item.replace(/^•\s*/, "").trim();
      }).filter(function(item) { return item.length > 0; });

      records.push({
        id: "survey_" + i,
        timestamp: timestamp,
        school: school,
        stage: stage,
        subject: subject,
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
