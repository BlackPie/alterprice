$ = require 'jquery'
require 'jquery-form'
formSuccessTemplate = require 'templates/client/formSuccess'


module.exports = class Form

    constructor: (options) ->
        @form = options.form
        form = options.form
        successCallback = options.success
        @form.ajaxForm
            dataType: options.dataType or 'json'
            type: @form.attr 'method' or 'POST'
            beforeSubmit: =>
                options.form.find('.error-text, .form-error').remove()
                options.form.find('.has-error').removeClass 'has-error'
                form.find('*[type="submit"]').attr 'disabled', 'disabled'
            success: (response, jqForm, options) =>
                if response.status == 'success'
                    if response.redirect_to
                        window.location.href = response.redirect_to
                    else
                        if response.message
                            form.html(formSuccessTemplate(response))
                if successCallback
                    successCallback(response)
                form.find('*[type="submit"]').removeAttr 'disabled'
            error:  (response) =>
                if response.responseJSON.status == 'fail'
                    for fieldName of response.responseJSON.errors
                        if fieldName == 'non_field_errors'
                            options.form.prepend "<span class=\"form-error\">#{response.responseJSON.errors[fieldName]}</span>"
                        else
                            fieldWrapper = options.form.find("*[name=\"#{fieldName}\"]").closest '.field-wrapper'
                            fieldWrapper.addClass 'has-error'
                            fieldWrapper.find('.field-value').append "<span class=\"error-text\">#{response.responseJSON.errors[fieldName]}</span>"
                form.find('*[type="submit"]').removeAttr 'disabled'
