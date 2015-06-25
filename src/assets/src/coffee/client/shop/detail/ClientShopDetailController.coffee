$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
ClientShopDetailFormView = require './views/ClientShopDetailFormView'


module.exports = class ClientShopDetailController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientShopDetailFormView = new ClientShopDetailFormView {channel: @channel}


    index: () =>
        console.log 'index'