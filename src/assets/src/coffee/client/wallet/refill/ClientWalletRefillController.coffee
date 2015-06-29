$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'
Events = require 'client/Events'

LeftMenuView = require 'base/views/LeftMenuView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'
ClientWalletRefillTabNavView = require './views/ClientWalletRefillTabNavView'
ClientWalletRefillOnlineFormView = require './views/ClientWalletRefillOnlineFormView'
ClientWalletRefillCardFormView = require './views/ClientWalletRefillCardFormView'


module.exports = class ClientWalletRefillController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}
        @clientWalletRefillTabNavView = new ClientWalletRefillTabNavView {channel: @channel}
        @clientWalletRefillOnlineFormView = new ClientWalletRefillOnlineFormView {channel: @channel}
        @clientWalletRefillCardFormView = new ClientWalletRefillCardFormView {channel: @channel}

        @channel.vent.on Events.WALLET_REFILL_CHANGE_TAB,  @onChangeTab


    index: () =>
        console.log 'index'


    onChangeTab: (tabName) =>
        if tabName == 'card'
            @clientWalletRefillOnlineFormView.closeTab()
            @clientWalletRefillCardFormView.openTab()
        else
            @clientWalletRefillCardFormView.closeTab()
            @clientWalletRefillOnlineFormView.openTab()