$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'
Events = require 'client/Events'

LeftMenuView = require 'base/views/LeftMenuView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'
Switcher = require 'base/utils/Switcher'
ClientPriceListDetailParamsFormView = require './views/ClientPriceListDetailParamsFormView'
ClientPricelistDetailInfoView = require './views/ClientPricelistDetailInfoView'

ClientPricelistDetailLayout = require './layouts/ClientPricelistDetailLayout'
ClientPricelistCategoriesCollection = require './collections/ClientPricelistCategoriesCollection'
ClientPricelistDetailCategoriesCollectionView = require './views/ClientPricelistDetailCategoriesCollectionView'

ClientPricelistProductsCollection = require './collections/ClientPricelistProductsCollection'
ClientPricelistDetailProductsCollectionView = require './views/ClientPricelistDetailProductsCollectionView'
ClientPricelistDetailProductsPagerView = require './views/ClientPricelistDetailProductsPagerView'



module.exports = class ClientPricelistDetailController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @pricelistId = options.context.pricelistId

        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}
        @clientPriceListDetailParamsFormView = new ClientPriceListDetailParamsFormView {channel: @channel}
        @clientPricelistDetailInfoView = new ClientPricelistDetailInfoView {channel: @channel, pricelistId: @pricelistId}

        @clientPricelistDetailLayout = new ClientPricelistDetailLayout {channel: @channel}

        @clientPricelistCategoriesCollection = new ClientPricelistCategoriesCollection
        @clientPricelistCategoriesCollection.setPricelistId @pricelistId
        @clientPricelistDetailCategoriesCollectionView = new ClientPricelistDetailCategoriesCollectionView
            channel: @channel
            collection: @clientPricelistCategoriesCollection
        @clientPricelistDetailLayout.categoriesList.show @clientPricelistDetailCategoriesCollectionView
        @clientPricelistCategoriesCollection.fetchFiltered()

        @clientPricelistProductsCollection = new ClientPricelistProductsCollection
        @clientPricelistProductsCollection.setPricelistId @pricelistId
        @clientPricelistDetailProductsCollectionView = new ClientPricelistDetailProductsCollectionView
            channel: @channel
            id: @pricelistId
            collection: @clientPricelistProductsCollection
        @clientPricelistDetailLayout.productsList.show @clientPricelistDetailProductsCollectionView
        @fetchProducts()

        @channel.vent.on Events.PRICELIST_PRODUCTS_PAGER,  @onChangeProductPage
        @channel.vent.on Events.PRICELIST_CHANGE_TITLE,  @onChangePricelistTitle


    index: () =>
        console.log 'index'


    fetchProducts: =>
        @clientPricelistDetailProductsPagerView = new ClientPricelistDetailProductsPagerView {channel: @channel}
        options =
            pageSize: @clientPricelistProductsCollection.state.pageSize
            currentPage: @clientPricelistProductsCollection.state.currentPage
        @clientPricelistProductsCollection.fetch().done (response) =>
            @clientPricelistDetailProductsPagerView.render response, options


    onChangeProductPage: (page) =>
        @clientPricelistProductsCollection.getPage(page)


    onChangePricelistTitle: (title) =>
        $('#price-list-name').text title
