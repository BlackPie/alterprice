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
CatalogProductsPagerView = require 'catalog/items_list/views/CatalogProductsPagerView'
CatalogProductsLayout = require 'catalog/items_list/layouts/CatalogProductsLayout'
CatalogProductsFilterState = require 'catalog/items_list/states/CatalogProductsFilterState'
CatalogProductsCategoriesListView = require 'catalog/items_list/views/CatalogProductsCategoriesListView'


module.exports = class CatalogItemsListController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel

        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}
        @catalogItemsListFilterView = new CatalogItemsListFilterView {channel: @channel}
        @catalogProductsLayout = new CatalogProductsLayout {channel: @channel}
        @catalogProductsPagerView = new CatalogProductsPagerView {channel: @channel}
        @catalogProductsCollection = new CatalogProductsCollection()
        @catalogProductsCategoriesListView = new CatalogProductsCategoriesListView {channel: @channel}
        @catalogProductsListView = new CatalogProductsListView {channel: @channel, collection: @catalogProductsCollection}
        @catalogProductsLayout.productsList.show @catalogProductsListView

        @catalogProductsCollection.on "sync", (collection) =>
            if collection.state.totalPages > 1
                @catalogProductsPagerView.show()
            else
                @catalogProductsPagerView.hide()

        #@catalogProductsCollection.fetchFiltered()
        @onSetFilter()

        @channel.vent.on Events.SET_FILTER,  @onSetFilter
        @channel.vent.on Events.SHOW_MORE,  @onShowMore


    index: () =>
        console.log 'index'


    onSetFilter: =>
        filterData = @catalogItemsListFilterView.getFilterData()
        catalogProductsFilterState = CatalogProductsFilterState.fromArray filterData
        @catalogProductsCollection.state.pageSize = @catalogProductsCollection.startPageSize
        @catalogProductsCollection.fetchFiltered catalogProductsFilterState


    onShowMore: =>
        filterData = @catalogItemsListFilterView.getFilterData()
        catalogProductsFilterState = CatalogProductsFilterState.fromArray filterData
        @catalogProductsCollection.state.pageSize = @catalogProductsCollection.state.pageSize + @catalogProductsCollection.showMoreSize
        @catalogProductsCollection.fetchFiltered catalogProductsFilterState
