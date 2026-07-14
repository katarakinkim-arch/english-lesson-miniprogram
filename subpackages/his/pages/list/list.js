const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"历史","root":"his","emoji":"📜","color":"#975a16","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修《中外历史纲要》上册","book":"必修《中外历史纲要》上册"},{"value":"2","label":"必修《中外历史纲要》下册","book":"必修《中外历史纲要》下册"},{"value":"3","label":"选择性必修1 国家制度与社会治理","book":"选择性必修1 国家制度与社会治理"},{"value":"4","label":"选择性必修2 经济与社会生活","book":"选择性必修2 经济与社会生活"},{"value":"5","label":"选择性必修3 文化交流与传播","book":"选择性必修3 文化交流与传播"}]};
Page(view.makeListPage(function () { return data; }, meta));
