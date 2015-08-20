$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
ClientShopDetailView = require './views/ClientShopDetailView'
ClientShopDetailFormView = require './views/ClientShopDetailFormView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'


module.exports = class ClientShopDetailController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientShopDetailFormView = new ClientShopDetailFormView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}

    index: () =>
        @clientShopDetailView = new ClientShopDetailView {channel: @channel}
