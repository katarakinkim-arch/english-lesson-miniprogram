const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"生物","root":"bio","emoji":"🧬","color":"#25855a","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修1 分子与细胞","book":"必修1 分子与细胞"},{"value":"2","label":"必修2 遗传与进化","book":"必修2 遗传与进化"},{"value":"3","label":"选择性必修1 稳态与调节","book":"选择性必修1 稳态与调节"},{"value":"4","label":"选择性必修2 生物与环境","book":"选择性必修2 生物与环境"},{"value":"5","label":"选择性必修3 生物技术与工程","book":"选择性必修3 生物技术与工程"}]};
Page(view.makeListPage(function () { return data; }, meta));
