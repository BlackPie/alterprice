$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'
Events = require 'client/Events'

LeftMenuView = require 'base/views/LeftMenuView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'

ClientWalletBalanceLayout = require './layouts/ClientWalletBalanceLayout'

ClientWalletPaymentsCollection = require './collections/ClientWalletPaymentsCollection'
ClientWalletPaymentsCollectionView = require './views/ClientWalletPaymentsCollectionView'
ClientWalletPaymentsPager = require './views/ClientWalletPaymentsPager'

ClientWalletBillsCollection = require './collections/ClientWalletBillsCollection'
ClientWalletBillsCollectionView = require './views/ClientWalletBillsCollectionView'
ClientWalletBillsPager = require './views/ClientWalletBillsPager'



module.exports = class ClientWalletBalanceController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}

        @clientWalletBalanceLayout = new ClientWalletBalanceLayout {channel: @channel}

        @clientWalletPaymentsCollection = new ClientWalletPaymentsCollection()
        @clientWalletPaymentsCollectionView = new ClientWalletPaymentsCollectionView
            channel: @channel
            collection: @clientWalletPaymentsCollection
        @clientWalletBalanceLayout.paymentsList.show @clientWalletPaymentsCollectionView
        @clientWalletPaymentsPager = new ClientWalletPaymentsPager {channel: @channel}

        @clientWalletPaymentsCollection.fetchFiltered().done (response) =>
            options =
                pageSize: @clientWalletPaymentsCollection.state.pageSize
                currentPage: @clientWalletPaymentsCollection.state.currentPage
            @clientWalletPaymentsPager.render response, options

        @channel.vent.on Events.WALLET_PAYMENT_PAGER,  @onChangePaymentsPage

        @clientWalletBillsCollection = new ClientWalletBillsCollection()
        @clientWalletBillsCollectionView = new ClientWalletBillsCollectionView
            channel: @channel
            collection: @clientWalletBillsCollection

        @clientWalletBalanceLayout.billsList.show @clientWalletBillsCollectionView
        @clientWalletBillsPager = new ClientWalletBillsPager {channel: @channel}

        @clientWalletBillsCollection.fetchFiltered().done (response) =>
            options =
                pageSize: @clientWalletBillsCollection.state.pageSize
                currentPage: @clientWalletBillsCollection.state.currentPage
            @clientWalletBillsPager.render response, options

        @channel.vent.on Events.WALLET_BILLS_PAGER,  @onChangeBillsPage


    onChangePaymentsPage: (page) =>
        @clientWalletPaymentsCollection.getPage(page)


    onChangeBillsPage: (page) =>
        @clientWalletBillsCollection.getPage(page)


    index: () =>
        console.log 'index'