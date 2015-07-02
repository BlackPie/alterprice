$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientWalletPaymentView = require './ClientWalletPaymentView'
WalletPaymentsCompositeTemplate = require 'templates/client/WalletPaymentsComposite'


module.exports = class ClientWalletPaymentsCollectionView extends Marionette.CompositeView
    template: false

    childViewContainer: 'tbody'

    template: WalletPaymentsCompositeTemplate

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ClientWalletPaymentView

    childViewOptions: (model, index) =>
        return {channel: @channel}