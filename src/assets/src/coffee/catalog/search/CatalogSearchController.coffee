$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

Events = require 'catalog/Events'
LeftMenuView = require 'base/views/LeftMenuView'
CitySelectorView = require 'base/views/CitySelectorView'

CatalogItemsListFilterView = require 'catalog/items_list/views/CatalogItemsListFilterView'
CatalogProductsListView = require 'catalog/items_list/views/CatalogProductsListView'
CatalogProductsPagerView = require 'catalog/items_list/views/CatalogProductsPagerView'
CatalogProductsFilterState = require 'catalog/items_list/states/CatalogProductsFilterState'

CatalogSearchProductsCollection = require 'catalog/search/collections/CatalogSearchProductsCollection'
CatalogSearchLayout = require 'catalog/search/layouts/CatalogSearchLayout'
CatalogSearchCategoriesListView = require 'catalog/search/views/CatalogSearchCategoriesListView'
CatalogSearchCategoryLinksCollection = require 'catalog/search/collections/CatalogSearchCategoryLinksCollection'

CatalogSearchOffersCollection = require 'catalog/search/collections/CatalogSearchOffersCollection'
CatalogSearchOffersListView = require 'catalog/search/views/CatalogSearchOffersListView'

module.exports = class CatalogSearchController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel

        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}
        @catalogItemsListFilterView = new CatalogItemsListFilterView {channel: @channel}
        @catalogSearchLayout = new CatalogSearchLayout {channel: @channel}
        @catalogProductsPagerView = new CatalogProductsPagerView {channel: @channel}

        @catalogSearchOffersCollection = new CatalogSearchOffersCollection()
        @catalogSearchOffersListView = new CatalogSearchOffersListView {channel: @channel, collection: @catalogSearchOffersCollection}
        @catalogSearchLayout.offersList.show @catalogSearchOffersListView


        @catalogSearchProductsCollection = new CatalogSearchProductsCollection()
        @catalogProductsListView = new CatalogProductsListView {channel: @channel, collection: @catalogSearchProductsCollection}
        @catalogSearchLayout.productsList.show @catalogProductsListView

        @catalogSearchCategoryLinksCollection = new CatalogSearchCategoryLinksCollection()
        @catalogSearchCategoriesListView = new CatalogSearchCategoriesListView {channel: @channel, collection: @catalogSearchCategoryLinksCollection}
        @catalogSearchLayout.categoriesList.show @catalogSearchCategoriesListView


        @catalogSearchProductsCollection.on "sync", (collection) =>
            if collection.state.totalPages > 1
                @catalogProductsPagerView.show()
            else
                @catalogProductsPagerView.hide()
                $('#catalog-search-offers').css
                  display: 'block'

        @onSetFilter()

        filterData = @catalogItemsListFilterView.getFilterData()
        catalogProductsFilterState = CatalogProductsFilterState.fromArray filterData
        @catalogSearchCategoryLinksCollection.fetchFiltered catalogProductsFilterState

        @catalogSearchCategoryLinksCollection.on "sync", (collection) =>
            @catalogSearchCategoriesListView.initMoreBtn()

        @channel.vent.on Events.SET_FILTER, @onSetFilter
        @channel.vent.on Events.SHOW_MORE, @onShowMore
        @channel.vent.on Events.SET_CATEGORY, @onSetCategory


    index: () =>
        console.log 'index'


    onSetFilter: =>
        filterData = @catalogItemsListFilterView.getFilterData()
        catalogProductsFilterState = CatalogProductsFilterState.fromArray filterData
        @catalogSearchProductsCollection.state.pageSize = @catalogSearchProductsCollection.startPageSize
        @catalogSearchProductsCollection.fetchFiltered catalogProductsFilterState
        @catalogSearchOffersCollection.fetchFiltered catalogProductsFilterState


    onShowMore: =>
        filterData = @catalogItemsListFilterView.getFilterData()
        catalogProductsFilterState = CatalogProductsFilterState.fromArray filterData
        @catalogSearchProductsCollection.state.pageSize = @catalogSearchProductsCollection.state.pageSize + @catalogSearchProductsCollection.showMoreSize
        @catalogSearchProductsCollection.fetchFiltered catalogProductsFilterState


    onSetCategory: (categoryId) =>
        @catalogItemsListFilterView.setCategory categoryId
        $('#catalog-search-categories-list-view').find('a.btn-sea.active').removeClass('active')
        $('#catalog-search-categories-list-view').find("a.btn-sea[data-category=\"#{categoryId}\"]").addClass('active')
        @onSetFilter()
