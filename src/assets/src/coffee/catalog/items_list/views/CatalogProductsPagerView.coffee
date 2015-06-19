$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'catalog/Events'


module.exports = class CatalogProductsPagerView extends Marionette.ItemView
    el: $('#catalog-products-pager-view')

    template: false

    ui:
        showMoreBtn: '.btn'

    events:
        "click @ui.showMoreBtn": "onClickShowMoreBtn"


    initialize: (options) =>
        @channel = options.channel


    onClickShowMoreBtn: (e) =>
        e.preventDefault()
        @channel.vent.trigger Events.SHOW_MORE


    show: =>
        @$(@ui.showMoreBtn).show()

    hide: =>
        @$(@ui.showMoreBtn).hide()