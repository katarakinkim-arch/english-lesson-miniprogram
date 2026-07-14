const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"语文","root":"cn","emoji":"📗","color":"#2f855a","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修上册","book":"必修上册"},{"value":"2","label":"必修下册","book":"必修下册"}]};
Page(view.makeListPage(function () { return data; }, meta));
