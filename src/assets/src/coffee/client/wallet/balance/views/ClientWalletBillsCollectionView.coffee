$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ClientWalletBillView = require './ClientWalletBillView'
WalletBillsCompositeTemplate = require 'templates/client/WalletBillsComposite'


module.exports = class ClientWalletBillsCollectionView extends Marionette.CompositeView
    template: false

    childViewContainer: 'tbody'

    template: WalletBillsCompositeTemplate

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ClientWalletBillView

    childViewOptions: (model, index) =>
        return {channel: @channel}