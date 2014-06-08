# -*- coding: utf-8 -*-
require File.expand_path(File.dirname(__FILE__) + '/cub/version')
require 'yaml'
require 'open-uri'
require 'nokogiri'

module Cub
  @@companies = YAML.load_file(File.dirname(__FILE__) + '/../companies.yml')

  class CompanyException < StandardError
  end

  def self.company(code)
    if valid_code?(code)
      company_name(code)
    else
      raise CompanyException, "無効な証券コード"
    end
  end

  def self.price(code)
    if valid_code?(code)
       fetch_price(code)
    else
      raise CompanyException, "無効な証券コード"
    end
  end

  def self.per(code)
    if valid_code?(code)
       fetch_per(code)
    else
      raise CompanyException, "無効な証券コード"
    end
  end

  def self.pbr(code)
    if valid_code?(code)
       fetch_pbr(code)
    else
      raise CompanyException, "無効な証券コード"
    end
  end

  private
  def self.valid_code?(code)
    /^\d{4}$/ =~ code.to_s
  end

  def self.company_name(code)
    company = @@companies[code]

    if company.nil?
      raise CompanyException, "証券コードに対応する会社が存在しない"
    else
      company
    end
  end

  def self.fetch_price(code)
    url = "http://stocks.finance.yahoo.co.jp/stocks/detail/?code=#{code}"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)'
    doc = Nokogiri::HTML(open(url, 'User-Agent' => user_agent).read)
    doc.css('td[class=stoksPrice]').text.gsub(/(\d{0,3}),(\d{3})/, '\1\2').to_i
  end

  def self.fetch_per(code)
    url = "http://stocks.finance.yahoo.co.jp/stocks/detail/?code=#{code}"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)'
    doc = Nokogiri::HTML(open(url, 'User-Agent' => user_agent).read)
    doc.css('div[class=chartFinance] dl[class=tseDtl] dd[class="ymuiEditLink mar0"] strong').children[2].text.gsub(/\((連|単)\) /, "").to_f
  end

  def self.fetch_pbr(code)
    url = "http://stocks.finance.yahoo.co.jp/stocks/detail/?code=#{code}"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)'
    doc = Nokogiri::HTML(open(url, 'User-Agent' => user_agent).read)
    doc.css('div[class=chartFinance] dl[class=tseDtl] dd[class="ymuiEditLink mar0"] strong').children[3].text.gsub(/\((連|単)\) /, "").to_f
  end

end
