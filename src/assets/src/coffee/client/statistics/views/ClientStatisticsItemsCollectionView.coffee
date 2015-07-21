$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientStatisticsItemView = require './ClientStatisticsItemView'
StatisticsItemsTemplate = require 'templates/client/StatisticsItems'


module.exports = class ClientStatisticsItemsCollectionView extends Marionette.CompositeView
    template: false

    childViewContainer: 'tbody'

    template: StatisticsItemsTemplate

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ClientStatisticsItemView

    childViewOptions: (model, index) =>
        return {channel: @channel}
