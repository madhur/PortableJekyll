require 'jekyll'
require 'html/pipeline'

module Jekyll
  class Mentions < Jekyll::Generator
    safe true

    DEFAULT_URL = "https://github.com"

    def initialize(config = Hash.new)
      @filter = HTML::Pipeline::MentionFilter.new(nil, {:base_url => base_url(config['jekyll-mentions']) })
    end

    def generate(site)
      site.pages.each { |page| mentionify page if html_page?(page) }
      site.posts.each { |post| mentionify post }
      site.docs_to_write.each { |doc| mentionify doc }
    end

    def mentionify(page)
      return unless page.content.include?('@')
      page.content = @filter.mention_link_filter(page.content)
    end

    def html_page?(page)
      page.html? || page.url.end_with?('/')
    end

    def base_url(configs)
      case configs
      when nil, NilClass
        DEFAULT_URL
      when String
        configs.to_s
      when Hash
        configs.fetch('base_url', DEFAULT_URL)
      else
        raise ArgumentError.new("Your jekyll-mentions config has to either be a string or a hash! It's a #{configs.class} right now.")
      end
    end
  end
end
