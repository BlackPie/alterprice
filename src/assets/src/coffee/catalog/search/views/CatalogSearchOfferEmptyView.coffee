Marionette   = require 'backbone.marionette'
$ = require 'jquery'


module.exports = class CatalogSearchOfferEmptyView extends Marionette.ItemView

    initialize: (options) =>
        @channel = options.channel

    template: (object) ->
        false
