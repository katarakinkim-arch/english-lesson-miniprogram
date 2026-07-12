// app.js — 小程序入口，管理全局数据与本地存储
const lessons = require('./data/lessons.js');

App({
  globalData: {
    lessons: lessons,           // 全部 30 课英语教案
    downloadLimit: 10,          // 每日下载额度（演示用）
    downloads: [],              // 下载记录
    recentlyViewed: []          // 最近浏览
  },

  onLaunch() {
    try {
      this.globalData.downloads = wx.getStorageSync('downloads') || [];
      this.globalData.recentlyViewed = wx.getStorageSync('recentlyViewed') || [];
    } catch (e) {
      this.globalData.downloads = [];
      this.globalData.recentlyViewed = [];
    }
  },

  // 记录最近浏览（最多保存 20 条，去重）
  addRecent(id) {
    let list = this.globalData.recentlyViewed.filter(x => x !== id);
    list.unshift(id);
    if (list.length > 20) list = list.slice(0, 20);
    this.globalData.recentlyViewed = list;
    wx.setStorageSync('recentlyViewed', list);
  },

  // 记录下载（去重，更新时间）
  addDownload(record) {
    const list = this.globalData.downloads.filter(d => !(d.lessonId === record.lessonId && d.format === record.format));
    list.unshift(record);
    this.globalData.downloads = list;
    wx.setStorageSync('downloads', list);
  },

  removeDownload(id) {
    const list = this.globalData.downloads.filter(d => d.id !== id);
    this.globalData.downloads = list;
    wx.setStorageSync('downloads', list);
  }
});
