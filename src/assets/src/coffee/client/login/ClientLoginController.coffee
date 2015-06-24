$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

ClientLoginFormView = require 'client/login/views/ClientLoginFormView'


module.exports = class ClientLoginController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @clientLoginFormView = new ClientLoginFormView {channel: @channel}


    index: () =>
        console.log 'index'