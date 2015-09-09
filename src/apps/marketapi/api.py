from json import loads
from time import sleep
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from django.core.cache import cache
from django.conf import settings


class MarketException(Exception):
    pass

class MarketHTTPError(Exception):
    pass


class MarketAPI(object):
    cache_ttl = 20 * 60

    @classmethod
    def _get_cached(cls, key):
        return cache.get(key)

    @classmethod
    def _set_cache(cls, key, value):
        cache.set(key, value)
        cache.expire(key, timeout=cls.cache_ttl)

    @classmethod
    def _exec(cls, params, url, retried=0):
        req = Request(
            url='%s?%s' % (url, urlencode(params)),
            headers={'Authorization': settings.MARKET_API_KEY},
            # method='GET',
        )

        try:
            x = urlopen(req)
            result = x.read().decode()
            x.close()
            sleep(0.2)
            return loads(result)
        except HTTPError as e:
            if e.code == 403 and retried < 20:
                sleep(0.5)
                return cls._exec(params, url, retried=retried+1)
            else:
                raise MarketHTTPError('%d %s' % (e.code, e.msg))
        except Exception as e:
            raise MarketHTTPError('%s' % str(e))

    @classmethod
    def get_offer(cls, offer_id, ip_addr=None, geo_id=None):
        if not ip_addr and not geo_id:
            raise MarketException('Must be passed ip_addr or geo_id')
        params = {}
        cache_key = 'yapi:offer:%s' % offer_id
        if ip_addr:
            params['ip_addr'] = ip_addr
            cache_key += ':ip_addr:%s' % ip_addr
        else:
            params['geo_id'] = geo_id
            cache_key += ':geo_id:%s' % str(geo_id)
        cached = cls._get_cached(cache_key)
        if cached:
            return cached
        url = 'https://api.content.market.yandex.ru/v1/offer/%s.json' % offer_id
        result = cls._exec(params, url)
        cls._set_cache(cache_key, result)
        return result

    @classmethod
    def get_model(cls, model_id, ip_addr=None, geo_id=None):
        if not ip_addr and not geo_id:
            raise MarketException('Must be passed ip_addr or geo_id')
        params = {}
        cache_key = 'yapi:model:%s' % model_id
        if ip_addr:
            params['ip_addr'] = ip_addr
            cache_key += ':ip_addr:%s' % ip_addr
        else:
            params['geo_id'] = geo_id
            cache_key += ':geo_id:%s' % str(geo_id)
        cached = cls._get_cached(cache_key)
        if cached:
            return cached
        url = 'https://api.content.market.yandex.ru/v1/model/%s.json' % model_id

        result = cls._exec(params, url)
        cls._set_cache(cache_key, result)
        return result

    @classmethod
    def search_offer(cls, query, geo_id):
        params = {'geo_id': geo_id, 'text': query,}
        url = 'https://api.content.market.yandex.ru/v1/search.json'
        return cls._exec(params, url)

    @classmethod
    def get_opinions(cls, model_id):
        url = 'https://api.content.market.yandex.ru/v1/model/%s/opinion.json' % str(model_id)
        return cls._exec({'geo_id': 225}, url)

    @classmethod
    def get_model_detail(cls, model_id):
        url = 'https://api.content.market.yandex.ru/v1/model/%s/details.json' % str(model_id)
        return cls._exec({'geo_id': 225}, url)

    @classmethod
    def get_category(cls, category_id):
        url = 'https://api.content.market.yandex.ru/v1/category/%s.json' % str(category_id)
        return cls._exec({'geo_id': 225}, url)

    @classmethod
    def get_top_categories(cls):
        return cls._exec({'geo_id': 225}, 'https://api.content.market.yandex.ru/v1/category.json')

    @classmethod
    def get_subcategies(cls, category_id):
        url = 'https://api.content.market.yandex.ru/category/%s/children.json' % str(category_id)
        return cls._exec({'geo_id': 225}, url)

    @classmethod
    def get_category_models(cls, category_id, page=1):
        url = 'https://api.content.market.yandex.ru/v1/category/%s/models.json' % str(category_id)
        return cls._exec({'geo_id': 225, 'page': page, 'count': 30}, url)
