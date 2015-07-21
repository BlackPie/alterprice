$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'

ClientStatisticsLayout = require './layouts/ClientStatisticsLayout'
ClientStatisticsItemsCollection = require './collections/ClientStatisticsItemsCollection'
ClientStatisticsItemsCollectionView = require './views/ClientStatisticsItemsCollectionView'

ClientStatisticsItemsFilterView = require './views/ClientStatisticsItemsFilterView'


module.exports = class ClientStatisticsController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}

        @clientStatisticsLayout = new ClientStatisticsLayout {channel: @channel}
        @clientStatisticsItemsCollection = new ClientStatisticsItemsCollection
        @clientStatisticsItemsCollectionView = new ClientStatisticsItemsCollectionView
            channel: @channel
            collection: @clientStatisticsItemsCollection
        @clientStatisticsLayout.itemsList.show @clientStatisticsItemsCollectionView
        @clientStatisticsItemsCollection.fetchFiltered({shop: 6})


        @clientStatisticsItemsFilterView = new ClientStatisticsItemsFilterView {channel: @channel}


    index: () =>
        console.log 'index'