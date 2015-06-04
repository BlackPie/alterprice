$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'

CatalogMenuView = require 'base/views/CatalogMenuView'


module.exports = class DefaultController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @catalogMenuView = new CatalogMenuView {channel: @channel}


    index: () =>
        console.log 'index'