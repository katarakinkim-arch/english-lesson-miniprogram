// 云函数 user —— 处理用户登录、资料与行为记录（下载/最近浏览/收藏）
// 部署：微信开发者工具中右键 cloudfunctions/user -> 上传并部署（云端安装依赖）
const cloud = require('wx-server-sdk');
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV });

const db = cloud.database();
const users = db.collection('users');

// 安全取值：保证返回的是数组
function arr(v) {
  return Array.isArray(v) ? v : [];
}

// 拉取当前用户文档（不存在则创建）
async function ensureUser(openid) {
  let doc = (await users.where({ _openid: openid }).get()).data[0];
  if (!doc) {
    const init = {
      _openid: openid,
      nickName: '',
      avatarUrl: '',
      downloads: [],
      recents: [],
      favorites: [],
      createdAt: Date.now()
    };
    await users.add(init);
    doc = (await users.where({ _openid: openid }).get()).data[0];
  }
  return doc;
}

exports.main = async (event) => {
  const { OPENID } = cloud.getWXContext();
  if (!OPENID) return { error: 'no openid' };

  const { action } = event;
  const doc = await ensureUser(OPENID);
  const uid = doc._id;
  const save = (patch) => users.doc(uid).update(patch);

  // 登录 / 拉取全部行为数据：返回统一结构
  if (action === 'login' || action === 'getActions') {
    return {
      openid: OPENID,
      nickName: doc.nickName || '',
      avatarUrl: doc.avatarUrl || '',
      downloads: arr(doc.downloads),
      recents: arr(doc.recents),
      favorites: arr(doc.favorites)
    };
  }

  // 新增行为
  if (action === 'addAction') {
    const { type, lessonId, format } = event;

    if (type === 'recent') {
      let rec = arr(doc.recents).filter((x) => x !== lessonId);
      rec.push(lessonId);
      if (rec.length > 20) rec = rec.slice(-20); // 仅保留最近 20 条
      await save({ recents: rec });
    } else if (type === 'download') {
      let dls = arr(doc.downloads).filter((x) => x.lessonId !== lessonId);
      dls.unshift({ lessonId, format: format || 'word', time: Date.now() });
      if (dls.length > 50) dls = dls.slice(0, 50);
      await save({ downloads: dls });
    } else if (type === 'favorite') {
      let fav = arr(doc.favorites);
      if (!fav.includes(lessonId)) {
        fav.unshift(lessonId);
        await save({ favorites: fav });
      }
    }
    return { ok: true };
  }

  // 移除行为（下载/收藏/最近）
  if (action === 'removeAction') {
    const { type, lessonId } = event;
    if (type === 'download') {
      const dls = arr(doc.downloads).filter((x) => x.lessonId !== lessonId);
      await save({ downloads: dls });
    } else {
      const list = arr(doc[type]).filter((x) => x !== lessonId);
      await save({ [type]: list });
    }
    return { ok: true };
  }

  // 清空某一类
  if (action === 'clear') {
    const { type } = event;
    await save({ [type]: [] });
    return { ok: true };
  }

  // 更新昵称头像
  if (action === 'updateProfile') {
    await save({
      nickName: event.nickName || '',
      avatarUrl: event.avatarUrl || '',
      updatedAt: Date.now()
    });
    return { ok: true };
  }

  return { error: 'unknown action: ' + action };
};
