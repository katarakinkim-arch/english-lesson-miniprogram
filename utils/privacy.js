// utils/privacy.js — 微信隐私合规封装
// 微信自 2023 年起强制：涉及收集用户信息的接口前必须弹隐私授权。
// 后台需在「小程序管理后台 > 设置 > 服务内容 > 用户隐私保护指引」勾选对应类目，
// 代码侧这里负责在合适时机弹出官方授权窗（requirePrivacyAuthorize）。

function needPrivacy() {
  return typeof wx.requirePrivacyAuthorize === 'function';
}

// 在需要隐私授权的接口前调用：若后台已配置隐私指引且用户未授权，则弹窗。
// resolve(true) = 已授权/无需授权；resolve(false) = 用户拒绝。
function ensurePrivacyAuthorize() {
  return new Promise((resolve) => {
    if (!needPrivacy()) { resolve(true); return; }
    wx.getPrivacySetting({
      success(res) {
        if (res && res.needAuthorization) {
          wx.requirePrivacyAuthorize({
            success: () => resolve(true),
            fail: () => resolve(false),
            complete: () => {}
          });
        } else {
          resolve(true);
        }
      },
      fail: () => resolve(true)
    });
  });
}

// 启动时尝试弹一次（后台未配置则自动 no-op，不影响启动）
function tryShowAtLaunch() {
  if (!needPrivacy()) return;
  wx.getPrivacySetting({
    success(res) {
      if (res && res.needAuthorization) {
        wx.requirePrivacyAuthorize({
          success: () => {},
          fail: () => {},
          complete: () => {}
        });
      }
    },
    fail: () => {}
  });
}

module.exports = { ensurePrivacyAuthorize, tryShowAtLaunch, needPrivacy };
