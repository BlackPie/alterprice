$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'


module.exports = class ProductTabsReviewsView extends Marionette.ItemView
    el: $('#comments-wrapper-view')

    template: false

    ui:
        wrapper: 'section'

    events:
        "click @ui.tabLink": "onClickTabLink"


    initialize: (options) =>
        @channel = options.channel


    show: =>
        @$(@ui.wrapper).show()


    hide: =>
        @$(@ui.wrapper).hide()