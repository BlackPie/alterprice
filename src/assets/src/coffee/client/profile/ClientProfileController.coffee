$ = require 'jquery'
_ = require 'underscore'
Marionette = require 'backbone.marionette'
Backbone = require 'backbone'
Events = require 'client/Events'

LeftMenuView = require 'base/views/LeftMenuView'
ClientProfileFormView = require './views/ClientProfileFormView'
ClientHeaderView = require 'client/profile/views/ClientHeaderView'
ClientProfilePasswordFormView = require './views/ClientProfilePasswordFormView'
ClientProfileEmailFormView = require './views/ClientProfileEmailFormView'


module.exports = class ClientProfileController extends Marionette.Controller

    initialize: (options) =>
        @channel = options.channel
        @leftMenuView = new LeftMenuView {channel: @channel}
        @clientProfileFormView = new ClientProfileFormView {channel: @channel}
        @clientHeaderView = new ClientHeaderView {channel: @channel}
        @clientProfilePasswordFormView = new ClientProfilePasswordFormView {channel: @channel}
        @clientProfileEmailFormView = new ClientProfileEmailFormView {channel: @channel}

        @channel.vent.on Events.PROFILE_CHANGE_EMAIL,  @onChangeEmail


    index: () =>
        console.log 'index'


    onChangeEmail: (email) =>
        @clientProfileFormView.setEmail email