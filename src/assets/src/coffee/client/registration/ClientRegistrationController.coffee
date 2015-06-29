$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

ClientRegistrationFormView = require 'client/registration/views/ClientRegistrationFormView'


module.exports = class ClientRegistrationController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @clientRegistrationFormView = new ClientRegistrationFormView {channel: @channel}


    index: () =>
        console.log 'index'