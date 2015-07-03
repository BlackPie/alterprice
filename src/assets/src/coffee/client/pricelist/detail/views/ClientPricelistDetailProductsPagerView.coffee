$ = require 'jquery'
Backbone = require 'backbone'
Marionette   = require 'backbone.marionette'

PagerTemplate = require 'templates/pager'


module.exports = class ClientPricelistDetailProductsPagerView extends Marionette.ItemView
    el: $('#client-pricelist-detail-products-pager-view')

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        return PagerTemplate(object)

    render: (options) =>
        console.log options
        @$el.html @template(options)