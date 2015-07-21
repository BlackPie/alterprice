$ = require 'jquery'
Marionette = require 'backbone.marionette'


module.exports = class ClientStatisticsLayout extends Marionette.LayoutView
    el: $('#client-statistics-detail')

    regions:
        itemsList:  "#client-statistics-items-region"