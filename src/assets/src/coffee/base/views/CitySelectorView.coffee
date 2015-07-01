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
        overlay: '.overlay'
        changeCityForm: '#change-city-form'

    events:
        "click @ui.chooseCityBtn": "onClickChooseCityBtn"
        "click @ui.cityChoiceBtn": "onClickCityChoiceBtn"
        "click @ui.overlay": "onClickOverlay"


    initialize: (options) =>
        @channel = options.channel


    onClickChooseCityBtn: (e) =>
        e.preventDefault()
        cityChoicesWrapper = @$(@ui.cityChoicesWrapper)
        if cityChoicesWrapper.hasClass 'opened'
            cityChoicesWrapper.fadeOut 80
            cityChoicesWrapper.removeClass 'opened'
            @$(@ui.overlay).hide()
        else
            cityChoicesWrapper.fadeIn 80
            cityChoicesWrapper.addClass 'opened'
            @$(@ui.overlay).show()


    onClickCityChoiceBtn: (e) =>
        e.preventDefault()
        cityChoicesWrapper = @$(@ui.cityChoicesWrapper)
        cityId = @$(e.target).attr 'data-value'
        @$(@ui.changeCityForm).find('input[name="city"]').val cityId
        @$(@ui.changeCityForm).submit()


    onClickOverlay: (e) =>
        e.preventDefault()
        cityChoicesWrapper = @$(@ui.cityChoicesWrapper)
        cityChoicesWrapper.fadeOut 70
        cityChoicesWrapper.removeClass 'opened'
        @$(@ui.overlay).hide()