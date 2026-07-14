const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"地理","root":"geo","emoji":"🌏","color":"#2c7a7b","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修第一册","book":"必修第一册"},{"value":"2","label":"必修第二册","book":"必修第二册"},{"value":"3","label":"选择性必修1 自然地理基础","book":"选择性必修1 自然地理基础"},{"value":"4","label":"选择性必修2 区域发展","book":"选择性必修2 区域发展"},{"value":"5","label":"选择性必修3 资源环境与国家安全","book":"选择性必修3 资源环境与国家安全"}]};
Page(view.makeListPage(function () { return data; }, meta));
