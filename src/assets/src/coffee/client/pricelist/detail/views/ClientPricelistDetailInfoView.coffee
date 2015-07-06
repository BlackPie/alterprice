$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Switcher = require 'base/utils/Switcher'


module.exports = class ClientPricelistDetailInfoView extends Marionette.ItemView
    el: $('#client-pricelist-detail-info-view')

    template: false

    ui:
        switcher: '.switcher-wrapper'

    #events:



    initialize: (options) =>
        @channel = options.channel
        @pricelistId = options.pricelistId
        new Switcher @$(@ui.switcher),
            onCheck: =>
                $.ajax
                    type: 'GET'
                    dataType: 'json'
                    url: "/api/shop/yml/#{@pricelistId}/publish/"
            onUncheck: =>
                $.ajax
                    type: 'GET'
                    dataType: 'json'
                    url: "/api/shop/yml/#{@pricelistId}/unpublish/"

