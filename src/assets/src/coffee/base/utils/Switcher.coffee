$ = require 'jquery'


module.exports = class Switcher

    constructor: (el, options) ->
        @el = $(el)
        @checkbox = @el.find('input[type="checkbox"]')
        _ = @
        options = options or {}
        onCheck = options.onCheck or null
        onUncheck = options.onUncheck or null

        @el.on 'click', (e) =>
            e.stopPropagation()
            if _.checkbox.is ':checked'
                _.el.addClass 'on'
            else
                _.el.removeClass 'on'

        @el.on 'change', (e) =>
            if _.checkbox.is ':checked'
                if onCheck
                    onCheck()
            else
                if onUncheck
                    onUncheck()