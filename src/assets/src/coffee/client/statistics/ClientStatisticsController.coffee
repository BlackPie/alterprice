$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'
Events = require 'client/Events'

LeftMenuView = require 'base/views/LeftMenuView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'

ClientStatisticsLayout = require './layouts/ClientStatisticsLayout'
ClientStatisticsItemsCollection = require './collections/ClientStatisticsItemsCollection'
ClientStatisticsItemsCollectionView = require './views/ClientStatisticsItemsCollectionView'
ClientStatisticsItemsPagerView = require './views/ClientStatisticsItemsPagerView'
ClientStatisticsItemsFilterView = require './views/ClientStatisticsItemsFilterView'
ClientStatisticsItemsFilterState = require './states/ClientStatisticsItemsFilterState'


module.exports = class ClientStatisticsController extends Marionette.Controller

    initialize: (options) =>
        @shopId = options.context['shopId']
        @pricelistId = options.context['pricelistId']
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}

        @clientStatisticsLayout = new ClientStatisticsLayout {channel: @channel}
        @clientStatisticsItemsCollection = new ClientStatisticsItemsCollection
        @clientStatisticsItemsCollection.setShopId @shopId
        @clientStatisticsItemsCollection.setPricelistId @pricelistId
        @clientStatisticsItemsCollectionView = new ClientStatisticsItemsCollectionView
            channel: @channel
            collection: @clientStatisticsItemsCollection
            type: 'offers'
        @clientStatisticsLayout.itemsList.show @clientStatisticsItemsCollectionView
        @clientStatisticsItemsFilterView = new ClientStatisticsItemsFilterView {channel: @channel}
        @clientStatisticsItemsPagerView = new ClientStatisticsItemsPagerView {channel: @channel}
        @fetchItems()

        @channel.vent.on Events.STATISTICS_ITEMS_PAGER, @onChangeItemsPage
        @channel.vent.on Events.STATISTICS_ITEMS_FILTERED,  @fetchItems


    index: () =>
        console.log 'index'


    fetchItems: =>
        filterData = @clientStatisticsItemsFilterView.getFilterData()
        clientStatisticsItemsFilterState = ClientStatisticsItemsFilterState.fromArray filterData
        @clientStatisticsItemsCollection.setType(filterData.type)
        @clientStatisticsItemsCollectionView.setType(filterData.type)
        options =
            pageSize: @clientStatisticsItemsCollection.state.pageSize
            currentPage: 1
        @clientStatisticsItemsCollection.getFirstPage({data: clientStatisticsItemsFilterState, fetch: true}).done (response) =>
            @clientStatisticsItemsPagerView.render response, options


    onChangeItemsPage: (page) =>
        filterData = @clientStatisticsItemsFilterView.getFilterData()
        clientStatisticsItemsFilterState = ClientStatisticsItemsFilterState.fromArray filterData
        @clientStatisticsItemsCollection.getPage(page, {data: clientStatisticsItemsFilterState, fetch: true})
