$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

Events = require 'catalog/Events'
LeftMenuView = require 'base/views/LeftMenuView'
CitySelectorView = require 'base/views/CitySelectorView'
CatalogItemsListFilterView = require 'catalog/items_list/views/CatalogItemsListFilterView'
CatalogProductsCollection = require 'catalog/items_list/collections/CatalogProductsCollection'
CatalogProductsListView = require 'catalog/items_list/views/CatalogProductsListView'
CatalogProductsLayout = require 'catalog/items_list/layouts/CatalogProductsLayout'
CatalogProductsFilterState = require 'catalog/items_list/states/CatalogProductsFilterState'


module.exports = class CatalogItemsListController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel

        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}
        @catalogItemsListFilterView = new CatalogItemsListFilterView {channel: @channel}

        @catalogProductsLayout = new CatalogProductsLayout {channel: @channel}
        @catalogProductsCollection = new CatalogProductsCollection()
        @catalogProductsListView = new CatalogProductsListView {channel: @channel, collection: @catalogProductsCollection}
        @catalogProductsLayout.productsList.show(@catalogProductsListView)
        @catalogProductsCollection.fetchFiltered()

        @channel.vent.on Events.SET_FILTER,  @onSetFilter


    index: () =>
        console.log 'index'

    onSetFilter: =>
        filterData = @catalogItemsListFilterView.getFilterData()
        catalogProductsFilterState = CatalogProductsFilterState.fromArray filterData
        #@productOffersCollection.state.pageSize = @productOffersCollection.startPageSize
        @catalogProductsCollection.fetchFiltered catalogProductsFilterState
