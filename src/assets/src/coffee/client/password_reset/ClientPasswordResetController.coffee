$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

ClientPasswordResetFormView = require './views/ClientPasswordResetFormView'


module.exports = class ClientPasswordResetController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @clientPasswordResetFormView = new ClientPasswordResetFormView {channel: @channel}


    index: () =>
        console.log 'index'