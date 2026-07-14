const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"英语","root":"eng","emoji":"📘","color":"#2b6cb0","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修第一册","book":"必修第一册"},{"value":"2","label":"必修第二册","book":"必修第二册"},{"value":"3","label":"必修第三册","book":"必修第三册"}]};
Page(view.makeListPage(function () { return data; }, meta));
