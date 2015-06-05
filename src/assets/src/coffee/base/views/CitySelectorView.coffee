$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'


module.exports = class CitySelectorView extends Marionette.ItemView
    el: $('#location-block')

    template: false

    ui:
        chooseCityBtn: '.choose-your-city-btn'
        cityChoicesWrapper: '.choose-your-city-wrapper'
        cityChoiceBtn: '.city-choice'

    events:
        "click @ui.chooseCityBtn": "onClickChooseCityBtn"
        "click @ui.cityChoiceBtn": "onClickCityChoiceBtn"


    initialize: (options) =>
        @channel = options.channel


    onClickChooseCityBtn: (e) =>
        e.preventDefault()
        cityChoicesWrapper = @$(@ui.cityChoicesWrapper)
        if cityChoicesWrapper.hasClass 'opened'
            cityChoicesWrapper.fadeOut 80
            cityChoicesWrapper.removeClass 'opened'
        else
            cityChoicesWrapper.fadeIn 80
            cityChoicesWrapper.addClass 'opened'


    onClickCityChoiceBtn: (e) =>
        e.preventDefault()
        city = @$(e.target).text()
        cityChoicesWrapper = @$(@ui.cityChoicesWrapper)
        @$(@ui.chooseCityBtn).text city
        cityChoicesWrapper.fadeOut 70
        cityChoicesWrapper.removeClass 'opened'