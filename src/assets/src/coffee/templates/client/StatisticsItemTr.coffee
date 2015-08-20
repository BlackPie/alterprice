Number = require 'base/utils/Number'

template = (locals) =>

    if not locals.sum
        locals.sum = 0

    if locals.type is 'offer'
        link = "/product/detail/#{locals.id}/"
    else
        link = "/catalog/#{locals.id}/products/"

    return "
        <td><a href=\"#{link}\" target=\"_blank\">#{locals.name}</a></td>
        <th class=\"text-center\">#{locals.count}</th>
        <th class=\"text-center\">#{locals.sum}</th>
    "

module.exports = template
