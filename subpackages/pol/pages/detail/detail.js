const view = require('../../../../utils/lessonView.js');
const data = require('../../data/lessons.js');
Page(view.makeDetailPage(function () { return data; }));
