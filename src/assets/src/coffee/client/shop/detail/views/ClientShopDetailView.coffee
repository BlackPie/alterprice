$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Events = require 'client/Events'

module.exports = class ClientShopDetailView extends Marionette.ItemView

    el: $('#client-shop-detail-page')
    template: false

    ui:
        leftBox: $('#client-shop-detail-form-view')
        rightBox: $('#client-shop-detail-call-view')

    initialize: (options) =>
        @channel = options.channel
        @updateHeight()
        @channel.vent.on Events.SHOP_DETAIL_UPDATE_HEIGHT, @updateHeight

    updateHeight: () =>
        @unsetHeight()
        @setHeight @getMaxHeight()

    unsetHeight: () =>
        @$(@ui.leftBox).css
            minHeight: 'auto'
        @$(@ui.rightBox).css
            minHeight: 'auto'

    setHeight: (height) =>
        @$(@ui.leftBox).css
            minHeight: height
        @$(@ui.rightBox).css
            minHeight: height

    getMaxHeight: () =>
        max = 0
        if max < @$(@ui.leftBox).height()  then max = @$(@ui.leftBox).height()
        if max < @$(@ui.rightBox).height() then max = @$(@ui.rightBox).height()
        max
