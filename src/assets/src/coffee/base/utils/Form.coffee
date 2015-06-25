$ = require 'jquery'
require 'jquery-form'


module.exports = class Form

    constructor: (options) ->
        @form = options.form

        successCallback = options.success

        @form.ajaxForm
            dataType: options.dataType or 'json'
            type: @form.attr 'method' or 'POST'
            beforeSubmit: =>
                options.form.find('.error-text').remove()
            success: (response, jqForm, options) =>
                if response.status == 'success'
                    if response.redirect_to
                        window.location.href = response.redirect_to

                if successCallback
                    successCallback()
            error:  (response) =>
                if response.responseJSON.status == 'fail'
                    for fieldName of response.responseJSON.errors
                        fieldWrapper = options.form.find("*[name=\"#{fieldName}\"]").closest '.field-wrapper'
                        fieldWrapper.find('.field-name').append "<span class=\"error-text\"> - #{response.responseJSON.errors[fieldName]}</span>"