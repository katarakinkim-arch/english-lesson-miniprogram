// utils/analytics.js — 轻量埋点 + 错误上报（本地优先，零后端依赖）
// 设计原则：不依赖任何后端/云函数，全部存本地 storage。
// 上线后可平滑替换为 wx.reportAnalytics（需在后台「自定义分析」配置事件）或自有上报接口。

const ERR_KEY = 'analytics_errors';
const EVT_KEY = 'analytics_events';
const MAX_ERR = 20;
const MAX_EVT = 200;

function read(key, fallback) {
  try { return wx.getStorageSync(key) || fallback; } catch (e) { return fallback; }
}
function write(key, val) {
  try { wx.setStorageSync(key, val); } catch (e) {}
}

// 启动初始化：预留 wx.reportAnalytics 钩子（后台未配置则静默跳过）
function init() {
  // 可在此接入微信自定义分析：wx.reportAnalytics('launch', {})
}

// 记录一次 JS 运行时错误
function recordError(err) {
  const msg = (typeof err === 'string') ? err : (err && err.message) ? err.message : String(err);
  const list = read(ERR_KEY, []);
  list.unshift({ t: Date.now(), msg: msg.substring(0, 300) });
  if (list.length > MAX_ERR) list.length = MAX_ERR;
  write(ERR_KEY, list);
  // 若后台配置了微信自定义分析，可在此上报：wx.reportAnalytics('js_error', { msg });
}

// 记录一个业务事件（本地计数 + 时间序列）
function track(event, data) {
  const list = read(EVT_KEY, []);
  list.unshift({ t: Date.now(), e: event, d: data || null });
  if (list.length > MAX_EVT) list.length = MAX_EVT;
  write(EVT_KEY, list);
  // 微信自定义分析钩子：wx.reportAnalytics(event, data || {});
}

// 读取错误/事件统计（供「我的」页或调试查看）
function getErrors() { return read(ERR_KEY, []); }
function getEvents() { return read(EVT_KEY, []); }
function clearAll() { write(ERR_KEY, []); write(EVT_KEY, []); }

module.exports = { init, recordError, track, getErrors, getEvents, clearAll };
