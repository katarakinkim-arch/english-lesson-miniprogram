const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"化学","root":"chem","emoji":"⚗️","color":"#c53030","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修第一册","book":"必修第一册"},{"value":"2","label":"必修第二册","book":"必修第二册"},{"value":"3","label":"选择性必修1 化学反应原理","book":"选择性必修1 化学反应原理"},{"value":"4","label":"选择性必修2 物质结构与性质","book":"选择性必修2 物质结构与性质"},{"value":"5","label":"选择性必修3 有机化学基础","book":"选择性必修3 有机化学基础"}]};
Page(view.makeListPage(function () { return data; }, meta));
