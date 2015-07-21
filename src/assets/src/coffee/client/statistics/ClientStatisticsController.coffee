$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'

ClientStatisticsItemsFilterView = require './views/ClientStatisticsItemsFilterView'


module.exports = class ClientStatisticsController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}

        @clientStatisticsItemsFilterView = new ClientStatisticsItemsFilterView {channel: @channel}


    index: () =>
        console.log 'index'