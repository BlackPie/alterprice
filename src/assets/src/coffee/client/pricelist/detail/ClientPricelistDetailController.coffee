$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'
Switcher = require 'base/utils/Switcher'
ClientPriceListDetailParamsFormView = require './views/ClientPriceListDetailParamsFormView'
ClientPricelistDetailInfoView = require './views/ClientPricelistDetailInfoView'
ClientPricelistDetailManagmentView = require './views/ClientPricelistDetailManagmentView'


module.exports = class ClientPricelistDetailController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}
        @clientPriceListDetailParamsFormView = new ClientPriceListDetailParamsFormView {channel: @channel}
        @clientPricelistDetailInfoView = new ClientPricelistDetailInfoView {channel: @channel}
        @clientPricelistDetailManagmentView = new ClientPricelistDetailManagmentView {channel: @channel}


    index: () =>
        console.log 'index'