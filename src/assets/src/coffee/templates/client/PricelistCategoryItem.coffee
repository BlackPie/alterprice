Number = require 'base/utils/Number'

template = (locals) =>
    if locals.viewURL
        name = "<a href=\"#{locals.viewURL}\" target=\"_blank\">#{locals.name}</a>"
    else
        name = locals.category.name

    return "
        <td>#{name}</td>
        <td class=\"text-center\">
            <div class=\"number-input-wrapper\">
                <button type=\"button\" class=\"increment-btn btn\"></button>
                <input type=\"text\" class=\"number-input\" value=\"#{locals.price}\" data-id=\"#{locals.id}\" />
                <button type=\"button\" class=\"decrement-btn btn\"></button>
            </div>
        </td>
        <td class=\"text-center\">#{locals.lead_price}</td>"


module.exports = template
