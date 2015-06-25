$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

LeftMenuView = require 'base/views/LeftMenuView'
ClientProfileFormView = require './views/ClientProfileFormView'


module.exports = class ClientProfileController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientProfileFormView = new ClientProfileFormView {channel: @channel}


    index: () =>
        console.log 'index'