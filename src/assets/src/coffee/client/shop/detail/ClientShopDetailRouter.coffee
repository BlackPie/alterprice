Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientShopDetailRouter extends Marionette.AppRouter
    appRoutes:
        "client/shop/:id/": "index"
