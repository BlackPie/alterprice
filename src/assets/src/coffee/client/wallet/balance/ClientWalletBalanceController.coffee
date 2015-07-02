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
        @clientWalletPaymentsCollection.fetchFiltered()


    index: () =>
        console.log 'index'