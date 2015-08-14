Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
Wreqr = require 'backbone.wreqr'


module.exports = class BaseApp extends Marionette.Application
    channelName: 'defaultChannel'
    controllerClass: null
    routerClass: null
    urlRoot: "/"

    initialize: (options) =>
        channel = Wreqr.radio.channel @channelName
        controller = new @controllerClass {channel: channel, context: options.context}
        router = new @routerClass {controller: controller, channel: channel}

        Backbone.history.start({pushState: true, root: @urlRoot})
