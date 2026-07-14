const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"物理","root":"physics","emoji":"🔭","color":"#6b46c1","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修第一册","book":"必修第一册"},{"value":"2","label":"必修第二册","book":"必修第二册"},{"value":"3","label":"选择性必修第一册","book":"选择性必修第一册"},{"value":"4","label":"选择性必修第二册","book":"选择性必修第二册"},{"value":"5","label":"选择性必修第三册","book":"选择性必修第三册"}]};
Page(view.makeListPage(function () { return data; }, meta));
