Marionette   = require 'backbone.marionette'
$ = require 'jquery'
#ProductCardTemplate = require 'templates/product/ProductCard'


module.exports = class CatalogProductEmptyView extends Marionette.ItemView
    initialize: (options) =>
        $('.items-list-page-wrapper').addClass('empty')
        @channel = options.channel

    template: (object) ->
        false