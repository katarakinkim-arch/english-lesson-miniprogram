// data/media.js
// 媒体清单：lesson id -> { images:[{file,desc}], audios:[{file,desc}] }
// file 为相对于 miniprogram/ 根目录的路径；生成 PPT 时由调用方读取字节嵌入。
// 文件随所属学科子包打包（如英语在 subpackages/eng/...），避免撑大主包。
// 说明：图片由 AI 生成后压缩为 JPEG（≤800px，质量78）以契合子包 2MB 上限；
//       音频当前为占位 WAV（真实可播放），待用户提供教材原声后替换 file 即可。
module.exports = {
  'l-eng-b1-u2-ls': {
    images: [
      { file: 'subpackages/eng/images/lessons/l-eng-b1-u2-ls/passport.jpg', desc: '护照' },
      { file: 'subpackages/eng/images/lessons/l-eng-b1-u2-ls/boardingpass.jpg', desc: '机票' },
      { file: 'subpackages/eng/images/lessons/l-eng-b1-u2-ls/suitcase.jpg', desc: '行李箱' },
      { file: 'subpackages/eng/images/lessons/l-eng-b1-u2-ls/map.jpg', desc: '地图' }
    ],
    audios: [
      { file: 'subpackages/eng/images/lessons/l-eng-b1-u2-ls/listening.wav', desc: '听力音频（教材配套·占位）' }
    ]
  }
};
