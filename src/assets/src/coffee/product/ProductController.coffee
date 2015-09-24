$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
CitySelectorView = require 'base/views/CitySelectorView'

Events = require 'product/Events'
ProductDetailView = require 'product/views/ProductDetailView'
ProductGalleryView = require 'product/views/ProductGalleryView'
ProductTabsNavigtionView = require 'product/views/tabs/ProductTabsNavigtionView'
ProductOffersLayout = require 'product/layouts/ProductOffersLayout'
ProductTabsPropsView = require 'product/views/tabs/ProductTabsPropsView'
ProductTabsReviewsView = require 'product/views/tabs/ProductTabsReviewsView'
ProductOffersFilterView = require 'product/views/offers/ProductOffersFilterView'
ProductOffersListView = require 'product/views/offers/ProductOffersListView'
ProductOffersPagerView = require 'product/views/offers/ProductOffersPagerView'
ProductOffersFilterState = require 'product/states/ProductOffersFilterState'
ProductOffersCollection = require 'product/collections/ProductOffersCollection'

ProductOpinionsLayout = require 'product/layouts/ProductOpinionsLayout'
ProductOpinionsCollection = require 'product/collections/ProductOpinionsCollection'
ProductOpinionsListView = require 'product/views/opinions/ProductOpinionsListView'
ProductOpinionPagerView = require 'product/views/opinions/ProductOpinionPagerView'


module.exports = class ProductController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @productId = options.context.productId

        @leftMenuView = new LeftMenuView {channel: @channel}
        @citySelectorView = new CitySelectorView {channel: @channel}

        @productDetailView = new ProductDetailView {channel: @channel}
        @productGalleryView = new ProductGalleryView {channel: @channel}
        @productTabsNavigtionView = new ProductTabsNavigtionView {channel: @channel}
        @productTabsPropsView = new ProductTabsPropsView {channel: @channel}
        @productTabsReviewsView = new ProductTabsReviewsView {channel: @channel}

        @productOffersLayout = new ProductOffersLayout {channel: @channel}
        @productOffersCollection = new ProductOffersCollection {id: @productId}
        @productOffersFilterView = new ProductOffersFilterView {channel: @channel}
        @productOffersListView = new ProductOffersListView {channel: @channel, collection: @productOffersCollection}
        @productOffersLayout.offersList.show @productOffersListView
        @productOffersPagerView = new ProductOffersPagerView {channel: @channel}

        @productOpinionsLayout = new ProductOpinionsLayout {channel: @channel}
        @productOpinionsCollection = new ProductOpinionsCollection {channel: @channel, id: @productId}
        @productOpinionsListView = new ProductOpinionsListView {channel: @channel, collection: @productOpinionsCollection}
        @productOpinionsLayout.opinionsList.show @productOpinionsListView
        @productOpinionPagerView = new ProductOpinionPagerView {channel: @channel}

        @productOffersCollection.on "sync", (collection) =>
            if collection.state.totalPages > 1
                @productOffersPagerView.show()
            else
                @productOffersPagerView.hide()

        @productOpinionsCollection.on "sync", (collection) =>
            if collection.state.totalPages > 1
                @productOpinionPagerView.show()
            else
                @productOpinionPagerView.hide()
            if collection.state.totalRecords
                $('.tab-link[data-tab="reviews"]').find('span').text "(#{collection.state.totalRecords})"

        @productOffersCollection.fetchFiltered()
        @productOpinionsCollection.fetchFiltered {product: @productId}

        @channel.vent.on Events.SET_OFFERS_FILTER,  @onSetOffersFilter
        @channel.vent.on Events.OFFERS_SHOW_MORE,  @onOffersShowMore

        @channel.vent.on Events.OPEN_OFFERS_TAB,  @openOffersTab
        @channel.vent.on Events.OPEN_PROPS_TAB,  @openPropsTab

        @channel.vent.on Events.OPEN_REVIEWS_TAB,  @openReviewsTab
        @channel.vent.on Events.OPINIONS_SHOW_MORE,  @onReviewsShowMore

        @channel.vent.on Events.OPINIONS_NULL, @onNullOpinions

    index: =>
        console.log 'index'

    onNullOpinions: =>
        @productDetailView.hideReviews()

    openOffersTab: =>
        @productOffersLayout.show()
        @productTabsPropsView.hide()
        @productTabsReviewsView.hide()


    openPropsTab: =>
        @productTabsPropsView.show()
        @productOffersLayout.hide()
        @productTabsReviewsView.hide()


    openReviewsTab: =>
        @productTabsReviewsView.show()
        @productOffersLayout.hide()
        @productTabsPropsView.hide()


    onSetOffersFilter: =>
        filterData = @productOffersFilterView.getFilterData()
        productOffersFilterState = ProductOffersFilterState.fromArray filterData
        @productOffersCollection.state.pageSize = @productOffersCollection.startPageSize
        @productOffersCollection.fetchFiltered productOffersFilterState


    onOffersShowMore: =>
        filterData = @productOffersFilterView.getFilterData()
        productOffersFilterState = ProductOffersFilterState.fromArray filterData
        @productOffersCollection.state.pageSize = @productOffersCollection.state.pageSize + @productOffersCollection.showMoreSize
        @productOffersCollection.fetchFiltered productOffersFilterState


    onReviewsShowMore: =>
        @productOpinionsCollection.state.pageSize = @productOpinionsCollection.state.pageSize + @productOpinionsCollection.showMoreSize
        @productOpinionsCollection.fetchFiltered {product: @productId}
