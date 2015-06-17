$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Events = require 'product/Events'


module.exports = class ProductOffersPagerView extends Marionette.ItemView
    el: $('#product-offers-pager-view')

    template: false

    ui:
        showMoreBtn: '.show-more'

    events:
        "click @ui.showMoreBtn": "onClickShowMoreBtn"


    initialize: (options) =>
        @channel = options.channel


    onClickShowMoreBtn: (e) =>
        e.preventDefault()
        @channel.vent.trigger Events.OFFERS_SHOW_MORE


    show: =>
        @$(@ui.showMoreBtn).show()

    hide: =>
        @$(@ui.showMoreBtn).hide()