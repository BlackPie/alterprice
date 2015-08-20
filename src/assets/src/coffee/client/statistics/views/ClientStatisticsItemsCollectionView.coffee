$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientStatisticsItemView = require './ClientStatisticsItemView'
StatisticsItemsTemplate = require 'templates/client/StatisticsItems'


module.exports = class ClientStatisticsItemsCollectionView extends Marionette.CompositeView

    childViewContainer: 'tbody'

    template: () =>
        StatisticsItemsTemplate
            type: @type

    initialize: (options) =>
        @channel = options.channel
        @type = options.type

    getChildView: (model) =>
        return ClientStatisticsItemView

    childViewOptions: (model, index) =>
        channel: @channel

    setType: (type) =>
        @type = type
        @render()
