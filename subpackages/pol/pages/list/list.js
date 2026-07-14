const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
const meta = {"subject":"政治","root":"pol","emoji":"⚖️","color":"#b7791f","books":[{"value":"0","label":"全部","book":"__all__"},{"value":"1","label":"必修1 中国特色社会主义","book":"必修1 中国特色社会主义"},{"value":"2","label":"必修2 经济与社会","book":"必修2 经济与社会"},{"value":"3","label":"必修3 政治与法治","book":"必修3 政治与法治"},{"value":"4","label":"必修4 哲学与文化","book":"必修4 哲学与文化"},{"value":"5","label":"选择性必修1 当代国际政治与经济","book":"选择性必修1 当代国际政治与经济"},{"value":"6","label":"选择性必修2 法律与生活","book":"选择性必修2 法律与生活"}]};
Page(view.makeListPage(function () { return data; }, meta));
