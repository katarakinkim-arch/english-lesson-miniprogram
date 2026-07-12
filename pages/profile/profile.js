// pages/profile/profile.js — 个人中心（昵称头像 + 统计 + 收藏）
const app = getApp();
const clouduser = require('../../utils/clouduser.js');

Page({
  data: {
    openid: '',
    nickName: '',
    avatarUrl: '',
    isLocal: false,           // true = 游客/未配置云，数据仅存本机
    stats: { downloads: 0, recents: 0, favorites: 0 },
    favorites: []             // 收藏的教案卡片列表
  },

  onShow() {
    this.refresh();
  },

  async refresh() {
    try {
      const u = await clouduser.login();          // 含昵称头像
      const a = await clouduser.getActions();      // 含 downloads/recents/favorites
      const favIds = (a && a.favorites) || [];
      const favLessons = app.getLessonsByIds(favIds);

      this.setData({
        openid: u.openid || '',
        nickName: u.nickName || '',
        avatarUrl: u.avatarUrl || '',
        isLocal: (u.openid || '') === 'local',
        stats: {
          downloads: (a && a.downloads) ? a.downloads.length : 0,
          recents: (a && a.recents) ? a.recents.length : 0,
          favorites: favIds.length
        },
        favorites: favLessons.map((l) => ({
          id: l.id,
          title: l.title,
          sub: '第' + l.unitNumber + '单元 · ' + l.lessonTypeName
        }))
      });
    } catch (e) {
      this.setData({ isLocal: true });
    }
  },

  // 选择头像（微信合规方式：button open-type=chooseAvatar）
  onChooseAvatar(e) {
    const avatarUrl = e.detail.avatarUrl;
    this.setData({ avatarUrl });
    clouduser.updateProfile({ nickName: this.data.nickName, avatarUrl });
  },

  // 填写昵称（input type=nickname）
  onNickname(e) {
    const nickName = e.detail.value;
    this.setData({ nickName });
    clouduser.updateProfile({ nickName, avatarUrl: this.data.avatarUrl });
  },

  openDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({ url: '/pages/detail/detail?id=' + id });
  },

  removeFav(e) {
    const id = e.currentTarget.dataset.id;
    wx.showModal({
      title: '取消收藏',
      content: '确定从收藏中移除该教案？',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.removeAction('favorite', id);
          this.refresh();
        }
      }
    });
  },

  clearFav() {
    if (!this.data.favorites.length) return;
    wx.showModal({
      title: '清空收藏',
      content: '确定清空全部收藏？',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('favorites');
          this.refresh();
        }
      }
    });
  },

  clearAll() {
    wx.showModal({
      title: '清空全部云端数据',
      content: '将清空下载、最近浏览与收藏记录，此操作不可恢复。',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('downloads');
          await clouduser.clear('recents');
          await clouduser.clear('favorites');
          this.refresh();
        }
      }
    });
  }
});
