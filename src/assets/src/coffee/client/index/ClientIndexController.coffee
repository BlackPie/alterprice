$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'


module.exports = class ClientIndexController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel


    index: () =>
        console.log 'index'