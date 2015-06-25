$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
ClientShopAddFormView = require './views/ClientShopAddFormView'


module.exports = class ClientShopAddController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientShopAddFormView = new ClientShopAddFormView {channel: @channel}


    index: () =>
        console.log 'index'