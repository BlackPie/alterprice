$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'

Switcher = require 'base/utils/Switcher'


module.exports = class ClientPricelistDetailInfoView extends Marionette.ItemView
    el: $('#client-pricelist-detail-info-view')

    template: false

    ui:
        switcher: '.switcher-wrapper'
        deleteBtn: '#client-pricelist-remove'

    events:
        "click @ui.deleteBtn": "onClickDeleteBtn"


    initialize: (options) =>
        @channel = options.channel
        @pricelistId = options.pricelistId
        new Switcher @$(@ui.switcher),
            onCheck: =>
                $.ajax
                    type: 'PUT'
                    dataType: 'json'
                    url: "/api/shop/yml/#{@pricelistId}/publish/"
            onUncheck: =>
                $.ajax
                    type: 'PUT'
                    dataType: 'json'
                    url: "/api/shop/yml/#{@pricelistId}/unpublish/"


    onClickDeleteBtn: (e) =>
        e.preventDefault()

        deleteUrl = @$(@ui.deleteBtn).attr 'data-url'
        $.ajax
            url: deleteUrl
            type: 'DELETE'
            dataType: 'json'
            success: (response) =>
                if response.redirect_to
                    window.location.href = response.redirect_to

