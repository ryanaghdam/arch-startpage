#!/usr/bin/env python2.5

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class HomePage:
  def __init__(self, search_engines=[]):
    self.search_engines = search_engines

  def template_values(self):
    return { 'search_engines': self.search_engines }

  def build_url(self, key, term):
    return "%s%s" % (self.get_engine_url_by_key(key), term)

  def get_engine_url_by_key(self, key):
    for search_engine in self.search_engines:
      if search_engine.id == key:
        return search_engine.url

  def __str__(self):
    path = os.path.join(os.path.dirname(__file__), 'main.html')
    return template.render(path, self.template_values())

class SearchEngine:
  def __init__(self, id, label, url, selected=False):
    self.id = id
    self.label = label
    self.url = url
    self.selected = selected

  def template_values(self):
    return {
        'id': self.id,
        'label': self.label,
        'url': self.url,
        'selected': self.selected
        }

  def __str__(self):
    path = os.path.join(os.path.dirname(__file__), 'search-engine.html')
    return template.render(path, self.template_values())


class MainHandler(webapp.RequestHandler):
    def get(self):
      homepage = HomePage([
        SearchEngine('google', '<u>G</u>oogle', 
          'http://google.com/search?q='),
        SearchEngine('wiki', 'Arch<u>W</u>iki', 
          'http://wiki.archlinux.org/index.php?search='),
        SearchEngine('aur', '<u>A</u>UR',
          'http://aur.archlinux.org/packages.php?O=0&do_Search=Go&K=')
        ])

      if self.request.get('search-engine'):
        self.redirect(homepage.build_url(self.request.get('search-engine'),
          self.request.get('search-text')), permanent=False)
      else:
        self.response.out.write(homepage)

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
